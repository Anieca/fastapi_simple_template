from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from fastapi_simple_template.main import app


@pytest.fixture
def client() -> Iterator[TestClient]:
    yield TestClient(app)
