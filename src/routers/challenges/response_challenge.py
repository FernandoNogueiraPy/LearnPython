from fastapi import APIRouter, Security
from fastapi.requests import Request
from src.security.auth import AuthSecurity

from src.entities.challenges.challenge_response import ResponseChallengeApp
from src.entities.challenges.challenge_response import ChallengeReponseUser

from src.services.challengers.challenge_response import (
    ControllerChallengeResponse,
)

router_response_challenge = APIRouter(dependencies=[Security(AuthSecurity())])


@router_response_challenge.post("/response_challenge", tags=["CHALLENGES"])
async def response_challenge(
    request: Request, response: ChallengeReponseUser, history_mode: bool = False
) -> ResponseChallengeApp:
    controller = ControllerChallengeResponse()
    return controller.check_response(response, history_mode)
