from fastapi import APIRouter

from src.routers.documentation.document import document_app
from src.routers.users.auth_user import router_auth_user
from src.routers.users.register_user import router_register_user
from src.routers.home.home import router_challenge_overview


router = APIRouter()

router.include_router(document_app)
router.include_router(router_register_user)
router.include_router(router_auth_user)
router.include_router(router_challenge_overview)
