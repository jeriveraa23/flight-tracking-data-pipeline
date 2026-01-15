import pandas as pd
from sqlalchemy import create_engine

class load_db():
    """PostgreSQL load class"""
    def __init__(self):
        self.url_db = "postgresql://admin_flight:flight_202*@postgres_db:5432/flight_db"
        self.engine = create_engine(self.url_db)
    
    def to_postgres_os(self, df_os:pd.DataFrame, table_name = "flights_history"):
        print(F"\n--- STARTING LOADING PHASE IN BD WITH TABLE {table_name} ---")

        try:
            with self.engine.begin() as connection:
                print(f"Connection established, loading data into the table {table_name}...")
                df_os.to_sql(
                    name=table_name,
                    con=connection,
                    if_exists='append',
                    index=False
                )
                print(f"{len(df_os)} records have been successfully uploaded")
        except Exception as e:
            print(f"Loading failure: {e}")
            raise
    
    def to_postgres_hdb(self, df_hdb:pd.DataFrame, table_name = "aircraft_info"):
        print(F"\n--- STARTING LOADING PHASE IN BD WITH TABLE {table_name} ---")

        try:
            with self.engine.begin() as connection:
                print(f"Connection established, loading data into the table {table_name}...")
                df_hdb.to_sql(
                    name=table_name,
                    con=connection,
                    if_exists='replace',
                    index=False
                )
                print(f"{len(df_hdb)} records have been successfully uploaded")
        except Exception as e:
            print(f"Loading failure: {e}")
            raise