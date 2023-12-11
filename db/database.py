from db.config import setting
from sqlalchemy.ext.asyncio import create_async_engine


async_engine = create_async_engine(
    url=setting.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10)
