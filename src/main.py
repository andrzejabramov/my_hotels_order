import uvicorn
from fastapi import FastAPI

from routers.hotels import router as rout_hotels


app = FastAPI()


app.include_router(rout_hotels)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)