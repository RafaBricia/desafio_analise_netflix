from ETL.stages.transform.transform_csv import transformCSV
from ETL.stages.load.load_csv import loadCSV

def main():

    transformer = transformCSV(
    'ETL/drives/netflix_titles.csv'
)

    df = transformer.transform()

    df.to_csv('ETL/drives/netflix_titles_transformed.csv', index=False)

    loader = loadCSV()

    loader.load(df)

    print("ETL executado com sucesso!")


if __name__ == "__main__":
    main()