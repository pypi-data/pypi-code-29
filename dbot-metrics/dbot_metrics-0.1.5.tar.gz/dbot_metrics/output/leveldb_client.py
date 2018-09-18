
from collections import MutableMapping
import leveldb
import json
from .output_plugin import OutputPlugin
import threading
import logging
import datetime
import os
from datetime import timedelta

class LevelDBDict(MutableMapping):
  def __init__(self, db_file):
    self.__db_file = db_file
    self.__db = leveldb.LevelDB(self.__db_file)
  def __len__(self):
    return len(self.keys())
  def __getitem__(self, key):
    k = str.encode(str(key)) if not isinstance(key, bytes) else key
    return self.__db.Get(k)

  def __setitem__(self, key, value):
    k = str.encode(str(key)) if not isinstance(key, bytes) else key
    self.__db.Put(k, value)

  def __delitem__(self, key):
    k = str.encode(str(key)) if not isinstance(key, bytes) else key
    self.__db.Delete(k)

  def __iter__(self):
    for k in self.__db.RangeIter(include_value=False):
      yield k

  def keys(self):
    return [k for k, v in self.__db.RangeIter()]

  def items(self):
    return self.__db.RangeIter()

  def rangescan(self, start=None, end=None):
    if start is None and end is None:
      return self.__db.RangeIter()
    elif end is None:
      k = str.encode(str(start)) if not isinstance(start, bytes) else start
      return self.__db.RangeIter(k)
    else:
      start = str.encode(str(start)) if not isinstance(start, bytes) else start
      end = str.encode(str(end)) if not isinstance(end, bytes) else end
      return self.__db.RangeIter(start, end)

  def writebatch(self, values):
    batch = leveldb.WriteBatch()
    for key, value in values.items():
      k = str.encode(str(key)) if not isinstance(key, bytes) else key
      batch.Put(k, str.encode(json.dumps(value)))
    self.__db.Write(batch)

  def deleterange(self, start, end):
    batch = leveldb.WriteBatch()
    iterator = self.rangescan(start, end)
    for k in iterator:
      batch.Delete(k[0])
    self.__db.Write(batch)

class LevelDBJsonDict(LevelDBDict):
    def __getitem__(self, key):
        return json.loads(LevelDBDict.__getitem__(self, key))

    def __setitem__(self, key, value):
        LevelDBDict.__setitem__(self, key, str.encode(json.dumps(value)))

    def iteritems(self):
        for k, v in LevelDBDict.iteritems(self):
            yield k, json.loads(v)

    def rangescan(self, start=None, end=None):
        for k, v in LevelDBDict.rangescan(self, start, end):
            yield k, json.loads(v)

class LevelDBClient(OutputPlugin):
  def __init__(self):
    super(LevelDBClient, self).__init__("leveldb")
    self.__cache = []
    self.__cache_mutex = threading.Lock()
    self.__history = None
    self.__datapath = None
    self.__database = {}
  def Init(self, options):
    database = options.get("database")
    enable_query = options.get('enable_query')
    self._enable_query = (enable_query == 'True')
    history = options.get("history")
    self.__history = {'s': lambda x: timedelta(seconds=x),
                      'm': lambda x: timedelta(minutes=x),
                      'h': lambda x: timedelta(hours=x),
                      'd': lambda x: timedelta(days=x),
                      'y': lambda x: timedelta(years=x)}[history[-1]](int(history[:-1]))
    logging.info("configure-- database %s", database)
    if not os.path.exists(database):
      os.makedirs(database)
    self.__datapath = database

  def Push(self):
    try:
      with self.__cache_mutex:
        while len(self.__cache) > 0:
          cache = self.__cache[0]
          cache['table'].writebatch(cache['records'])
          self._size -= len(cache['records'])
          self.__cache.pop(0)
    except:
        logging.exception("leveldb send cache failed")
        return
    
    records = {}
    with self._queue_mutex:
      for body in self._queue:
        record = { 'time':body["time"], 'tags':body['tags'], 'fields':body['fields'] }

        table_name = body['table']
        recordlist = records.get(table_name)
        if recordlist:
          recordlist['records'][record['time']] = record
        else:
          table = self.__database.get(table_name, None)
          if table is None:
            table = LevelDBJsonDict(self.__datapath + "/" + table_name + ".db")
            self.__database[table_name] = table
          records[table_name] = {'table':table, 'records':{record['time']: record}}
        
      self._queue[:] = []
    try:
      tables={}
      for r in list(records.keys()):
        record = records[r]
        record['table'].writebatch(record['records'])
        self._size -= len(record['records'])
        tables[r] = record['table']
        del records[r]
      rmv_before = int((datetime.datetime.utcnow() - self.__history).strftime("%s"))
      for _, t in tables.items():
        self.RmvOlder(t, rmv_before)
    except:
      with self.__cache_mutex:
        for _, record in records.items():
          self.__cache.append(record)
  def GenerateRecord(self, table, time, tags, fields):
    json_body = {"table":table, "tags": tags, "time": time, "fields": fields}
    return json_body
  def LoseRecord(self):
    with self.__cache_mutex:
      if len(self.__cache) > 0:
        first = self.__cache[0]
        del(first[0])
        self._size -= 1
        if len(first) == 0:
          del(self.__cache[0])
      elif len(self._queue) > 0:
        del(self._queue[0])
        self._size -= 1

  def Query(self, json_request):
    ts_range = json_request.get('range')
    ts_from = ts_range.get('from')
    ts_to = ts_range.get('to')
    targets = json_request.get('targets')
    for target in targets:
      table_name = target.get('table')
      table = self.__database.get(table_name, None) 
      if table is None:
        table = LevelDBJsonDict(self.__datapath + "/" + table_name + ".db")
        self.__database[table_name] = table
      query_type = target.get('type')
      if query_type == 'all':
        return [v[1] for v in list(table.rangescan(ts_from, ts_to))]
      else:
        logging.error("Unsupported query type %s", query_type)
        return None

  def RmvOlder(self, t, oldtime):
    t.deleterange(0, oldtime)
    
