from pydantic import BaseModel


class RewardsChallenge(BaseModel):
    name_reward: str
    description: str
    points: int
    id_player: str
    id_challenge: str
