from ghostbot.utils.logger import Logger


class Asserter(object):
    MESSAGE_NONE = "Assertion Failed: expected none, but actually '{}'"
    MESSAGE_NOT_NONE = "Assertion Failed: expected not none, but actually '{}'"
    MESSAGE_TRUE = "Assertion Failed: expected True, but actually '{}'"
    MESSAGE_FALSE = "Assertion Failed: expected False, but actually '{}'"
    MESSAGE_EMPTY = "Assertion Failed: expected empty, but actually '{}'"
    MESSAGE_NOT_EMPTY = "Assertion Failed: expected not empty but actually '{}'"
    MESSAGE_EQUAL = "Assertion Failed: expected '{}' equal '{}'"
    MESSAGE_NOT_EQUAL = "Assertion Failed: expected '{}' not equal '{}'"
    MESSAGE_IN = "Assertion Failed: expected '{}' in '{}'"
    MESSAGE_NOT_IN = "Assertion Failed: expected '{}' not in '{}'"

    def __init__(self):
        self.logger = Logger(__name__)
        self._asserts = []

    def is_success(self):
        return len(self._asserts) == 0

    def asserts(self):
        return self._asserts

    def clear(self):
        self._asserts.clear()

    def _register(self, message):
        self.logger.warning(message)
        self._asserts.append(message)

    def assert_none(self, actual, message=None):
        if actual is not None:
            self._register(message if message else self.MESSAGE_NONE.format(actual))

    def assert_not_none(self, actual, message=None):
        if actual is None:
            self._register(message if message else self.MESSAGE_NOT_NONE.format(actual))

    def assert_true(self, expression, message=None):
        if expression:
            self._register(message if message else self.MESSAGE_TRUE.format(expression))

    def assert_false(self, expression, message=None):
        if not expression:
            self._register(message if message else self.MESSAGE_FALSE.format(expression))

    def assert_empty(self, actual, message=None):
        if len(actual) == 0:
            self._register(message if message else self.MESSAGE_EMPTY.format(actual))

    def assert_not_empty(self, actual, message=None):
        if len(actual) != 0:
            self._register(message if message else self.MESSAGE_NOT_EMPTY.format(actual))

    def assert_equal(self, expected, actual, message=None):
        if expected != actual:
            self._register(message if message else self.MESSAGE_EQUAL.format(expected, actual))

    def assert_not_equal(self, expected, actual, message=None):
        if expected == actual:
            self._register(message if message else self.MESSAGE_NOT_EQUAL.format(expected, actual))

    def assert_in(self, expected, candidates, message=None):
        if expected not in candidates:
            self._register(message if message else self.MESSAGE_IN.format(expected, candidates))

    def assert_not_in(self, expected, candidates, message=None):
        if expected in candidates:
            self._register(message if message else self.MESSAGE_NOT_IN.format(expected, candidates))
