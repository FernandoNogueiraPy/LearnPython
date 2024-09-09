from typing import Dict, Type, Any
from src.errors.model_exception import HTTPExceptionModel


def generate_error_responses(
    *exceptions: Type[HTTPExceptionModel],
) -> Dict[int | str, Dict[str, Any]]:
    responses: Dict[int | str, Dict[str, Any]] = {}
    for exception in exceptions:
        exc_instance = exception()  # type: ignore
        responses[exc_instance.status_code] = {
            "description": exc_instance.error,
            "content": {
                "application/json": {"example": {"detail": exc_instance.detail}}
            },
        }
    return responses
