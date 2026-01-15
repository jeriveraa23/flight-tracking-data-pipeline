from src.extractors.config import URL_HEXDB, URL_OPENSKY
from src.extractors.flight_extract import HexDBExtractor, OpenSkyExtractor
from src.loaders.flight_load import load_db
import pandas as pd
import time

def main():
    print("--- STARTING FLIGHT PIPELINE ---")

    hex_records = []

    #--- 1 STEP: EXTRACTION ---#
    #OpenSky extractor instance
    opensky_extractor = OpenSkyExtractor(URL_OPENSKY)

    # Call the OpenSky extraction method
    df_opensky = opensky_extractor.extract()

    if df_opensky is None or df_opensky.empty:
        print("No data received from OpenSky. Exiting...")
        return

    #Taking the unique icaos
    planes_names = df_opensky['icao24'].unique().tolist()

    for icao in planes_names[:60]:
        #HexDB extractor instance for each icao
        hexdb_extractor = HexDBExtractor(URL_HEXDB,icao)
        #Call the HexDB extraction method for each icao
        df_hexdb_temp = hexdb_extractor.extract()

        #Validate that the df is not empty and agg in list
        if df_hexdb_temp is not None and not df_hexdb_temp.empty:
            hex_records.append(df_hexdb_temp)
        
        time.sleep(0.5)
        
    #--- 2 STEP: UPLOAD ---#
    # If the dictionary list is not empty, it loads it
    if hex_records:
        df_hexdb = pd.concat(hex_records, ignore_index=True)
        loader = load_db()
        loader.to_postgres_os(df_opensky)
        loader.to_postgres_hdb(df_hexdb)

    print("--- PIPELINE SUCCESSFULLY COMPLETED ---")

if __name__ == "__main__":
    main()