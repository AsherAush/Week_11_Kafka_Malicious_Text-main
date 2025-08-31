from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class MongoFetcher:
    def __init__(self):
        # קריאת פרטי התחברות מקובץ env
        self.uri = os.getenv('MONGO_URI')
        self.db_name = os.getenv("DB_NAME")
        self.collection_name = os.getenv("COLLECTION_NAME")

        # התחברות לmongoDB
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    # שליפת ה100 הודעות האחרונות בכל פעם
    def fetch_messagas(self):
        messages = list(self.collection.find().sort("createDate", -1).limit(100))
        for msg in messages:
            msg["_id"] = str(msg["_id"])
        return messages

