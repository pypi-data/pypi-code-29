from os.path import join, dirname
from languageflow.reader.dictionary_loader import DictionaryLoader

words = DictionaryLoader(join(dirname(__file__), "Viet74K.txt")).words
lower_words = set([word.lower() for word in words])


def text_lower(word):
    return word.lower()


def text_isdigit(word):
    return word.isdigit()


def text_isallcap(word):
    for letter in word:
        if not letter.istitle():
            return False
    return True


def text_istitle(word):
    if len(word) == 0:
        return False
    try:
        titles = [s[0] for s in word.split(" ")]
        for token in titles:
            if token[0].istitle() is False:
                return False
        return True
    except:
        return False


def text_is_in_dict(word):
    return str(word.lower() in lower_words)


functions = {
    "lower": text_lower,
    "istitle": text_istitle,
    "isallcap": text_isallcap,
    "isdigit": text_isdigit,
    "is_in_dict": text_is_in_dict
}


def template2features(sent, i, template, debug=True):
    """
    :type token: object
    """
    # columns = []
    # for j in range(len(sent[0])):
    #     columns.append([t[j] for t in sent])
    index1, index2, column, func, token_syntax = template
    if debug:
        prefix = "%s=" % token_syntax
    else:
        prefix = ""
    if i + index1 < 0:
        return "%sBOS" % prefix
    if i + index1 >= len(sent):
        return "%sEOS" % prefix
    if index2 is not None:
        if i + index2 >= len(sent):
            return "%sEOS" % prefix
        tmp = [sent[j][column] for j in range(i + index1, i + index2 + 1)]
        word = " ".join(tmp)
    else:
        word = sent[i + index1][column]
    if func is not None:
        result = functions[func](word)
    else:
        result = word
    return "%s%s" % (prefix, result)
