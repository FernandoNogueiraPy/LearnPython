from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
import base64


class BasicAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, username: str, password: str):
        super().__init__(app)
        self.username = username
        self.password = password

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        if request.url.path.startswith("/docs") or request.url.path.startswith(
            "/redoc"
        ):
            credentials = request.headers.get("Authorization")
            if not credentials or not self._check_credentials(credentials):
                return self._unauthorized_response()

        response = await call_next(request)
        return response

    def _check_credentials(self, credentials: str) -> bool:
        if not credentials.startswith("Basic "):
            return False
        encoded_credentials = credentials[len("Basic ") :]
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        username, password = decoded_credentials.split(":", 1)
        return username == self.username and password == self.password

    def _unauthorized_response(self) -> Response:
        return Response(
            "Unauthorized",
            status_code=401,
            headers={"WWW-Authenticate": "Basic realm='Access to the docs'"},
        )
