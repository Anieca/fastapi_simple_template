from fastapi.testclient import TestClient


class TestMain:
    def test_root(self, client: TestClient) -> None:
        assert client.get("/").status_code == 200

    def test_health(self, client: TestClient) -> None:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.text == "OK"
