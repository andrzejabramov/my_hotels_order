from pydantic_settings import BaseSettings, SettingsConfigDict


class Settigs(BaseSettings):

    DB_PORT: int
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    def DB_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settigs()