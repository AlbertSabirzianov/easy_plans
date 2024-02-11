import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    def __init__(self):
        self.pg_host = os.getenv('PG_HOST')
        self.pg_port = os.getenv('PG_PORT')
        self.pg_user = os.getenv('PG_USER')
        self.pg_password = os.getenv('PG_PASSWORD')
        self.db_name = os.getenv('DB_NAME')

    @property
    def db_url(self):
        return f'postgresql+psycopg2://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.db_name}'

