import uvicorn
from fastapi import FastAPI

from product_views import router as product_router
from users.views import router as user_router
from contextlib import asynccontextmanager

from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)
app.include_router(product_router)
app.include_router(user_router)


@app.get("/")
def hello_world():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
