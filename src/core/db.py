from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.core.settings import settings

engine = create_async_engine(
    url=settings.get_db_url(),
)

async_session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False
)
