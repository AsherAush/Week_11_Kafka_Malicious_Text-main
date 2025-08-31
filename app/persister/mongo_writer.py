from pymongo import MongoClient
from datetime import datetime

class MongoWriter:
    # יצירת חיבור למונגו דיבי
    def __init__(self, db_name='tweets_db'):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    # הוספת שדות לקולקשן
    def insert(self, collection_name, doc):
        # הוספת שדה זמן יצירה
        doc['createdate'] = datetime.utcnow().isoformat()

        # שמירה של כלי הנשק הראשון, אם אין - מחרוזת ריקה
        weapons = doc.get("weapons_detected", [])
        doc["weapons_detected"] = weapons[0] if weapons else ""
        self.db[collection_name].insert_one(doc)
