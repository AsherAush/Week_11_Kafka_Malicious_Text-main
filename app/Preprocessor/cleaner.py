import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()

# Define the cleaner class
class Cleaner:
    def __init__(self, text):
        self.text = text


    def Punctuation_shpichel_cleaning(self, text):
        # Implement text cleaning logic here
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text

    def Cleaning_unnecessary_characters(self, text):
        # Remove unnecessary_characters
        text_clean = re.sub(r'\s+', ' ', text)
        text_clean = text_clean.strip()
        return text_clean

    def stop_words(self, text):
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = text.split()
        tokens_clean = [word for word in tokens if word not in stop_words]
        return ' '.join(tokens_clean)

    def lower_case(self, text):
        # Convert to lower case
        return text.lower()

    def lemmatization(self, text):
        # Lemmatization
        tokens = text.split()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(lemmatized_tokens)

    def get_text(self, ):

        text = self.Punctuation_shpichel_cleaning(self.text)
        text = self.Cleaning_unnecessary_characters(text)
        text = self.lower_case(text)
        text = self.stop_words(text)
        text = self.lemmatization(text)
        return text

