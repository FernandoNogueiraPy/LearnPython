from pydantic import BaseModel


class PlayerExp(BaseModel):
    level: int = 0
    exp_current: float = 0.0
    exp_next_level: float = 100.0


class PlayerRank(BaseModel):
    rank_current: str = "Novato Tecnológico"
    info_level: PlayerExp = PlayerExp()
