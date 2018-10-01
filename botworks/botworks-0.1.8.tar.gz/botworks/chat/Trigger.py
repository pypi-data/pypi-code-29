import logging
from difflib import SequenceMatcher

from botworks.slack.Payload import Payload

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


class Trigger:
    def __init__(self, match_method=None, match_phrases=None, event=None, full_text=None, full_text_ratio=0.7):
        self.matchMethod = match_method
        self.matchPhrases = match_phrases
        self.event = event
        self.fullText = full_text
        self.fullTextRatio = full_text_ratio

    def check(self, payload: Payload):
        log.debug("Checking " + str(payload.lower_message))
        if self.matchMethod:
            return self.matchMethod.check(payload)
        if self.event == payload.event_type:
            return True
        if self.fullText and payload.imageText and \
                SequenceMatcher(None, self.fullText, payload.imageText).ratio() > self.fullTextRatio:
            return True
        return self.matchPhrases and payload.lower_message and self.matchPhrases.check(payload.lower_message)


class And:
    def __init__(self, *args):
        self.triggers = list(map(lambda x: x.lower() if type(x) == str else x, [*args]))

    def check(self, message) -> bool:
        log.debug("Checking And " + str(len(self.triggers)))
        res = True
        for t in self.triggers:
            if type(t) is str:
                res &= t in message
            else:
                res &= t.check(message)
                if not res:
                    break
        return res


class Or:
    def __init__(self, *args):
        self.triggers = list(map(lambda x: x.lower() if type(x) == str else x, [*args]))

    def check(self, message) -> bool:
        log.debug("Checking Or " + str(len(self.triggers)))
        res = False
        for t in self.triggers:
            if type(t) is str:
                res |= t in message
            else:
                res |= t.check(message)
            if res:
                break
        return res


class Not:
    def __init__(self, *args):
        if len([*args]) != 1:
            log.error("Misconfigured Not, it's going to get weird")
        self.triggers = list(map(lambda x: x.lower() if type(x) == str else x, [*args]))

    def check(self, message) -> bool:
        log.debug("Checking Not " + str(len(self.triggers)))
        if type(self.triggers[0]) is str:
            res = self.triggers[0] not in message
        else:
            res = not self.triggers[0].check(message)

        return res


class StartsWith:
    def __init__(self, *args):
        if len([*args]) != 1:
            log.error("Misconfigured Startswith, it's going to get weird")
        self.triggers = list(map(lambda x: x.lower() if type(x) == str else x, [*args]))

    def check(self, message: str) -> bool:
        log.debug("Checking StartsWith " + str(len(self.triggers)))
        if type(self.triggers[0]) is str:
            return message.startswith(self.triggers[0])

        return False
