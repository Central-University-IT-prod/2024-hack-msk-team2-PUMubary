from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from data.config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_mysql,
    echo=False,
)

session_factory = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass