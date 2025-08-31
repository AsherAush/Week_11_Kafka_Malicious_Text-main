from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

class DataRetrieval:
    # חיבור למונגו דיבי
    def __init__(self, db_name='tweets_db'):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    # המרת הID לסטרינג
    def serialize(self, doc):
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        return doc

    # שליפת כל הדוקומנטס מהקולקשן כרשימה
    def get_collection(self, collection_name):
        docs = list(self.db[collection_name].find())
        return [self.serialize(doc) for doc in docs]

service = DataRetrieval()

# ראוט לאנטישמי
@app.get("/antisemitic")
def get_antisemitic():
    return service.get_collection("tweets_antisemitic")

# ראוט ללא אנטישמי
@app.get("/not_antisemitic")
def get_not_antisemitic():
    return service.get_collection("tweets_not_antisemitic")
