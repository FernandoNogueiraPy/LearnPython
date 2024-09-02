from pydantic import BaseModel, EmailStr, field_validator, Field
from uuid import uuid4


class RegisterUser(BaseModel):
    id_player: str = Field(default_factory=lambda: str(uuid4()))
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
