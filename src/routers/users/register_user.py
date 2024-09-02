from fastapi import APIRouter
from src.entities.users.register_user import RegisterUser
from src.controllers.users.controller_user import UserControler

router_register_user = APIRouter()


@router_register_user.post("/register", tags=["USERS"])
def register_user(register_user: RegisterUser):
    return UserControler().register_user(register_user)
