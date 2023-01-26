from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from fastapi_simple_template.main import app


class TestRouters:
    @pytest.fixture
    def client(self) -> Iterator[TestClient]:
        yield TestClient(app)

    def test_capitalize(self, client: TestClient) -> None:
        response = client.post("/capitalize", json={"text": "string"})
        assert response.status_code == 200
        assert response.json()["text"] == "String"
