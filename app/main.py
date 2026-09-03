from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends
from app.core.dependencies import get_current_user
from app.core.config import settings
from app.schemas import UserDataResponse
from app.api.auth import router as auth_router
from app.db.db_connection import init_db,close_db

#Context Manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


#instaciating Application
app = FastAPI(lifespan=lifespan,
    title=settings.project_name,version=settings.project_version,
    description="This is a module for Login System with Messaging workers",
    )

app.include_router(router=auth_router,prefix='/api',tags=["Authenication"])


@app.get("/")
async def homepage():
    return {
        'hello,world!'
    }

@app.get("/api/auth/me")
async def loging(current_user: UserDataResponse = Depends(get_current_user)) -> UserDataResponse:
    return current_user
    