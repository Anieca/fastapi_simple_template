from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

from fastapi_simple_template.container import Container
from fastapi_simple_template.routers import router

title = "FastAPI Simple Templete"
version = "2023.01.21.0"

container = Container()

app = FastAPI(title=title, version=version)


@app.get("/", response_class=HTMLResponse)
def root() -> HTMLResponse:
    return HTMLResponse(
        content=f"""
        <h2>{title}</h2>
        <a href=\"redoc\">redoc</a> / <a href=\"docs\">docs</a>
        """
    )


@app.get("/health", response_class=PlainTextResponse)
def health() -> PlainTextResponse:
    return PlainTextResponse("OK")


app.include_router(router)
