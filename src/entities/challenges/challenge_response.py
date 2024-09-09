from pydantic import BaseModel
from src.entities.rewards.reward_challenge import RewardsChallenge


class ChallengeReponseUser(BaseModel):
    id_challenge: str
    id_player: str
    response_user: str


class ResponseChallengeApp(BaseModel):
    message: str
    description: str
    next_challenge: bool
    reward: RewardsChallenge | None = None
