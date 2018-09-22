from abc import ABCMeta, abstractmethod


class SDKException(Exception, metaclass=ABCMeta):
    pass


class SDKResponseException(SDKException, metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_message(response):
        raise NotImplemented

    def __init__(self, response):
        super().__init__(self.__class__.get_message(response))


class ParallelizerException(SDKException):
    def __init__(self, summary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.summary = summary


class SequentializerException(SDKException):
    def __init__(self, summary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.summary = summary
