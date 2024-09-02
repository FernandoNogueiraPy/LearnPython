from fastapi import HTTPException
import jwt
import datetime
from typing import Any

from src.config import SECRET_KEY, ALGORITHM

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY not set")

if ALGORITHM is None:
    raise ValueError("ALGORITHM not set")


class ControllerToken:
    @staticmethod
    def create_access_token(
        data: dict[str, Any], expires_delta: datetime.timedelta = None
    ) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> dict[str, Any]:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
