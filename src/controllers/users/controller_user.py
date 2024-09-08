from addemongo import QueryBuilder
from fastapi import HTTPException
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4
from re import match

from src.core.crypt_helper import CryptHelper
from src.repositories.users.connect_users import respository_users_sync
from src.entities.users.register_user import RegisterUser
from src.entities.users.login_user import LoginUser
from src.entities.users.auth_user import AuthUser
from src.entities.users.response_auth import ReponseAuth


from typing import ClassVar


class EmailValidator:
    email_pattern: ClassVar[str] = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    @classmethod
    def is_email(cls, value: str) -> bool:
        if match(cls.email_pattern, value):
            return True
        return False


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
    def register_user(self, form_register: RegisterUser) -> ReponseAuth:
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
            new_id_player = str(uuid4())
            new_user = LoginUser(id_player=new_id_player, **form_register.model_dump())
            new_user.password = ControllerPassword.hash_password(form_register.password)

            respository_users_sync.insert_one(new_user)

            acess_token = CryptHelper().encoder(
                payload={"player_id": new_user.id_player, "username": new_user.username}
            )

            response = ReponseAuth(
                player_id=new_user.id_player,
                access_token=acess_token,
                message="Usuário registrado com sucesso!",
            )

            return response

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Erro ao registrar usuário: {str(e)}"
            )

    def authenticate_user(self, form_auth: AuthUser) -> ReponseAuth:
        querybuild = QueryBuilder()

        validate_email = EmailValidator.is_email(form_auth.username_or_email)

        if validate_email:
            querybuild.set_equal("email", form_auth.username_or_email)
        else:
            querybuild.set_equal("username", form_auth.username_or_email)

        user = respository_users_sync.find_one(querybuild)

        if not user or not ControllerPassword.verify_password(
            user.password, form_auth.password
        ):
            raise HTTPException(status_code=400, detail="Erro: Credenciais inválidas.")

        acess_token = CryptHelper().encoder(
            payload={"player_id": user.id_player, "username": user.username}
        )

        response = ReponseAuth(
            player_id=user.id_player,
            access_token=acess_token,
            message="Usuário autenticado com sucesso!",
        )

        return response
