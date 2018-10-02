import logging
import pytest
from qa_cli_tools.dfm import DateFormatMachine
import pendulum

log = logging.getLogger()


class TestDFM:

    def test_unix_timestamp(self):
        log.debug("test_unix_timestamp")

    def test_milestone_timestamps(self):
        log.debug("test_milestone_timestamps")
        # http://www.silisoftware.com/tools/date.php
        print("figuring timestamps")
        print("compared to : 2017, 2, 2, 15, 0, 0")

        anchor = pendulum.datetime(2017, 2, 2, 15, 0, 0)
        unix_start = pendulum.datetime(1970, 1, 1, 0, 0, 0)
        apple_start = pendulum.datetime(1904, 1, 1, 0, 0, 0)
        msoft_start = pendulum.datetime(1899, 12, 30, 0, 0, 0)
        file_start = pendulum.datetime(1601, 1, 1, 0, 0, 0)

        udelta = anchor - unix_start
        unix_timestamp = udelta.total_seconds()
        print(" unix timestamp : %d" % unix_timestamp)
        assert unix_timestamp == 1486047600

        adelta = anchor - apple_start
        apple_timestamp = adelta.total_seconds()
        print("apple timestamp : %d" % apple_timestamp)
        assert apple_timestamp == 3568892400

        mdelta = anchor - msoft_start
        msoft_timestamp = mdelta.total_days()
        print("msoft timestamp : %f" % msoft_timestamp)
        assert msoft_timestamp == 42768.625000

        fdelta = anchor - file_start
        # filetime_stamp = (fdelta.total_seconds() * 1000000000) / 100
        filetime_stamp = (fdelta.total_seconds() * 10000000)
        print(" filetime stamp : %d" % filetime_stamp)
        assert filetime_stamp == 131305212000000000

        apple_diff_unix = unix_start - apple_start
        print("apple diff : %d" % apple_diff_unix.total_seconds())

        msoft_diff_unix = unix_start - msoft_start
        print("msoft diff days : %f" % msoft_diff_unix.total_days())
        print("msoft diff seconds : %f" % msoft_diff_unix.total_seconds())
        file_diff = unix_start - file_start
        print(" file diff : %d" % file_diff.total_seconds())
        file_diff_unix = (131305212000000000 / 10000000) - 11644473600

        print(" file diff unix : %d" % file_diff_unix)

    def test_unix_timestamp_parse(self):

        unix = 1486047600
        dfm = DateFormatMachine(unix, 'unix')

        pdt = dfm.parse()
        print(pdt)

        anchor = pendulum.datetime(2017, 2, 2, 15, 0, 0)

        assert pdt == anchor

    def test_apple_timestamp_parse(self):

        apple = 3568892400
        dfm = DateFormatMachine(apple, 'apple')

        pdt = dfm.parse()
        print(pdt)

        anchor = pendulum.datetime(2017, 2, 2, 15, 0, 0)

        assert pdt == anchor

    def test_microsoft_parse(self):
        # https://msdn.microsoft.com/en-us/library/office/ff197413.aspx

        microsoft = 42768.852777778
        dfm = DateFormatMachine(microsoft, 'microsoft')

        pdt = dfm.parse()
        print(pdt)

        anchor = pendulum.datetime(2017, 2, 2, 20, 28, 0)

        assert pdt == anchor

        d2 = DateFormatMachine(42768.852777778, 'microsoft').parse()
        print("d2 : %s" % d2)
        assert d2 == anchor

        m3 = 1.0
        d3_actual = pendulum.parse('1899-12-31T00:00:00+00:00')
        d3_test = DateFormatMachine(1.0, 'microsoft').parse()
        print("d3 : %s" % d3_test)
        assert d3_test == d3_actual

        assert m3 == DateFormatMachine.to_microsoft(d3_actual)

        d4_actual = pendulum.parse('1900-01-01T12:00:00+00:00')
        d4_test = DateFormatMachine(2.5, 'microsoft').parse()
        print("d4 : %s" % d4_test)
        assert d4_test == d4_actual

        d5_actual = pendulum.parse('1992-11-06T03:00:00+00:00')
        d5_test = DateFormatMachine(33914.125, 'microsoft').parse()
        print("d5 : %s" % d5_test)
        assert d5_test == d5_actual

    def test_to_unix(self):
        d1 = DateFormatMachine('2017-02-02T20:28:25+00:00').parse()
        print(d1)
        d1_unix = DateFormatMachine.to_unix(d1)
        print(d1_unix)
        assert d1_unix == 1486067305

    def test_to_apple(self):
        d1 = DateFormatMachine('2017-02-02T20:28:25+00:00').parse()
        print(d1)
        d1_apple = DateFormatMachine.to_apple(d1)
        print(d1_apple)
        assert d1_apple == 3568912105

    def test_to_microsoft(self):

        # Thursday, February 2, 2017 8:28:25pm
        dfm = DateFormatMachine(1486067305, 'unix', 'microsoft')
        d1 = dfm.parse()
        print(d1)
        m_result = DateFormatMachine.to_microsoft(d1)
        print("result : %s" % m_result)

        dfm2 = DateFormatMachine(m_result, 'microsoft', 'cookie')
        d2 = dfm2.parse()
        print(dfm2.report(d2))

        assert d1 == d2
