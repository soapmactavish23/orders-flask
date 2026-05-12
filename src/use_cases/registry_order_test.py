from src.main.http_types.http_request import HttpRequest
from src.use_cases.registry_order import RegistryOrder


class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.inser_document_att = {}

    def insert_document(self, document: dict) -> None:
        self.inser_document_att["document"] = document

def test_registry():
    repo = OrdersRepositoryMock()
    registry_order = RegistryOrder(repo)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "joaozinho",
                "address": "rua do limao",
                "cupom": False,
                "items": [
                    {"item": "Refrigerante", "quantity": 2},
                    {"item": "Pizza", "quantity": 3},
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)

    assert "name" in repo.inser_document_att["document"]
    assert "address" in repo.inser_document_att["document"]
    assert "created_at" in repo.inser_document_att["document"]

    assert response.status_code == 201
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["type"] == "Order"