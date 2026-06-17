from ETL.infra.database_connector import DatabaseConnector


class loadCSV:
    def __init__(self):
        self.engine = DatabaseConnector.get_engine()

    
    def load(self, df, table_name='netflix_titles', if_exists='replace'):
        df.to_sql(
            name=table_name,
            con=self.engine,
            if_exists=if_exists,
            index=False
        )