from fastapi import APIRouter, Security
from fastapi.requests import Request

from src.entities.challenges.challenge_overview import ChallengeOverview
from src.services.home.controller_home import ControllerChallengeOverview
from src.security.auth import AuthSecurity


router_challenge_overview = APIRouter(dependencies=[Security(AuthSecurity())])


@router_challenge_overview.get(
    "/challenge_overview", tags=["CHALLENGE OVERVIEW"], response_model=ChallengeOverview
)
async def challenge_overview(request: Request) -> ChallengeOverview:
    return ControllerChallengeOverview().get_challenge_overview(
        request.state.user.id_player, request.state.user.username
    )
