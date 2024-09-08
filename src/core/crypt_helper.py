from datetime import timedelta
from typing import Any
from src.config import SECRET_KEY, ALGORITHM

from jwt import decode, encode  # type: ignore


class CryptHelper:
    @staticmethod
    def decoder(token: str) -> dict[str, Any]:
        """
        Decode the given token.

        Args:
            token (str): The token to decode.
        """

        return decode(
            token,
            key=str(SECRET_KEY),
            algorithms=[str(ALGORITHM)],
            verify=True,
            leeway=timedelta(hours=1),
        )

    @staticmethod
    def encoder(payload: dict[str, Any]) -> str:
        """
        Encode the given payload.

        Args:
            payload (dict[str, str]): The payload to encode.
            expire_in (int, optional): The time in hours to expire the token.
                Defaults to None.
        """

        return str(encode(payload, key=str(SECRET_KEY), algorithm=str(ALGORITHM)))
