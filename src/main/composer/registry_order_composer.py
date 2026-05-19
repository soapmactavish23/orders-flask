from src.models.connection.connection_handler import db_connection_handler
from src.models.repository.orders_repository import OrdersRepository
from src.use_cases.registry_order import RegistryOrder


def registry_order_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    return RegistryOrder(model)
