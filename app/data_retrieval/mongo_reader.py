from pymongo import MongoClient

class MongoReader:
    def __init__(self, db_name='tweets_db'):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def get_all_documents(self, collection_name):
        documents = list(self.db[collection_name].find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return documents
