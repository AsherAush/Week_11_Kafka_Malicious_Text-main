from cleaner import  Cleaner
from consumer import  Consumer
from producer import KafkaPublisher

class Main:
    def __init__(self):
        self.text_consumer = Consumer()
        self.text_producer = KafkaPublisher()

    def process_messages(self):
        # Subscribe to two topics
        try:
            for message in self.text_consumer.consumer:
                msg = message.value
                topic = message.topic
                original_text = msg.get("text", "")
                cleaned_text = Cleaner(original_text).get_text()

                print("--------------------------------------------------")
                print(f" Topic: {topic}")
                # print(f" Original: {original_text}")
                # print(f" Cleaned: {cleaned_text}")

                yield {
                    'topic': topic,
                    'original_text': original_text,
                    'cleaned_text': cleaned_text,
                    'timestamp': message.timestamp
                }


        except KeyboardInterrupt:
            print("\n close the consumer...")
        except Exception as e:
            print(f"Error processing messages: {e}")
        finally:
            self.text_consumer.consumer.close()



    def pruducer_message(self):
        # עיבוד ושליחה של הודעות
        for processed_message in self.process_messages():
            topic = processed_message['topic']
            original_text = processed_message['original_text']
            cleaned_text = processed_message['cleaned_text']
            timestamp = processed_message['timestamp']

            # שליחת ההודעה המעובדת לטופיק המתאים
            if topic == "raw_tweets_antisemitic":
                self.text_producer.last_publish("preprocessed_tweets_antisemitic", {
                    "original_text": original_text,
                    'cleaned_text': cleaned_text,
                    'timestamp': timestamp
                })
                print(f"Sent cleaned message to topic {topic}")
            elif topic == "raw_tweets_not_antisemitic":
                self.text_producer.last_publish("preprocessed_tweets_not_antisemitic", {
                    "original_text": original_text,
                    'cleaned_text': cleaned_text,
                    'timestamp': timestamp
                })
                print(f"Sent cleaned message to topic {topic}")




if __name__ == "__main__":
    main_processor = Main()
    main_processor.pruducer_message()


