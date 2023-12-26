from contextlib import asynccontextmanager

from db.config import setting
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


async_engine = create_async_engine(
    url=setting.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10)


async_session_factory = async_sessionmaker(async_engine)


@asynccontextmanager
async def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = async_session_factory()
    try:
        yield session
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()


class Base(DeclarativeBase):
    pass


# if __name__ == '__main__':
#     with session_scope() as session:
#         pass
