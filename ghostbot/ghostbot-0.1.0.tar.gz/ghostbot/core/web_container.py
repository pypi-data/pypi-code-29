import traceback
from bs4 import BeautifulSoup
from ghostbot import StatusCode
from ghostbot.utils.logger import Logger
from .container import Container


class WebContainer(Container):
    DEFAULT_PARSER = "lxml"

    def __init__(self, agent=None):
        super().__init__(agent)
        self.logger = Logger(__name__)
        self._url = None
        self._active = None
        self._scrap = {}

    def contents(self, key=None, value=None):
        if key and value:
            try:
                self._active = BeautifulSoup(value, self.DEFAULT_PARSER)
                super().contents(key, self._active)
            except Exception as e:
                self.error(StatusCode[520], e.args)
                traceback.print_exc()
        return super().contents()

    # TODO use this method for convert contents from relational url to absolute url
    def url(self, url=None):
        if url:
            self._url = url
        return self._url

    def scrap(self, key=None, value=None):
        if key and value:
            result = self._scrap[key] = value
        elif key and key in self._scrap:
            result = self._scrap[key]
        else:
            result = self._scrap
        return result

    def find(self, *args, **kwargs):
        result = None
        if self._active:
            try:
                result = self._active.find(*args, **kwargs)
            except Exception as e:
                self.error(StatusCode[523], e.args, __file__)
                traceback.print_exc()
        else:
            self.error(StatusCode[521], __name__)
        return result

    def find_all(self, *args, **kwargs):
        result = []
        if self._active:
            try:
                result = self._active.find_all(*args, **kwargs)
            except Exception as e:
                self.error(StatusCode[523], e.args, __file__)
                traceback.print_exc()
        else:
            self.error(StatusCode[521], __name__)
        return result

    def xpath(self, expression):
        result = None
        if self._active:
            if expression and len(expression.strip()) > 0:
                try:
                    expression = self._resolve(expression)
                    result = self._active.xpath(expression)
                except Exception as e:
                    self.error(StatusCode[523], e.args, __file__)
                    traceback.print_exc()
            else:
                self.error(StatusCode[522], expression)
        else:
            self.error(StatusCode[521], __name__)
        return result

    def xpath_all(self, expression):
        result = None
        if self._active:
            if expression and len(expression.strip()) > 0:
                try:
                    expression = self._resolve(expression)
                    result = self._active.xpath(expression)[0]
                except Exception as e:
                    self.error(StatusCode[523], e.args, __file__)
                    traceback.print_exc()
            else:
                self.error(StatusCode[522], expression)
        else:
            self.error(StatusCode[521], __name__)
        return result

    def select(self, expression):
        result = None
        if self._active:
            if expression and len(expression.strip()) > 0:
                try:
                    expression = self._resolve(expression)
                    result = self._active.select(expression)[0]
                except Exception as e:
                    self.error(StatusCode[523], e.args, __file__)
                    traceback.print_exc()
            else:
                self.error(StatusCode[522], expression)
        else:
            self.error(StatusCode[521], __name__)
        return result

    def select_all(self, expression):
        result = None
        if self._active:
            if expression and len(expression.strip()) > 0:
                try:
                    expression = self._resolve(expression)
                    result = self._active.select(expression)
                except Exception as e:
                    self.error(StatusCode[523], e.args, __file__)
                    traceback.print_exc()
            else:
                self.error(StatusCode[522], expression)
        else:
            self.error(StatusCode[521], __name__)
        return result

    def unwrap(self, element):
        result = element
        if self._active:
            try:
                result = element.unwrap()
            except Exception as e:
                self.error(StatusCode[523], e.args, __file__)
                traceback.print_exc()
        else:
            self.error(StatusCode[521], __name__)
        return result

    def _resolve(self, expression):
        result = expression
        agent = self.agent()
        if expression[:1] == agent.SYMBOL_RESOURCES:
            result = agent.resources_forms(expression)
        return result
