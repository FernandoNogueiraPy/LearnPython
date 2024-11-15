from addemongo import QueryBuilder
from fastapi import HTTPException
from bcrypt import hashpw, gensalt, checkpw
from datetime import datetime
from datetime import timedelta
from random import choices
from uuid import uuid4
from re import match
import string

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import ClassVar


from src.core.crypt_helper import CryptHelper
from src.repositories.users.connect_users import respository_users_sync
from src.entities.users.register_user import RegisterUser
from src.entities.users.login_user import LoginUser
from src.entities.users.auth_user import AuthUser
from src.entities.users.response_auth import ReponseAuth
from src.templates.users.html_show_message import send_template_change_password
from src.config import SENDER_EMAIL, SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT
from src.entities.users.validation_code import ValidationCode

verification_codes_permission: dict[str, ValidationCode] = {}


class UserControler:
    email_pattern: ClassVar[str] = r"^[\w\.-]+@[\w\.-]+\.\w+$"

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
            new_user.password = self.hash_password(form_register.password)

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

        validate_email = self.is_email(form_auth.username_or_email)

        if validate_email:
            querybuild.set_equal("email", form_auth.username_or_email)
        else:
            querybuild.set_equal("username", form_auth.username_or_email)

        user = respository_users_sync.find_one(querybuild)

        if not user or not self.verify_password(user.password, form_auth.password):
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

    def send_verification_email(self, email: str, code: str):
        if not SENDER_EMAIL or not SENDER_PASSWORD or not SMTP_SERVER or not SMTP_PORT:
            raise Exception("Configurações de e-mail não encontradas")

        user_connection = respository_users_sync
        user = user_connection.find_one(QueryBuilder().set_equal("email", email))

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado com o e-mail informado.",
            )

        sender_email = SENDER_EMAIL
        sender_password = SENDER_PASSWORD
        smtp_server = SMTP_SERVER
        smtp_port = SMTP_PORT

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = "Código de Verificação para Redefinição de Senha"
        body = send_template_change_password(code)
        message.attach(MIMEText(body, "html"))

        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())

    def is_email(self, value: str) -> bool:
        if match(self.email_pattern, value):
            return True
        return False

    def generate_verification_code(self):
        return "".join(choices(string.ascii_uppercase + string.digits, k=6))

    def store_verification_code(self, email: str, code: str):
        expiration_time = datetime.utcnow() + timedelta(
            minutes=10
        )  # Código expira em 10 minutos
        verification_codes_permission[email] = ValidationCode(
            code=code, expires_at=expiration_time, change_password=False
        )

    def hash_password(self, password: str) -> str:
        salt = gensalt()
        hashed_password = hashpw(password.encode(), salt)
        return hashed_password.decode()

    def verify_password(self, stored_hash: str, password: str) -> bool:
        return checkpw(password.encode(), stored_hash.encode())

    def change_password(self, email: str, new_password: str):
        user_connection = respository_users_sync
        user = user_connection.find_one(QueryBuilder().set_equal("email", email))

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado com o e-mail informado.",
            )

        if not verification_codes_permission[email].change_password:
            raise HTTPException(
                status_code=400,
                detail="Código de verificação não foi validado para este e-mail.",
            )

        if verification_codes_permission[email].expires_at < datetime.now():
            raise HTTPException(
                status_code=400,
                detail="Código de verificação expirado.",
            )

        user.password = self.hash_password(new_password)
        user_connection.update_one(
            QueryBuilder().set_equal("id_player", user.id_player), user
        )

        return {"message": "Senha alterada com sucesso!"}
