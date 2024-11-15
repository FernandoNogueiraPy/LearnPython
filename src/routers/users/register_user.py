from fastapi import APIRouter

from src.entities.users.response_auth import ReponseAuth
from src.entities.users.register_user import RegisterUser
from src.services.users.controller_user import UserControler

from src.errors.create_error_response import generate_error_responses
from src.errors.users.email_invalid import EmailInvalid

router_register_user = APIRouter()
errors = generate_error_responses(EmailInvalid)


@router_register_user.post(
    "/register", tags=["USERS"], response_model=ReponseAuth, responses=errors
)
async def register_user(register_user: RegisterUser) -> ReponseAuth:
    return UserControler().register_user(register_user)
