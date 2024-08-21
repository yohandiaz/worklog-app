from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn
from dotenv import load_dotenv


class Settings(BaseSettings):
    postgres_dsn: PostgresDsn

    model_config = SettingsConfigDict(case_sensitive=False, strict=True)

    @staticmethod
    def safe_constructor():

        load_dotenv()

        return Settings()  # type: ignore

    @property
    def sqlalchemy_database_url(self) -> str:

        return str(self.postgres_dsn)


engine = create_engine(Settings.safe_constructor().sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
