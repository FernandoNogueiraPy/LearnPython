from pydantic import BaseModel
from uuid import UUID


class PlayerExp(BaseModel):
    level: int = 0
    exp_current: float
    exp_next_level: float


class PlayerRank(BaseModel):
    id_player: UUID
    username: str
    rank_current: str = "Novato Tecnológico"
    info_level: PlayerExp
