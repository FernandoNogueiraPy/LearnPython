from pydantic import BaseModel


class TeachingChallengeOne(BaseModel):
    pass


class ChallengeOne(BaseModel):
    name_desafio: str


class RewardsChallengeOne(BaseModel):
    name_reward: str
    description: str
    points: int
    id_player: str
    id_challenge: str
