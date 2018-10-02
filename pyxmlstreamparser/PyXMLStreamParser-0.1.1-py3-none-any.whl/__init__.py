from xml.sax import make_parser
from xml.sax._exceptions import SAXException

from io import SEEK_END

__version__ = '0.1.1'


class StopParser(SAXException):
    pass


class BaseXMLStream:
    def __init__(self, handler, *args, **kwargs):
        self.stream = None
        self.handler = handler

    def parse(self):
        try:
            parser = make_parser()
            parser.setContentHandler(self.handler)
            parser.parse(self.stream)
        except StopParser:
            pass


class XMLStream(BaseXMLStream):
    def __init__(self, handler, stream, *args, **kwargs):
        super(XMLStream, self).__init__(handler)
        self.stream = stream

    def parse(self):
        try:
            parser = make_parser()
            parser.setContentHandler(self.handler)
            parser.parse(self.stream)
        except StopParser:
            pass


class XMLFileStream(BaseXMLStream):

    def __init__(self, filename, handler, *args, **kwargs):
        super(XMLFileStream, self).__init__(handler)
        self.filename = filename
        self.current_read = 0
        self.current_file_size = None

    def parse(self):
        with open(self.filename) as f:
            self.stream = f
            self.stream.seek(0, SEEK_END)
            self.current_file_size = f.tell()
            self.stream.seek(0)

            super(XMLFileStream, self).parse()
