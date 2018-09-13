from ghostbot.utils.logger import Logger


class Basis(object):

    def __init__(self):
        self.logger = Logger(__name__)
        self._debugs = []
        self._infos = []
        self._warnings = []
        self._errors = []
        self._criticals = []

    def is_continuable(self):
        return len(self._criticals) == 0

    def has_warnings(self):
        return len(self._warnings) > 0

    def has_errors(self):
        return (len(self._errors) + len(self._criticals)) > 0

    def warnings(self):
        return self._warnings

    def errors(self):
        return self._errors + self._criticals

    def debug(self, template, *args):
        message = template.format(*args)
        self._debugs.append(message)
        self.logger.debug(message)

    def info(self, template, *args):
        message = template.format(*args)
        self._infos.append(message)
        self.logger.info(message)

    def warning(self, template, *args):
        message = template.format(*args)
        self._warnings.append(message)
        self.logger.warning(message)

    def error(self, template, *args):
        message = template.format(*args)
        self._errors.append(message)
        self.logger.error(message)

    def critical(self, template, *args):
        message = template.format(*args)
        self._criticals.append(message)
        self.logger.critical(message)
