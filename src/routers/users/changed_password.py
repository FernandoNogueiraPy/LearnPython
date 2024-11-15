from fastapi import APIRouter
from src.services.users.controller_user import UserControler

router_changed_password = APIRouter()


@router_changed_password.post("/change_password", tags=["USERS"])
async def change_password_user(email: str, new_password: str):
    return UserControler().change_password(email, new_password)
