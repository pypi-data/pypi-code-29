from unittest import TestCase
from functools import wraps
from sections import *


class TestReport(TestCase):
    MD_DIR = None
    PDF_DIR = None
    TEX_DIR = None
    CSV_DIR = None
    HTML_DIR = None

    def __init__(self, *args, **kwargs):
        self.__report_info__ = None
        self.__test_case__ = None
        methods = filter(lambda x: x.find("test") == 0, dir(self))
        for method_name in methods:
            method = getattr(self, method_name)

            def wrapper(f):
                @wraps(f)
                def wrapped(*args, **kwargs):
                    self.__report_info__ = []
                    self.__test_case__ = f.__name__
                    ret = f(*args, **kwargs)
                    if TITLE not in [x[0] for x in self.__report_info__]:
                        self.__report_info__.append((TITLE, f.__name__))
                    return ret
                return wrapped
            setattr(self, method_name, wrapper(method))

        tearDown = getattr(self, "tearDown")

        def tearDown_wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                ret = f(*args, **kwargs)
                self.generate_report()
                self.__report_info__ = None
                self.__test_case__ = None
                return ret
            return wrapped
        setattr(self, "tearDown", tearDown_wrapper(tearDown))
        super(TestReport, self).__init__(*args, **kwargs)

    def generate_report(self):
        from report import  report2Csv, report2Md, report2HTML, report2tex, report2PDF
        print "Report for " + str(self.__test_case__)
        if self.MD_DIR:
            report2Md(self.__report_info__, self.MD_DIR, testsuite=self.__class__.__name__)
        if self.HTML_DIR:
            report2HTML(self.__report_info__, self.HTML_DIR, testsuite=self.__class__.__name__)
        if self.TEX_DIR:
            report2tex(self.__report_info__, self.TEX_DIR, testsuite=self.__class__.__name__)
        if self.PDF_DIR:
            report2PDF(self.__report_info__, self.PDF_DIR, testsuite=self.__class__.__name__)

        if self.CSV_DIR:
            report2Csv(self.__report_info__, self.CSV_DIR)

    def title(self, title):
        self.__report_info__.append((TITLE, title))

    def explanation(self, text):
        self.__report_info__.append((EXPLANATION, text))

    def tip(self, text):
        self.__report_info__.append((TIP, text))

    def code(self, text):
        self.__report_info__.append((CODE, text))


class TestTest(TestReport):
    CSV_DIR = "."
    MD_DIR = True
    HTML_DIR = True
    TEX_DIR = True
    PDF_DIR = True

    def testCase(self):
        self.title("umd")
        self.explanation("what ever")
        self.tip("tip")
        self.code("code")

    def testCase2(self):
        self.explanation("what ever 2")
        self.tip("tip 2")
        self.code("code 2")

    def tearDown(self):
        print "########### TEARDOWN"


if __name__ == '__main__':
    import unittest
    unittest.main()
