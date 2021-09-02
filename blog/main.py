from fastapi import FastAPI
from . import schemas, models
from .database import engine
from .routers import blog

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
