from fastapi import FastAPI
from fastapi.responses import HTMLResponse

title = "FastAPI Simple Templete"
version = "2023.01.21.0"

app = FastAPI(title=title, version=version)


@app.get("/", response_class=HTMLResponse)
def root() -> HTMLResponse:
    return HTMLResponse(
        content=f"""
        <h2>{title}</h2>
        <a href=\"redoc\">redoc</a> / <a href=\"docs\">docs</a>
        """
    )
