import string
def isAppendingDigitsOrPunctuation(text):
    if text is None or not text:
        return False
    print('appending {}'.format(text))
    if text[-1].isdigit() or (text[-1] in string.punctuation):
        print("failed append")
        return True
    return False

if isAppendingDigitsOrPunctuation('.'):
    print("found one")
