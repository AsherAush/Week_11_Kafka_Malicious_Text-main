import re
from datetime import datetime
from sentiment_model import get_sentiment

class Enricher:
    # מקבלת את קובץ הנשקים ופותחת אותו בגייסון באותיות קטנות
    def __init__(self, weapons_path):
        with open(weapons_path, encoding='utf-8') as f:
            self.weapons = [line.strip().lower() for line in f if line.strip()]

    # חיפוש נשקים בטקסט והחזרת רשימה שלהם
    def get_weapons(self, text):
        return [w for w in self.weapons if w in text.lower()]

    # חיפוש תאריכים בטקסט, כשמוצא - ממיר לדאטהטיים ומחזיר את הכי מאוחר
    def latest_time(self, text):
        pattern = r'(\d{2}/\d{2}/\d{4} \d{2}:\d{2}|\d{4}-\d{2}-\d{2} \d{2}:\d{2})'
        matches = re.findall(pattern, text)
        times = []
        for m in matches:
            try:
                if "/" in m:
                    times.append(datetime.strptime(m, "%d/%m/%Y %H:%M"))
                else:
                    times.append(datetime.strptime(m, "%Y-%m-%d %H:%M"))
            except:
                continue
        return max(times).isoformat() if times else None

    # עיבוד הטקסט - הוספת שדות של רגש, רשימת נשק, הזמן העדכני שבטקסט
    def enrich(self, doc):
        copy_doc = doc.copy()
        original = copy_doc.get("original_text", copy_doc.get("text", ""))
        clean = copy_doc.get("clean_text", original.lower())

        copy_doc["sentiment"] = get_sentiment(clean)
        copy_doc["weapons_detected"] = self.get_weapons(clean)
        copy_doc["relevant_timestamp"] = self.latest_time(original)
        return copy_doc
