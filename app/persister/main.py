from consumer import KafkaSubscriber
from mongo_writer import MongoWriter

topics_map = {'enriched_preprocessed_tweets_antisemitic': ('tweets_antisemitic', 1),
              'enriched_preprocessed_tweets_not_antisemitic': ('tweets_not_antisemitic', 0)}

if __name__ == '__main__':
    consumer = KafkaSubscriber(list(topics_map.keys()))
    mongo_writer = MongoWriter()

    for topic, message in consumer.listen():
        collection_name, antisemitic_flag = topics_map[topic]
        message["Antisemietic"] = antisemitic_flag
        mongo_writer.insert(collection_name, message)
        print(f"[{topic}] saved to '{collection_name}' with flag={antisemitic_flag}")
