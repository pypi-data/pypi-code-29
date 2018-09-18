
import configparser

class Configuration():
  def __init__(self, config_file):
    self.__collector_file = config_file
    self.__config_parser = configparser.ConfigParser()
    self.__config_parser.read(self.__collector_file)

    self.__metric_buffer_limit = 0
    self.__precision = 0
    self.__plugins = {}
    self.__parse_sections()
  def Get(self, section, key):
    return self.__config_parser.get(section, key)
  def GetMetricBufferLimit(self):
    return self.__metric_buffer_limit
  def GetPluginOptions(self):
    return self.__plugins
  def __get_options(self, section):
    options = self.__config_parser.options(section)
    opts = {}
    for opt in options:
      opts[opt] = self.__config_parser.get(section, opt)
    return opts
      
  def __parse_sections(self):
    self.__metric_buffer_limit = self.__config_parser.get('base', 'metric_buffer_limit')
    self.__precision = self.__config_parser.get('base', 'precision')

    sections = self.__config_parser.sections()
    for sec in sections:
      secsplit = sec.split('.', 1)
      if len(secsplit) != 2:
        continue
      sectype = secsplit[0]
      secname = secsplit[1]
      if self.__plugins.get(sectype) is None:
        self.__plugins[sectype] = {secname: self.__get_options(sec)}
      else:
        self.__plugins[sectype][secname] = self.__get_options(sec)
        
