from fastapi import APIRouter, Security
from fastapi.requests import Request

from src.controllers.home.controller_home import ControllerChallengeOverview
from src.security.auth import AuthSecurity


router_challenge_overview = APIRouter(dependencies=[Security(AuthSecurity())])


@router_challenge_overview.get("/challenge_overview", tags=["CHALLENGE OVERVIEW"])
async def challenge_overview(request: Request):
    return ControllerChallengeOverview().get_challenge_overview(
        request.state.user.id_player
    )
