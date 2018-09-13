from abc import abstractmethod
from ghostbot import Ghostbot, StatusCode
from ghostbot.utils.logger import Logger
from ghostbot.utils.string import String
from .basis import Basis
from .asserter import Asserter


class Agent(Basis, Asserter):

    def __init__(self, scenario=None, container=None, reactor=None):
        super().__init__()
        self._scenario = scenario
        self._container = container
        self._reactor = reactor
        self._job_id = None
        self._options = None
        self._api_calls = []
        self.logger = Logger(__name__)

    def name(self):
        return String.snake(String.subtract(self.__class__.__qualname__, "Agent"))[1:]

    def job_id(self, job_id=None):
        if job_id:
            self._job_id = job_id
        return self._job_id

    def scenario(self, scenario=None):
        if scenario:
            self._scenario = scenario
        return self._scenario

    def container(self, container=None):
        if container:
            self._container = container
        return self._container

    def reactor(self, reactor=None):
        if reactor:
            self._reactor = reactor
        return self._reactor

    def options(self, options=None):
        if options:
            self._options = options
        return self._options

    def api_calls(self, api_call=None):
        if api_call:
            self._api_calls.append(api_call)
        return self._api_calls

    def event_loop(self):
        # FIXME collaboration outer world of self scope
        uri = "/"
        while uri is not None:
            handler, is_generator = self._handler(uri)
            if handler is not None:
                uri = self._dispatch(uri, handler, is_generator)
            else:
                uri = None
                self.error(StatusCode[541], self.__class__.__name__, uri)

    def _dispatch(self, uri, handler, is_generator):
        result = None
        self.info(StatusCode[150], self.__class__.__name__, uri)
        if is_generator:
            for uri in handler():
                handler, is_generator = self._handler(uri)
                result = self._dispatch(uri, handler, is_generator)
        else:
            result = handler()
        return result

    def _handler(self, uri):
        # FIXME judge generator or method without action decorator's argument
        result = None
        method, is_generator = Ghostbot.actions(uri, self.__class__.__name__)
        if method is not None and hasattr(self, method):
            result = getattr(self, method)
        else:
            self.error(StatusCode[540], self.__class__.__name__, method)
        return result, is_generator

    @abstractmethod
    def startup(self, config=None):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def execute(self, options=None):
        pass
