from fastapi import FastAPI
import uvicorn


from src.routers.documentation.document import document_app
from src.routers.users.register_user import router_register_user
from src.routers.users.auth_user import router_auth_user

app = FastAPI()

app.include_router(document_app)
app.include_router(router_register_user)
app.include_router(router_auth_user)

HOST = "0.0.0.0"
PORT = 8000


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
