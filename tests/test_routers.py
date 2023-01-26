import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from fastapi_simple_template.main import container


class TestRouters:
    def test_mocked_capitalize(self, client: TestClient, mocker: MockerFixture) -> None:
        text_operation_service_mock = mocker.MagicMock()
        mocker.patch.object(text_operation_service_mock, "capitalize", return_value="")

        with container.text_operation_service.override(text_operation_service_mock):
            response = client.post("/capitalize", json={"text": "string"})

        assert response.status_code == 200
        assert response.json()["text"] == ""

    @pytest.mark.integration
    def test_capitalize(self, client: TestClient) -> None:
        response = client.post("/capitalize", json={"text": "string"})
        assert response.status_code == 200
        assert response.json()["text"] == "String"


# pyright: reportUnknownMemberType=false
