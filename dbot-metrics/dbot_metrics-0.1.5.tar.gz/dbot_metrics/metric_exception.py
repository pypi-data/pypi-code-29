
class MetricException(Exception):
  def __init__(self, info):
    super(MetricException, self).__init__()
    self.except_info = info
  def __str__(self):
    return "MetricException:" + self.except_info
