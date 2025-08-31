from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv


load_dotenv()

class Consumer:
    def __init__(self):
        self.bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        self.consumer = KafkaConsumer(
            "raw_tweets_antisemitic",
            "raw_tweets_not_antisemitic",
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='text-cleaner-group')

    def send_cleaner_message(self,):
        self.process_messages()


if __name__ == "__main__":
    consumer = Consumer()
    consumer.process_messages()
