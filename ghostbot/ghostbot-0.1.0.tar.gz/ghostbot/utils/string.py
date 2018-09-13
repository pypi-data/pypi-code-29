import re


class String(object):

    @classmethod
    def subtract(cls, text, substring):
        return text.replace(substring, "")

    @classmethod
    def upper(cls, text):
        return text.upper()

    @classmethod
    def lower(cls, text):
        return text.lower()

    @classmethod
    def pascal(cls, text):
        return cls.camel(text, upper=True)

    @classmethod
    def camel(cls, text, upper=False):
        result = re.sub("_(.)", lambda x: x.group(1).upper(), text)
        if upper:
            result = result[:1].upper() + result[1:]
        return result

    @classmethod
    def snake(cls, text):
        return re.sub("([A-Z])", lambda x: "_" + x.group(1).lower(), text)
