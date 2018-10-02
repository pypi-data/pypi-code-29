from nltk.corpus import stopwords
from nltk.tokenize.regexp import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer

from eqi_utils.data import view


class SOCClassifier:
    def __init__(self):
        df = view.load_to_df('soc_data', user='jinpeng.zhang', remote=True)
        self._stop = set(stopwords.words('english'))
        self._stemmer = SnowballStemmer("english")
        self._soc_titles = set(df['2018 SOC Direct Match Title'])
        self._soc_title_majorgroup_map = \
            df.set_index('2018 SOC Direct Match Title')['major_code'].to_dict()
        self._title_map = {
            x: (self.preprocess(x), self._soc_title_majorgroup_map[x]) for x in
            self._soc_titles}

    def preprocess(self, sentence):
        sentence = sentence.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(sentence)
        filtered_words = [self._stemmer.stem(w) for w in tokens if
                          w not in self._stop]
        return set(filtered_words)

    @staticmethod
    def jaccard(s1, s2):
        return float(len(s1.intersection(s2)) / len(s1.union(s2)))

    @staticmethod
    def argmax_jaccard(job_title, title_map):
        max_score = -1
        argmax = None
        for k, v in title_map.items():
            score = SOCClassifier.jaccard(v[0], job_title)
            if score > max_score:
                argmax = v[1]
                max_score = score
        return argmax

    def classify(self, job_title):
        if job_title is None:
            return -1
        return SOCClassifier.argmax_jaccard(self.preprocess(job_title),
                                            self._title_map)
