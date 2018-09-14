from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


__all__ = ["calculate_sentiment"]


class SentimentResult:

    def __init__(self, dict_result):
        compound = dict_result["compound"]
        self.positive = compound >= 0.05
        self.neutral = -0.05 < compound < 0.05
        self.negative = compound <= -0.05


def calculate_sentiment(text):
    return SentimentResult(analyzer.polarity_scores(text))
