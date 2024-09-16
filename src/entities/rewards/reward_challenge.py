from pydantic import BaseModel


class RewardsChallenge(BaseModel):
    name_reward: str
    description: str
    points: int
    exp: float
    id_player: str
    id_challenge: str
    complete_challenge: bool
