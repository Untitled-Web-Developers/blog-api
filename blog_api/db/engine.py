from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .. import config

engine = create_async_engine(config.SQLALCHEMY_DATABASE_URL, echo=True, future=True)
sessionmaker = async_sessionmaker(
    bind=engine, expire_on_commit=False, autocommit=False
)


class BaseModel(DeclarativeBase):
    pass


async def make_session() -> AsyncSession:
    async with sessionmaker() as session:
        yield session
