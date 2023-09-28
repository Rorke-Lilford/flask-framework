import pymongo


class Database(object):

    DATABASE = None

    def __init__(self, CONN_STR) -> None:
        self.CONN_STR = CONN_STR

    # Initialize MongoDB connection - Must be run in app python file
    def initialize(self):
        client = pymongo.MongoClient(self.CONN_STR)
        Database.DATABASE = client['<your_database_name>']

    @staticmethod
    def find(collection: str, query=None):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: dict):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def insert_one(collection: str, data: dict):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def insert_many(collection: str, data: list):
        Database.DATABASE[collection].insert_many(data)

    @staticmethod
    def update_one(collection: str, filter: dict, data: dict):
        Database.DATABASE[collection].update_one(filter, {"$set": data})
