
import datetime
import logging
import threading
import json
import os
from .timer import Timer
from .configuation import Configuration
from .metric_exception import MetricException

class SingleInstance(object):
  _instance = None
  def __new__(cls, *args, **kw):
    if not cls._instance:
      cls._instance = super(SingleInstance, cls).__new__(cls, *args, **kw)  
    return cls._instance 

class DBotMetricsCollector(SingleInstance):
  _is_inited = False
  def __init__(self):
    if self._is_inited:
      return
    self._is_inited = True
    self.__mutex_metrics = threading.Lock()
    self.__metrics = {}
    self.__mutex_output = threading.Lock()
    self.__output_plugins = {}
    self.__unit_time = 1
    self.__timer = Timer(self.__unit_time, self.__on_timer)
    self.__config_file = None
    self.__config = None
  def Start(self, config=None):
    if config:
      self.__config_file = config
    else:
      self.__config_file = '/etc/collector.conf'

    if not os.path.isfile(self.__config_file):
      raise MetricException("Please set config file collector.conf or copy it to default path /etc")

    self.__config = Configuration(config)
    logging.info("Metric dispatcher start, config %s", self.__config_file)
    self.__load_plugins()
    self.__timer.start()
  def Stop(self):
    logging.info("Metric dispatcher stop")
    self.__timer.stoptimer()

  def __load_plugins(self):
    plugins = self.__config.GetPluginOptions()
    for plugin_type, plugin_options in plugins.items():
      for name, options in plugin_options.items():
        enable = options.get('enable')
        if enable == 'True':
          try:
            pluginfile = options.get('file')
            plugin_module = options.get('module')
            plugin = __import__("dbot_metrics." + plugin_type + "." + pluginfile, fromlist=[plugin_module])
            objclass = getattr(plugin, plugin_module)
            o = objclass()
            o.Init(options)
            self.__register_plugin(plugin_type, o)
          except:
            logging.exception("import plugin failed")

  def __on_timer(self):
    with self.__mutex_metrics:
      for _, m in self.__metrics.items():
        m.time_counter += 1
        if m.time_counter >= m.GetCollectInterval():
          infos = m.FetchInfo()
          if len(infos) == 0:
            m.time_counter = 0
            continue
          lastinfo = infos.pop()
          for info in infos:
            self.__process_metric(info, False)
          self.__process_metric(lastinfo, True)
          m.time_counter = 0

  def __process_metric(self, data, push_immediate):
    timestamp = float(datetime.datetime.utcnow().strftime("%s.%f"))
    with self.__mutex_output:
      for _, output in self.__output_plugins.items():
        output.Put(data['target'], timestamp, data['keys'], data['values'])
        if push_immediate:
          output.Push()

  def __register_plugin(self, plugin_type, plugin_obj):
    if plugin_type == "output":
      self.__register_output_plugin(plugin_obj)
    elif plugin_type == "input":
      raise MetricException("Not support input plugins")
      #self.RegisterMetric(plugin_obj)

  def RegisterMetric(self, metric):
    logging.info("Metric register metric plugin %s", metric.GetName())
    with self.__mutex_metrics:
      self.__metrics[metric.GetName()] = metric
    metric.RegisterNotify(self.__process_metric)

  def GetMetric(self, name):
    with self.__mutex_metrics:
      return self.__metrics.get(name)

  def __register_output_plugin(self, output):
    logging.info("Metric register output plugin %s", output.GetName())
    with self.__mutex_output:
      self.__output_plugins[output.GetName()] = output

  def __unregister_output_plugin(self, name):
    logging.info("Metric unregister output plugin %s", name)
    with self.__mutex_output:
      del self.__output_plugins[name]

  def Query(self, request):
    result = []
    with self.__mutex_output:
      for name, output in self.__output_plugins.items():
        if output.EnableQuery():
          result.extend([{'name':name, 'content':output.Query(request)}])
    return result

