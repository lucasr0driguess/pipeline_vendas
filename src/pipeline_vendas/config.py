import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

load_dotenv()



class Settings:


    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_USER')
    DB_NAME = os.getenv('DB_USER')
    DB_HOST = os.getenv('DB_HOST')
    DB_URL = os.getenv('DB_URL')



Settings = Settings()