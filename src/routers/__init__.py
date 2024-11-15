from fastapi import APIRouter

from src.routers.documentation.document import document_app
from src.routers.users.auth_user import router_auth_user
from src.routers.users.register_user import router_register_user
from src.routers.home.home import router_challenge_overview
from src.routers.challenges.sort_challenge import router_random_challenge
from src.routers.challenges.response_challenge import router_response_challenge
from src.routers.users.request_password_reset import request_password_router
from src.routers.users.changed_password import router_changed_password
from src.routers.users.verify_code import verify_code_router


router = APIRouter()

router.include_router(document_app)

router.include_router(router_register_user)
router.include_router(router_auth_user)
router.include_router(request_password_router)
router.include_router(verify_code_router)
router.include_router(router_changed_password)

router.include_router(router_challenge_overview)
router.include_router(router_random_challenge)
router.include_router(router_response_challenge)
