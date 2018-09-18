
import threading
class OutputPlugin(object):
  def __init__(self, name):
    self.__name = name
    self._size = 0
    self.__limit_size = 1000
    self._queue = []
    self._queue_mutex = threading.Lock()
    self._enable_query = False
  def Init(self, options):
    pass
  def GetName(self):
    return self.__name
  def Put(self, target, timestamp, keys, values):
    record = self.GenerateRecord(target, timestamp, keys, values)
    with self._queue_mutex:
      if self._size >= self.__limit_size:
        self.LoseRecord()
      self._queue.append(record)
      self._size += 1
  def Pop(self):
    pass
  def LoseRecord(self):
    pass
  def GenerateRecord(self, target, timestamp, keys, values):
    pass
  def Query(self, json_request):
    pass
  def EnableQuery(self):
    return self._enable_query
