from src.errors.model_exception import HTTPExceptionModel


class UsernameLenInvalid(HTTPExceptionModel):
    def __init__(self):
        super().__init__(
            status_code=400,
            error="Username inválido",
            detail="O seu nickname deve ter no mínimo 3 caracteres ou mais.",
        )


class UsernameCharsInvalid(HTTPExceptionModel):
    def __init__(self):
        super().__init__(
            status_code=400,
            error="Username inválido",
            detail="O seu nickname não pode conter '@' ou '{}'.",
        )
