import unittest
from ybc_speech import *


class MyTestCase(unittest.TestCase):
    def test_voice2text(self):
        self.assertEqual('原辅导你好', voice2text('test.wav'))

    def test_text2voice(self):
        filename = text2voice('欢迎参加编程课', 'temp.wav')
        self.assertEqual('欢迎参加编程课', voice2text(filename))


if __name__ == '__main__':
    unittest.main()
