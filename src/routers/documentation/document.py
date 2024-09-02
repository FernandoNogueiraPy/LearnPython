from fastapi import APIRouter
from fastapi.responses import HTMLResponse

document_app = APIRouter(tags=["DOCUMENTATION"])


@document_app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def documentation() -> str:
    with open("src/templates/index.html", "r") as f:
        html_content = f.read()

    return html_content
