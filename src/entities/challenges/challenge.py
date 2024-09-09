from pydantic import BaseModel


class Challenge(BaseModel):
    id: str
    history_mode: bool
    challenge_postion_map: int
    difficulty: int
    mapa: str
    name: str
    explication: str
    description: str
    points: int
    exp: float
    options: list[str]


class ChallengeRandom(BaseModel):
    id: str
    challenge_postion_random: int
    difficulty: int
    mapa: str
    name: str
    explication: str
    description: str
    points: int
    exp: float
    options: list[str]
