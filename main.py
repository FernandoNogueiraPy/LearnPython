import uvicorn
from fastapi import FastAPI

from src.routers import router

app = FastAPI()
app.include_router(router)

HOST = "0.0.0.0"
PORT = 8000


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
