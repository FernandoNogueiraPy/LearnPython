from pydantic import BaseModel


class AuthUser(BaseModel):
    username_or_email: str
    password: str
