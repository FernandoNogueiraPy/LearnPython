from addemongo import QueryBuilder
from fastapi import HTTPException
from bcrypt import hashpw, gensalt, checkpw


from src.core.crypt_helper import CryptHelper
from src.repositories.users.connect_users import respository_users_sync
from src.entities.users.register_user import RegisterUser
from src.entities.users.login_user import LoginUser
from src.entities.users.auth_user import AuthUser


class ControllerPassword:
    @classmethod
    def hash_password(cls, password: str) -> str:
        salt = gensalt()
        hashed_password = hashpw(password.encode(), salt)
        return hashed_password.decode()

    @classmethod
    def verify_password(cls, stored_hash: str, password: str) -> bool:
        return checkpw(password.encode(), stored_hash.encode())


class UserControler:
    def register_user(self, form_register: RegisterUser):
        querybuild = QueryBuilder()
        querybuild.set_equal("email", form_register.email)
        querybuild.set_equal("username", form_register.username)

        result = respository_users_sync.find_one(querybuild)

        if result:
            if form_register.username:
                raise HTTPException(
                    status_code=400,
                    detail=f"Erro: O nome de usuário '{form_register.username}' já está em uso.",
                )
            elif form_register.email:
                raise HTTPException(
                    status_code=400,
                    detail=f"Erro: O email '{form_register.email}' já está em uso.",
                )

        try:
            new_user = LoginUser(**form_register.model_dump())
            new_user.password = ControllerPassword.hash_password(form_register.password)

            respository_users_sync.insert_one(new_user)

            acess_token = CryptHelper().encoder(
                payload={"player_id": new_user.id_player}
            )

            response = {
                "player_id": new_user.id_player,
                "access_token": acess_token,
                "token_type": "bearer",
                "message": "Usuário registrado com sucesso!",
            }

            return response

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Erro ao registrar usuário: {str(e)}"
            )

    def authenticate_user(self, form_auth: AuthUser):
        querybuild = QueryBuilder()
        querybuild.set_equal("username", form_auth.username)

        user = respository_users_sync.find_one(querybuild)

        if not user:
            raise HTTPException(status_code=400, detail="Erro: Usuário não encontrado.")

        if not ControllerPassword.verify_password(user.password, form_auth.password):
            raise HTTPException(status_code=400, detail="Erro: Senha inválida.")

        # Gerar token JWT
        acess_token = CryptHelper().encoder(payload={"player_id": user.id_player})

        response = {
            "player_id": user.id_player,
            "access_token": acess_token,
            "token_type": "bearer",
            "message": "Usuário autenticado com sucesso!",
        }

        return response
