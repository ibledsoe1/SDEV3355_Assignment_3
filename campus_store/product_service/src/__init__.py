from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.items.routes import item_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server starting")
    await init_db()
    yield
    print("server shutting down")

app = FastAPI(
    title="Store service",
    version="0.1.0",
    description="A campus online store system",
    lifespan=lifespan,
)

app.include_router(item_router, tags=["items"])