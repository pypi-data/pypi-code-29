from django.utils.text import Truncator


def truncate_html_words(value, length):
    return Truncator(value).words(length, html=True)


def truncate_words(value, length):
    return Truncator(value).words(length)
