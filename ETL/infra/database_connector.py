import os
from dotenv import load_dotenv
from sqlalchemy import create_engine # type: ignore

load_dotenv()

class DatabaseConnector:

    @staticmethod
    def get_engine():

        return create_engine(
            f"postgresql+psycopg2://"
            f"{os.getenv('DB_USER')}:"
            f"{os.getenv('DB_PASSWORD')}"
            f"@{os.getenv('DB_HOST')}:"
            f"{os.getenv('DB_PORT')}/"
            f"{os.getenv('DB_NAME')}"
        )
