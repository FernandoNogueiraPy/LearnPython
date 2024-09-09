from fastapi import HTTPException


class HTTPExceptionModel(HTTPException):
    def __init__(
        self,
        status_code: int,
        error: str,
        detail: str,
    ):
        self.error = error
        super().__init__(status_code=status_code, detail=detail)
