import uvicorn
import sys
from pathlib import Path
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.routers.hotels import router as rout_hotels


app = FastAPI()


app.include_router(rout_hotels)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)