import requests as rq
import pandas as pd

class ExtractorBase:
    """Parent class of extractors"""
    def __init__(self, source_name):
        self.source_name = source_name

    def extract(self):
        raise NotImplementedError("The extraction method must be implemented")
    
class OpenSkyExtractor(ExtractorBase):
    """OpenSky extraction class"""
    def __init__(self, url):
        super().__init__('OpenSky')
        self.url = url
    
    def extract(self):
        params = {
            'lamin': 4.0,
            'lomin': -77.5,
            'lamax': 8.5,
            'lomax': -73.0
        }

        try:
            with rq.get(self.url, params=params) as response:
                response.raise_for_status()
                data = response.json()
                columns = ['time','icao24','callsign','origin_country','time_position','last_contact','longitude','latitude',
                           'baro_altitude','on_ground','velocity','true_track','vertical_rate','sensors','geo_altitude',
                           'squawk','spi','position_source']
                states = data.get('states',[])
                for sublist in states:
                     sublist.insert(0,data.get('time',''))
                df = pd.DataFrame(states, columns=columns)
                return df
        except rq.exceptions.RequestException as e:
            print(f"Network or API error for OpenSky")
            return None
class HexDBExtractor(ExtractorBase):
    """HexDB extraction class"""
    def __init__(self, url, icao24):
        super().__init__('HexDB')
        self.url = url
        self.icao24 = icao24
    
    def extract(self):
        try:
            with rq.get(f"{self.url}{self.icao24}") as response:
                response.raise_for_status()
                data = response.json()
                df = pd.DataFrame([data])
                return df
        except rq.exceptions.RequestException as e:
            print(f"Network or API error for HexDB")
            return None

        
                
            