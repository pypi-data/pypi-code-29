import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets
import nltk
from nltk.corpus import stopwords
import pickle




class NLTK:

    def train(self, file_name):

        data = pd.read_csv(file_name, encoding="latin1", )
        data = data[["text", "sentiment"]]
        train, test = train_test_split(data, test_size=0.1)
        # Removing neutral sentiments
        train = train[train.sentiment != "Neutral"]
        train_pos = train[train['sentiment'] == 'Positive']
        train_pos = train_pos['text']
        train_neg = train[train['sentiment'] == 'Negative']
        train_neg = train_neg['text']
        tweets = []
        stopwords_set = set(stopwords.words("english"))

        for index, row in train.iterrows():
            words_filtered = [e.lower() for e in row.text.split() if len(e) >= 3]
            words_cleaned = [word for word in words_filtered
                             if 'http' not in word
                             and not word.startswith('@')
                             and not word.startswith('#')
                             and word != 'RT']
            words_without_stopwords = [word for word in words_cleaned if not word in stopwords_set]
            tweets.append((words_without_stopwords, row.sentiment))



        training_set = nltk.classify.apply_features(self.extract_features,tweets)
        classifier = nltk.NaiveBayesClassifier.train(training_set)

        file = open('classifier.pickle', 'wb')
        pickle.dump(classifier, file)
        file.close()

    def get_words_in_tweets(self,tweets):
        all = []
        for (words) in tweets:
            all.extend(words)
        return all

    def get_word_features(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        features = wordlist.keys()
        return features


    def extract_features(self,document):
    # document_words = re.sub("[^\w]", " ", document).split()
     document_words = set(document)
     features = {}
     w_features = self.get_word_features(self.get_words_in_tweets(document))
     for word in w_features:
        features['contains(%s)' % word] = (word in document_words)
        return features

    def get_sentiment(self, text,filename):
         file = open(filename, 'rb')
         classifier = pickle.load(file)
         file.close()

         res = classifier.classify(self.extract_features(text))
         return res



