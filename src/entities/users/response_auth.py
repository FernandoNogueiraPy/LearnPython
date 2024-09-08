from pydantic import BaseModel


class ReponseAuth(BaseModel):
    player_id: str
    access_token: str
    token_type: str = "bearer"
    message: str
