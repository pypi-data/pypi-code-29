from pathlib import Path
import re

from tensorflow.keras.models import load_model

from .preproc import code_label, texts_to_matrix


model_path = Path(__file__).parent / 'model.hdf5'
pos_tagging_model = load_model(model_path)

white_space_re = re.compile(r'\s+')


class Worin:
    def _split_text(self, text):
        """
        Split a text up to 100 characters
        :param text:
        :return:
        """
        text = white_space_re.sub(text.strip(), ' ')
        if len(text) <= 100:
            texts = [text]
        else:
            texts = []
            start = 0
            end = 80
            n = len(text)
            while start < n:
                if end >= n or text[end] in ' \r\n\t' or end - start >= 100:
                    texts.append(text[start:end])
                    start = end + 1
                    end = start + 80
                else:
                    end += 1
        return texts

    def _pair_word_label(self, texts, tags):
        words = []
        pos = []

        for text, tag in zip(texts, tags):
            prev_label = None
            for letter, code in zip(text, tag):
                label, trail = code_label[code]

                if letter == ' ':
                    continue

                elif trail == 1 and prev_label == label:
                    words[-1] += letter
                else:
                    words.append(letter)
                    pos.append(label)

                prev_label = label
        return list(zip(words, pos))

    def pos(self, text):
        texts = self._split_text(text)
        mat = texts_to_matrix(texts)
        tags = pos_tagging_model.predict_classes(mat)
        return self._pair_word_label(texts, tags)

    def nouns(self, text):
        return [word for word, pos in self.pos(text) if pos == 'N']
