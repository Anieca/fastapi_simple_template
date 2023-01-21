FROM python:3.10 as builder

ARG POETRY_VERSION=1.3.2

ENV \
    # python
    PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUTF8=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY src/ src/

RUN \
    curl -sSL https://install.python-poetry.org | python && \
    ${POETRY_HOME}/bin/poetry install --only main

FROM builder as development

WORKDIR /app

COPY tests/ tests/
RUN ${POETRY_HOME}/bin/poetry install --with dev


FROM python:3.10-slim-bullseye

COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY src/fastapi_simple_template/gunicorn.conf.py gunicorn.conf.py

CMD ["gunicorn", "-c", "gunicorn.conf.py"]
