from .SentimentModels.NLTK import  NLTK
class SentimentAnalysis:

    def analysis(self, text,type,classifier_path):
        if type=='NLTK':
            nltk=NLTK()
            return nltk.get_sentiment(text,classifier_path)
    def train(self, csv_file_name, type):
        if type == 'NLTK':
            nltk = NLTK()
            nltk.train(csv_file_name)
