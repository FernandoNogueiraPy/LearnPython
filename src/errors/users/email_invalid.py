from src.errors.model_exception import HTTPExceptionModel


class EmailInvalid(HTTPExceptionModel):
    def __init__(self):
        super().__init__(
            status_code=400,
            error="Email inválido",
            detail="O endereço de e-mail é inválido.",
        )
