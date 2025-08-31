from kafka import KafkaConsumer
import json

class KafkaSubscriber:
    def __init__(self, topics, bootstrap_servers='localhost:9092', group_id='persister-group'):
        self.consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id)

    def listen(self):
        for message in self.consumer:
            yield message.topic, message.value
