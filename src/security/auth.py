from fastapi import Request, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from addemongo import QueryBuilder

from src.core.crypt_helper import CryptHelper
from src.repositories.users.connect_users import respository_users_async


class _Payload(BaseModel):
    player_id: str
    username: str


class AuthSecurity(APIKeyHeader):
    _crypt_helper = CryptHelper()
    _user_repo = respository_users_async

    def __init__(
        self,
        *,
        description: str | None = None,
        auto_error: bool = False,
    ) -> None:
        super().__init__(
            name="Authorization",
            description=description or "Bearer token",
            auto_error=auto_error,
        )

    def _get_token(self, request: Request):
        if authorization := (
            request.headers.get("Authorization") or request.cookies.get("Authorization")
        ):
            return authorization

    async def _validate_token(self, request: Request):
        token = self._get_token(request)

        if not token:
            raise HTTPException(status_code=401, detail="Token not found")

        payload = _Payload(**self._crypt_helper.decoder(token))
        query = QueryBuilder()
        query.set_equal("id_player", payload.player_id)

        if user := await self._user_repo.find_one(query):
            request.state.user = user
            return True

    async def __call__(self, request: Request) -> None:
        await self._validate_token(request)
