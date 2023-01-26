from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from fastapi_simple_template.main import app


class TestMain:
    @pytest.fixture
    def client(self) -> Iterator[TestClient]:
        yield TestClient(app)

    def test_root(self, client: TestClient) -> None:
        assert client.get("/").status_code == 200

    def test_health(self, client: TestClient) -> None:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.text == "OK"
