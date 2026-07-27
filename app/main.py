from fastapi import FastAPI
from app.core.config import settings

#instaciating Application
app = FastAPI(
    title=settings.project_name,version=settings.project_version,
    description="This is a module for Login System with Messaging workers"
    )


@app.get("/")
async def homepage():
    return {
        'hello,world!'
    }