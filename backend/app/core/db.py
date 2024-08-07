import logging
from pymongo import MongoClient

from backend.app.core.config import Settings

logger = logging.getLogger(__name__)


class Mongodb:
    _mongo_client = None

    def __init__(self):
        self._mongo_client = self.get_or_initialize_mongo_client()

    @classmethod
    def get_or_initialize_mongo_client(cls):
        if cls._mongo_client is None:
            cls._mongo_client = cls.initialize_mongo_client()
        return cls._mongo_client

    @staticmethod
    def initialize_mongo_client():
        try:
            logging.info("Initializing MongoDB client...")
            client = MongoClient(Settings.MONGO_DETAILS, tls=True)
            db = client.get_database(Settings.DATABASE_NAME)
            logging.info("Initialized MongoDB client.")
            return db
        except Exception as ex:
            logging.error(f"Error while initializing MongoDB client: {ex}")
            raise ValueError(f"Error initializing MongoDB client: {ex}")
