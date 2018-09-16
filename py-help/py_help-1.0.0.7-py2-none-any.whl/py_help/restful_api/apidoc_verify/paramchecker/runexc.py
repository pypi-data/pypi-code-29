# -*- coding: utf-8 -*-

from oslo_log import log as logging
from oslo_utils import encodeutils
from sf_apidesc.i18n import _

LOG = logging.getLogger(__name__)


def _format_with_unicode_kwargs(msg_format, kwargs):
    try:
        return msg_format % kwargs
    except UnicodeDecodeError:
        try:
            kwargs = {k: encodeutils.safe_decode(v)
                      for k, v in kwargs.items()}
        except UnicodeDecodeError:
            # NOTE(jamielennox): This is the complete failure case
            # at least by showing the template we have some idea
            # of where the error is coming from
            return msg_format

        return msg_format % kwargs


class Error(Exception):
    """Base error class.

    Child classes should define an HTTP status code, title, and a
    message_format.

    """
    message_format = None

    def __init__(self, message=None, **kwargs):
        try:
            message = self._build_message(message, **kwargs)
        except KeyError:
            message = self.message_format

        super(Error, self).__init__(message)

    def _build_message(self, message, **kwargs):
        """Build and returns an exception message.

        :raises KeyError: given insufficient kwargs

        """
        if message:
            return message
        return _format_with_unicode_kwargs(self.message_format, kwargs)


class ValidateError(Error):

    def __init__(self, message=None):
        self.code = 400
        super(ValidateError, self).__init__(message)

    @property
    def side(self):
        if self.code == 400:
            return _('Input')
        else:
            return _('Return')


class VisibleExInvalidInput(ValidateError):

    message_format = _(
        'Error: In data: %(input)s, invalid %(field)s: %(expect)s %(error)s')

    def __init__(self, field, value, expect_cls=None, error=''):
        expect = expect_cls.tostring() \
            if expect_cls and hasattr(expect_cls, 'tostring') else ''
        self.dbgmsg = self.message_format % {'field': field,
                                             'input': value,
                                             'expect': expect,
                                             'error': error}
        LOG.error(self.dbgmsg)
        super(VisibleExInvalidInput, self).__init__(
            _(u'%(field)s输入错误：%(error)s')
            % {'field': field, 'error': error})


class VisibleExMissingArgument(ValidateError):

    message_format = _('Error: in %(input)s, missing argument %(name)s')

    def __init__(self, argname, value):
        self.dbgmsg = self.message_format % {'name': argname, 'input': value}
        LOG.error(self.dbgmsg)
        super(VisibleExMissingArgument, self).__init__(
            _(u'缺少参数：%s') % argname)


class VisibleExUnknownArgument(ValidateError):

    message_format = _('Error: Unknown argument: %(name)s')

    def __init__(self, argname):
        self.dbgmsg = self.message_format % {'name': argname}
        LOG.error(self.dbgmsg)
        super(VisibleExUnknownArgument, self).__init__(
            _(u'不接受参数：%s') % argname)


class VisibleExValueError(ValidateError):
    pass


class SchemaFormatError(ValidateError):

    message_format = _('Error: Schema format error')
