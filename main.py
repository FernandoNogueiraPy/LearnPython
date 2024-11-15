import uvicorn
from fastapi import FastAPI

from src.security.auth_document import BasicAuthMiddleware
from src.config import LOGIN_DOCUMENTATION, PASSWORD_DOCUMENTATION

from src.routers import router


app = FastAPI()

if not LOGIN_DOCUMENTATION or not PASSWORD_DOCUMENTATION:
    raise ValueError("Please set LOGIN_DOCUMENTATION and PASSWORD_DOCUMENTATION in .env file")

app.add_middleware(
    BasicAuthMiddleware, username=LOGIN_DOCUMENTATION, password=PASSWORD_DOCUMENTATION #type: ignore
)
app.include_router(router)

HOST = "0.0.0.0"
PORT = 8000


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
