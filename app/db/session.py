from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.core.config import settings
from typing import AsyncGenerator

if settings.debug:
    DB_URL = settings.db_url
else:
    DB_URL = settings.db_url

# Create the async engine
engine = create_async_engine(
    url=DB_URL,
    echo=settings.debug,
    pool_pre_ping=True
)

# Bind the engine with async_sessionmaker
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False
)

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()