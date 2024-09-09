from pydantic import BaseModel, EmailStr, field_validator
from re import search

from src.errors.users.email_invalid import EmailInvalid


class RegisterUser(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str

    @field_validator("password", mode="before")
    def password_must_be_strong(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

    @field_validator("full_name", mode="before")
    def full_name_cannot_be_empty(cls, value: str):
        if not value.strip():
            raise ValueError("Full name cannot be empty")
        return value

    @field_validator("username", mode="before")
    def username_valid(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("O seu nickname deve ter no mínimo 3 caracteres")

        forbidden_chars = r"[@{}]"
        if search(forbidden_chars, value):
            raise EmailInvalid()
        return value
