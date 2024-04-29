from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    db_name: str
    db_user: str
    db_host: str
    db_port: str
    db_pass: str

    yandex_geocoder_api_key: str = '935552d3-68a0-49f4-b922-b98d44419799'

    def get_db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
