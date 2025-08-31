from enricher import Enricher
from consumer import KafkaSubscriber
from producer import KafkaPublisher
import threading

# מילון של טופיקים נכנסים ויוצאים
topics = {'preprocessed_tweets_antisemitic': 'enriched_preprocessed_tweets_antisemitic',
          'preprocessed_tweets_not_antisemitic': 'enriched_preprocessed_tweets_not_antisemitic'}

# מאזין לטופיק, מבצע העשרה, ושולח לטופיק החדש
def process_topic(input_topic, output_topic):
    enricher = Enricher("weapon.txt")
    consumer = KafkaSubscriber([input_topic])
    producer = KafkaPublisher()

    for topic, message in consumer.listen():
        enriched = enricher.enrich(message)
        producer.send(output_topic, enriched)
        print(f"[{input_topic} => {output_topic}] {enriched}")

# הפעלת מאזינים במקביל
if __name__ == "__main__":
    for in_topic, out_topic in topics.items():
        threading.Thread(target=process_topic, args=(in_topic, out_topic), daemon=True).start()