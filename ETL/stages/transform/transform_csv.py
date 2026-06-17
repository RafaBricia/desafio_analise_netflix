import pandas as pd
from ETL.stages.extract.extract_csv import extractCSV

class transformCSV:
    def __init__(self, path):
        self.path = path

    def transform(self):
        df = extractCSV(self.path).extract()
        
        df.drop_duplicates(inplace=True)

        df['date_added'] = pd.to_datetime(
        df['date_added'],
        format='%B %d, %Y',
        errors='coerce' )
        
        return df