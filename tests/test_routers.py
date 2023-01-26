from fastapi.testclient import TestClient


class TestRouters:
    def test_capitalize(self, client: TestClient) -> None:
        response = client.post("/capitalize", json={"text": "string"})
        assert response.status_code == 200
        assert response.json()["text"] == "String"
