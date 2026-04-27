from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.pool import NullPool

from app.core.config import settings

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.supabase_db_user,
    password=settings.supabase_db_password,
    host=settings.supabase_db_host,
    port=settings.supabase_db_port,
    database=settings.supabase_db_name,
    query={"sslmode": "require"},
)

engine = create_engine(DATABASE_URL, poolclass=NullPool)


def test_db_connection() -> bool:
    with engine.connect() as connection:
        connection.execute(text("select 1"))
    return True