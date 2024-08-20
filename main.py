from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get(
    "/", response_class=HTMLResponse, tags=["DOCUMENTATION"], include_in_schema=False
)
async def documentation() -> str:
    with open("src/templates/index.html", "r") as f:
        html_content = f.read()

    return html_content


HOST = "0.0.0.0"
PORT = 8000


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
