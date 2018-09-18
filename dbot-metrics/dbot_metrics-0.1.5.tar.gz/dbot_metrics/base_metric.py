class BaseMetric(object):
  def __init__(self):
    pass
  def Init(self, options):
    raise NotImplemented()
  '''
  @return String
  '''
  def GetName(self):
    raise NotImplemented()
  '''
  @para notify: a callback handle, with one parameter: metric records
  '''
  def RegisterNotify(self, notify):
    raise NotImplemented()
  '''
  @para flag: Donot record every time the metric collected if False
  '''
  def EnableDetailRecord(self, flag):
    raise NotImplemented()
  '''
  @return a list of metric records, with format like flowing
          [{'target': 'table_student', 'keys': {"name":"steven", "no": 11223344}, 'values': {"age": 23}}]
  '''
  def FetchInfo(self):
    raise NotImplemented()
  '''
  @return the collecting interval(seconds)
  '''
  def GetCollectInterval(self):
    raise NotImplemented()
