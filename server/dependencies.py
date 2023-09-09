from server.config import Settings
from repositories.user import UserRepository
from databases import Database


settings = Settings()
db_url = "postgresql+asyncpg://" + \
    f"{settings.db_user}:{settings.db_pass}@" + \
    f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
database = Database(url=db_url)
user_repo = UserRepository(database=database)


def get_settings() -> Settings:
    return settings


def get_database() -> Database:
    return database


def get_user_repo() -> UserRepository:
    return user_repo
