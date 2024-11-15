from fastapi import APIRouter

from src.services.users.controller_user import UserControler

request_password_router = APIRouter()


@request_password_router.post("/request-password-reset", tags=["USERS"])
async def request_password_reset(email: str):
    user_service = UserControler()
    code = user_service.generate_verification_code()
    user_service.store_verification_code(email, code)
    user_service.send_verification_email(email, code)
    return {
        "message": "Código de verificação enviado para o e-mail, verifique sua caixa de entrada."
    }
