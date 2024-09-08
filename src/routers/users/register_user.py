from fastapi import APIRouter

from src.entities.users.response_auth import ReponseAuth
from src.entities.users.register_user import RegisterUser
from src.controllers.users.controller_user import UserControler

router_register_user = APIRouter()


@router_register_user.post("/register", tags=["USERS"], response_model=ReponseAuth)
async def register_user(register_user: RegisterUser) -> ReponseAuth:
    return UserControler().register_user(register_user)
