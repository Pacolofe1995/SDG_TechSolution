from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    VERSION: str = "1.0.0"
    NAME: str = "SDG API"
    DESCRIPTION: str = "SDG API"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "SDG API Project"

settings = Settings()