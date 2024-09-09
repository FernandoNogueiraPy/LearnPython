from fastapi import APIRouter, Security
from src.security.auth import AuthSecurity

from src.controllers.challengers.controller_challenges import ControllerChallenges
from src.entities.challenges.challenge import ChallengeRandom

router_random_challenge = APIRouter(dependencies=[Security(AuthSecurity())])


@router_random_challenge.get("/random_challenge", tags=["CHALLENGES"])
async def sort_challenge() -> ChallengeRandom:
    return ControllerChallenges().random_challenge()
