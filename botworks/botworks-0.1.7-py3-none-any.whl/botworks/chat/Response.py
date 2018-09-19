import random


class IResponse:
    def respond(self, client, payload): pass


class Response(IResponse):
    def __init__(self, text=None, emoji=None, ephemeral=None, threaded=None, method=None):
        self.__text = self.__to_list(text)
        self.__emoji = self.__to_list(emoji)
        self.__ghostly = self.__to_list(ephemeral)
        self.__threaded_response = self.__to_list(threaded)
        self.__method = method

    def respond(self, client, payload):
        if self.__method:
            self.__method(client=client, payload=payload)
        if self.__text:
            for t in self.__text:
                client.post_message(channel=payload.channel, message=t)
        if self.__emoji:
            for e in self.__emoji:
                client.react(payload=payload, reaction=e)
        if self.__ghostly:
            for e in self.__ghostly:
                client.ephemeral_message(payload=payload, message=e)
        if self.__threaded_response:
            for m in self.__threaded_response:
                client.thread_reply(payload=payload, message=m)

    @staticmethod
    def __to_list(o):
        if not o:
            return None
        if type(o) is list:
            return o
        return [o]


class Responses(IResponse):
    def __init__(self, responses):
        self.responses = responses

    def respond(self, client, payload):
        if type(self.responses) is list:
            random.choice(self.responses).respond(client, payload)
        else:
            self.responses.respond(client, payload)


