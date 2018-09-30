import sys
import json
import logging
from datetime import datetime, timezone, timedelta
from http import HTTPStatus

import cherrypy
import schedule
from cherrypy.process.plugins import Monitor

from .model import createRecord, groupTimeseries
from .storage import StorageQueryError


__all__ = 'RecordApi', 'authenticate'

logger = logging.getLogger(__name__)


def jsonifyTool(fn):
  '''Wrapper around built-in tool to pass ``default = str`` to encoder.'''

  def json_encode(value):
    for chunk in json.JSONEncoder(default = str).iterencode(value):
      yield chunk.encode()

  def json_handler(*args, **kwargs):
    value = cherrypy.serving.request._json_inner_handler(*args, **kwargs)  # @UndefinedVariable
    return json_encode(value)

  return cherrypy.tools.json_out(handler = json_handler)(fn) #@UndefinedVariable

cherrypy.tools.jsonify = jsonifyTool


class RecordApi:

  exposed = True


  def _getDt(self, s):
    if not s:
      return None

    try:
      return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo = timezone.utc)
    except ValueError:
      return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo = timezone.utc)

  def _getFilters(self, **kwargs):
    return {
      'date'  : (self._getDt(kwargs.get('after')), self._getDt(kwargs.get('before'))),
      'level' : kwargs.get('level'),
      'name'  : kwargs.get('name'),
      'query' : kwargs.get('query')
    }

  def HEAD(self, **kwargs):
    filters = self._getFilters(**kwargs)
    group   = kwargs.get('group')
    tz      = kwargs.get('timezone')
    if group and timezone:
      m15grp = cherrypy.request.app.storage.count(filters, True)
      result = groupTimeseries(m15grp, group, tz)
      pair   = list(map(','.join, zip(*((str(int(v[0].timestamp())), str(v[1])) for v in result))))

      headers = cherrypy.response.headers
      headers['X-Record-Group'], headers['X-Record-Count'] = pair if pair else ('', '')
    else:
      cherrypy.response.headers['X-Record-Count'] = cherrypy.request.app.storage.count(filters)

    cherrypy.response.headers['Cache-Control'] = 'no-cache'

  @cherrypy.tools.jsonify
  def GET(self, _id = None, **kwargs):
    storage = cherrypy.request.app.storage
    if _id:
      record = storage.get(_id)
      if not record:
        raise cherrypy.HTTPError(404)

      cherrypy.response.headers['Cache-Control'] = 'max-age=2600000'
      return record
    else:
      filters = self._getFilters(**kwargs)
      range = storage.range(int(kwargs['left']), int(kwargs['right']), filters)
      cherrypy.response.headers['Cache-Control'] = 'no-cache'
      return range

  @cherrypy.tools.jsonify
  def POST(self, **kwargs):
    id = cherrypy.request.app.storage.record(*createRecord(**kwargs))
    cherrypy.response.status = HTTPStatus.CREATED.value  # @UndefinedVariable
    return id

  def _handleUnexpectedError():  # @NoSelf
    extype, exobj, _ = sys.exc_info()

    status = 500
    if isinstance(exobj, StorageQueryError):
      status = 400

    if cherrypy.request.method == 'HEAD':
      cherrypy.response.headers['X-Error-Type']    = extype.__name__
      cherrypy.response.headers['X-Error-Message'] = str(exobj)
    else:
      cherrypy.response.body = json.dumps({'error': {
        'type'    : extype.__name__,
        'message' : str(exobj)
      }}).encode()

    cherrypy.response.status = status

  def _handleExpectedError(status, message, traceback, version):  # @NoSelf
    extype, _, _ = sys.exc_info()
    return json.dumps({'error': {
      'type'    : extype.__name__,
      'message' : message
    }}).encode()

  _cp_config = {
    'request.error_response': _handleUnexpectedError,
    'error_page.default'    : _handleExpectedError
  }


class RecordPurgePlugin(Monitor):

  _schedule = None
  _older = None


  def __init__(self, bus):
    self._schedule = schedule.Scheduler()
    self._schedule.every().day.at('00:00').do(self._purge)

    # Zero frequency means no timing thread will be created
    frequency = 0
    retainDays = cherrypy.config['retention']['days']
    if retainDays:
      frequency = 300
      self._older = timedelta(days = float(retainDays))

    super().__init__(bus, self._schedule.run_pending, frequency = frequency)

  def _purge(self):
    count = self.storage.purge(self._older)
    logger.info('Purged records: %s', count)


def authenticate(realm, username, password):
  '''Basic Auth handler'''

  credentials = cherrypy.config['auth']
  return username == credentials['username'] and password == credentials['password']

