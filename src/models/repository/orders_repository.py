from typing import Dict, List


class OrdersRepository:
    def __init__(self, db_connection):
        self.__connection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> List:
        collection = self.__db_connection.get_collection(self.__connection_name)
        return collection.find(doc_filter)

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__connection_name)
        return collection.find_one(doc_filter)

    def select_many_with_properties(self, doc_filter: dict) -> List:
        collection = self.__db_connection.get_collection(self.__connection_name)
        return collection.find(doc_filter, {"_id": 0, "cupom": 0})

    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__connection_name)
        return collection.find({"address": {"$exists": True}})