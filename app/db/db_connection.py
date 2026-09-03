from app.db.session import engine
from app.models import Base


#init db

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    except Exception as e:
        print("database Connection failed")
        print(f"ERROR {e}")

async def close_db():
    await engine.dispose()
