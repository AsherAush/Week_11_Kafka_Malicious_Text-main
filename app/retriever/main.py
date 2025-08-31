from fetcher import MongoFetcher
from producer import KafkaPublisher
import time

# יצירת מופעים של המחלקות
fetcher = MongoFetcher()
publisher = KafkaPublisher()

def run():
    while True:
        messages = fetcher.fetch_messagas()
        for msg in messages:
            # בודקת אם הערך הוא אנטישמי ואם כן יוצרת טופיק כזה
            if msg.get("Antisemitic") == 1:
                topic = "raw_tweets_antisemitic"
            else:
                topic = "raw_tweets_not_antisemitic"
            # המרת ערך createData לסטרינג
            msg["CreateDate"] = msg["CreateDate"].strftime("%d/%m/%Y %H:%M:%S")

            # מדפיס את ההודעות לשם בדיקה שהכל עובד
            print(f"Message: {msg}")

            # שולח את ההודעות לקאפקה
            publisher.publish(topic, msg)

        # מחכה 60 שניות עד השליחה הבאה
        time.sleep(60)

if __name__ == "__main__":
    run()
