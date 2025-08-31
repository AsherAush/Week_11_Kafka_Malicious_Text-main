from kafka import KafkaProducer
import json
import os
from dotenv import load_dotenv

load_dotenv()

class KafkaPublisher:
    def __init__(self):
        # כתובת הקאפקה
        self.bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        # יצירת פרודיוסר
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"))
        
    # פונקצייה ששולחת הודעות לטופיק מסויים
    def publish(self, topic, message):
        self.producer.send(topic, message)
        self.producer.flush()
