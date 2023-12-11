from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self) -> str:
        return (f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')

    model_config = SettingsConfigDict(env_file='.env')


setting = Settings()
