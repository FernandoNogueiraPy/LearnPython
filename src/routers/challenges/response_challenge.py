from fastapi import APIRouter, Security
from fastapi.requests import Request
from src.security.auth import AuthSecurity

from src.controllers.challengers.challenge_response import response_challenge_one
from src.entities.challenges.challenge_response import ResponseChallengeApp
from src.entities.challenges.challenge_response import ChallengeReponseUser

router_response_challenge = APIRouter(dependencies=[Security(AuthSecurity())])


@router_response_challenge.post("/response_challenge", tags=["CHALLENGES"])
async def response_challenge(
    request: Request, response: ChallengeReponseUser
) -> ResponseChallengeApp:
    return response_challenge_one(response)
