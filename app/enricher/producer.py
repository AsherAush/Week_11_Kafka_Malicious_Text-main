from kafka import KafkaProducer
import json

class KafkaPublisher:
    # יצירת פרודיוסר
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda m: json.dumps(m).encode('utf-8'))

    # פונקצייה שמקבלת טופיק ודיקט ושולחת אותו לקאפקה
    def send(self, topic, message):
        self.producer.send(topic, value = message)
        self.producer.flush()
