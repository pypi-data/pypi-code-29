"""The Python implementation of the gRPC strax server."""

from concurrent import futures
import numpy as np
import pandas as pd
import strax
import time
import fnmatch
import grpc
from . import straxrpc_pb2
from . import straxrpc_pb2_grpc
from .data_types import type_testers
from . import config

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



def fake_df(ncol=10,nrow=10):
    data = {}
    for c in range(ncol):
        data['col_{}'.format(c)] = np.random.random(nrow)
    return pd.DataFrame(data)

def fake_arr(ncol=10,nrow=10):
    a = np.random.random((nrow,ncol))
    a.dtype=np.dtype([(('random column number {}'.format(c),'col_{}'.format(c)),np.float64) for c in range(ncol)])
    return a

def df_to_columns(df):
    cols = []
    for name in df.columns:
        dtype_name = str(df[name].dtype)
        for tester in type_testers:
            if tester.test(dtype_name):
                break
        else:
            continue

        info = straxrpc_pb2.ColumnInfo(
                  name=name,
                  dtype=tester.name,
            )
        try:
            values = tester.cast(df[name].values)
            data =  getattr(straxrpc_pb2,tester.column_class)(values=values)
            col_params = {'info': info, "index":df[name].index, tester.name:data}
            cols.append(straxrpc_pb2.DataColumn(**col_params))
        except:
            print("Could not transfer columns {}".format(name))
    return cols

def arr_to_columns(arr):
    cols = []
    for i, name in enumerate(arr.dtype.names):
        dtype_name = str(arr.dtype[i])
        for tester in type_testers:
            if tester.test(dtype_name):
                break
        else:
            continue

        info = straxrpc_pb2.ColumnInfo(
                  name=name,
                  dtype=tester.name,
            )
        values = arr[name].flatten()
        index = np.array(range(values.size), dtype=np.uint32)
        data =  getattr(straxrpc_pb2, tester.column_class)(values=values)
        col_params = {'info': info, "index":index, tester.name:data}
        cols.append(straxrpc_pb2.DataColumn(**col_params))
    return cols

def search_field(ctx, pattern):
    """
    Temporary fix, need to add pull request to have a flag to change this methods
    behavior so it returns a machine readable structure instead of printing to stdout.
    """
    match_list = []
    cache = dict()
    for d in ctx._plugin_class_registry:
        if d not in cache:
            cache.update(ctx._get_plugins((d,), run_id='0'))
        p = cache[d]

        for field_name in p.dtype.names:
            if fnmatch.fnmatch(field_name, pattern):
                match_list.append((field_name, d, p.__class__.__name__))
    return match_list

class StraxRPCServicer(straxrpc_pb2_grpc.StraxRPCServicer):

    def __init__(self, strax_context):
        print('Servicer started.')
        self.ctx = strax_context
        


    def SearchField(self, request, context):
        """
            TODO: Adapt search_field to accept flag for api usage of strax
            then change this method to:
                        match_list = self.ctx.search_field(pattern)
        """

        pattern = request.pattern
   
        match_list = search_field(self.ctx, pattern)
        for column, dataname, plugin in match_list:
            yield straxrpc_pb2.ColumnInfo(
                  name=column,
                  data_name=dataname,
                  plugin=plugin,
                 )


    def DataInfo(self, request, context):
      """

      """
      dataname = request.name
      df = self.ctx.data_info(dataname)
      for col in df_to_columns(df):
          yield col

    def GetDataframe(self, request, context):
        plugin_name = request.name
        run_id = request.run_id
        try:
            df = self.ctx.get_df(run_id, plugin_name) #
        except:
            df = fake_df() #
        for col in df_to_columns(df):
            yield col

    def GetArray(self, request, context):
        plugin_name = request.name
        run_id = request.run_id
        try:
            arr = self.ctx.get_array(run_id, plugin_name) #
        except:
            arr = fake_arr() #
        for col in arr_to_columns(arr):
            yield col

    def SearchDataframeNames(self, request, context):
        pattern = request.pattern
        for d in self.ctx._plugin_class_registry:
            if fnmatch.fnmatch(d, pattern):
                yield straxrpc_pb2.PluginInfo(name=d,)

    def ShowConfig(self, request, context):
        name = request.name
        df = self.ctx.show_config(name)
        for col in df_to_columns(df):
            yield col

class StraxServer:
    def __init__(self, addr="localhost:50051", strax_context=None):
        self.addr = addr

    def serve(self, strax_context):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        straxrpc_pb2_grpc.add_StraxRPCServicer_to_server(
            StraxRPCServicer(strax_context), server)
        server.add_insecure_port(self.addr)
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)

if __name__ == '__main__':
    from straxrpc import StraxServer
    server = StraxServer()
    ctx = strax.Context(
            storage=[strax.ZipDirectory(config.ZIPDIR),
                     strax.DataDirectory(config.DATADIR)],
            register_all=strax.xenon.plugins) 
    server.serve(ctx)
