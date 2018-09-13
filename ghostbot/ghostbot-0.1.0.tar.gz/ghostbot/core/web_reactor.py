import traceback
import html2text
from bs4 import BeautifulSoup
from pymongo import MongoClient
from ghostbot import StatusCode
from ghostbot.utils.logger import Logger
from .reactor import Reactor


class WebReactor(Reactor):
    PARSER_LXML = "lxml"
    MONGODB_DSN = "mongodb://localhost:27017/"

    def __init__(self, agent=None):
        super().__init__(agent)
        self.logger = Logger(__name__)
        self.mongodb = None
        self.db = None

    def setup(self, database):
        result = False
        try:
            self.mongodb = MongoClient(self.MONGODB_DSN)
            self.db = self.mongodb[database]
            result = True
        except Exception as e:
            self.logger.critical(StatusCode[340], e.args)
            traceback.print_exc()
        return result

    def execute(self):
        pass

    @staticmethod
    def soup(html):
        return BeautifulSoup(html)

    def markdown(self, html):
        content = BeautifulSoup(html, self.PARSER_LXML)
        for tag in ["script", "style", "font", "em"]:
            [s.decompose() for s in content(tag)]
        for attr in ["style", "xmlns"]:
            content = self.remove_attrs(content, attr)
        return html2text.html2text(content)

    @staticmethod
    def remove_attrs(content, target):
        for tag in content.find_all(True):
            for attr in [attr for attr in tag.attrs if attr == target]:
                del tag[attr]
        return content

    @staticmethod
    def analyze(html):
        result = {}
        for tag in html.find_all():
            if tag.name in ["ol", "ul", "li"]:
                items = [item.string for item in tag.find_all("li")]
                if items and len(items) > 0:
                    if "list" not in result:
                        result["list"] = []
                    result["list"].append({"items": items})
            elif tag.name in ["select", "option"]:
                options = [item.string for item in tag.find_all("option")]
                defaults = [item.string for item in tag.find_all("option") if "default" in item.attr]
                default_option = None if len(defaults) == 0 else defaults[0]
                if options and len(options) > 0:
                    if "select" not in result:
                        result["select"] = []
                    result["select"].append({"options": options, "default": default_option})
            elif tag.name in ["form", "input", "button"]:
                if tag.name == "form":
                    if "form" not in result:
                        result["form"] = []
                    result["form"].append({"method": tag["method"], "action": tag["action"]})
                else:
                    if tag.type in ["button", "submit"]:
                        if "button" not in result:
                            result["button"] = []
                        result["button"].append({"name": tag["name"], "value": tag["value"]})
                    else:
                        if "input" not in result:
                            result["input"] = []
                        result["input"].append({"type": tag["type"], "name": tag["name"], "value": tag["value"]})
            elif tag.name == "a":
                if "href" in tag.attrs:
                    if "link" not in result:
                        result["link"] = []
                    result["link"].append({"href": tag["href"], "text": str(tag.text).strip()})
            else:
                if tag.string:
                    text = str(tag.string).strip()
                    if len(text) > 0:
                        if "text" not in result:
                            result["text"] = []
                        result["text"].append(text)
        return result

    def save(self, key, value):
        result = None
        try:
            collection = self.db[key]
            result = collection.insert_one(value).inserted_id
        except Exception as e:
            self.logger.critical(StatusCode[341], e.args)
            traceback.print_exc()
        return result
