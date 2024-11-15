from fastapi import APIRouter, Security
from fastapi.requests import Request
from src.security.auth import AuthSecurity

<<<<<<< HEAD
from src.services.challengers.challenge_response import response_challenge_one
=======
from src.controllers.challengers.challenge_response import ControllerChallengeResponse
>>>>>>> ede1bf39575fdd3e6171b69638473a1e56a609e8
from src.entities.challenges.challenge_response import ResponseChallengeApp
from src.entities.challenges.challenge_response import ChallengeReponseUser

router_response_challenge = APIRouter(dependencies=[Security(AuthSecurity())])


@router_response_challenge.post("/response_challenge", tags=["CHALLENGES"])
async def response_challenge(
    request: Request, response: ChallengeReponseUser, history_mode: bool = False
) -> ResponseChallengeApp:
    controller = ControllerChallengeResponse()
    return controller.check_response(response, history_mode)
