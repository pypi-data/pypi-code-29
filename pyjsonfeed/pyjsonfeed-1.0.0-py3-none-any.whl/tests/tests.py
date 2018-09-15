import os
from pyjsonfeed import pyjsonfeed
import unittest
import json

files_with_prefix = []
files = []
feeds = []
os.chdir(os.path.dirname(__file__))
for feed in sorted(os.listdir("feeds")):
    if feed.endswith(".json") and "output" not in feed:
        files.append(feed)
        files_with_prefix.append("feeds/" + feed)

        with open("feeds/" + feed) as f:
            feeds.append(json.load(f))


class TestParseMethod(unittest.TestCase):
    def test_url(self):
        url_prefix = "https://gist.githubusercontent.com/noaoh/4c7f40153ec58f462e437f90b5b49f25/raw/2d0814f2f84a7c005bc0589f48692b7b25ecedf8/"
        urls = sorted([url_prefix + x for x in files])
        for actual, expected in zip(urls, feeds):
            with self.subTest():
                self.assertEqual(pyjsonfeed.parse(actual)._asdict(), expected)


    def test_file(self):
        for actual, expected in zip(files_with_prefix, feeds):
            with self.subTest():
                self.assertEqual(pyjsonfeed.parse(actual)._asdict(), expected)


    def test_string(self):
        strings = []
        for x in files_with_prefix:
            with open(x, encoding="utf8") as f:
                strings.append(f.read())

        for actual, expected in zip(strings, feeds):
            with self.subTest():
                self.assertEqual(pyjsonfeed.parse(actual)._asdict(), expected)


if __name__ == "__main__":
    unittest.main()

