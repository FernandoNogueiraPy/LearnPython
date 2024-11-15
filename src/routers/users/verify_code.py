from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
from src.services.users.controller_user import verification_codes_permission


verify_code_router = APIRouter()


@verify_code_router.post("/verify-code", tags=["USERS"])
async def verify_code(email: str, code: str):
    stored_code_info = verification_codes_permission.get(email)

    if stored_code_info:
        code_time = stored_code_info.expires_at

        if not stored_code_info:
            raise HTTPException(
                status_code=404, detail="Código não encontrado ou expirado"
            )

        # Verificar se o código expirou
        if type(code_time) is datetime and datetime.utcnow() > code_time:
            del verification_codes_permission[email]  # Remove o código expirado
            raise HTTPException(status_code=400, detail="Código expirado")

        # Verificar se o código está correto
        if stored_code_info.code != code:
            raise HTTPException(status_code=400, detail="Código incorreto")

        verification_codes_permission[email].change_password = True

        return JSONResponse(
            status_code=200,
            content={
                "message": "Código verificado com sucesso. Você pode redefinir sua senha."
            },
            media_type="application/json",
        )

    raise HTTPException(
        status_code=404, detail="Nenhum código encontrado para o e-mail"
    )
