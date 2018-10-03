from __future__ import print_function
import grpc
from . import straxrpc_pb2
from . import straxrpc_pb2_grpc
import pandas as pd
import numpy as np
from collections import defaultdict
import pickle

class StraxClient:

    def __init__(self, addr="localhost:50051"):
        self.addr = addr 

    def search_field(self, pattern):
         with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            sp = straxrpc_pb2.SearchPattern(pattern=pattern)
            rs = stub.SearchField(sp)
            results = [f"{r.name} is part of {r.data_name} (provided by {r.plugin})" for r in rs]
            # print(results)
            return results

    def data_info(self, dataname):
        with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            ti = straxrpc_pb2.TableInfo(name=dataname)
            r = stub.DataInfo(ti)
            df = pickle.loads(r.data)
            return df

    def get_array_iter(self, run_id, dframes):
        if isinstance(dframes, str):
            names = [dframes]
        else:
            names = dframes
        with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            ti = straxrpc_pb2.TableRequest(names=names, run_id=run_id)
            for r in stub.GetArray(ti):
                arr = pickle.loads(r.data)
                yield arr

    def get_array(self, run_id, dframe):
        records = np.hstack([arr for arr in self.get_array_iter(run_id, dframe)])
        return records

    def get_df_iter(self, run_id, dframe):
        for records in self.get_array_iter(run_id, dframe):
            df = pd.DataFrame.from_records(records)
            yield df

    def get_df(self, run_id, dframe):
        records = self.get_array(run_id, dframe)
        df = pd.DataFrame.from_records(records)
        return df

    def show_config(self, name):
        with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            ti = straxrpc_pb2.TableInfo(name=name)
            r = stub.ShowConfig(ti)
            df = pickle.loads(r.data)
            return df

    def search_dataframe_names(self, pattern):
        with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            sp = straxrpc_pb2.SearchPattern(pattern=pattern,)
            rs = stub.SearchDataframeNames(sp)
            names = [x.name for x in rs]
            # print(names)
            return names


            # data = {}
            # for col in stub.ShowConfig(ti):
            #     vs = getattr(col, col.info.dtype).values
            #     data[col.info.name] = pd.Series(index=col.index, data=vs)
            # df = pd.DataFrame(data)
            # return df


def run():
    client = StraxClient()
    print("---------------------- Search for s1* ----------------------")
    res = client.search_field( "s1*")
    print("\n".join(res))
    print("\n-------------- Data Info for event_basics --------------\n")
    df = client.data_info( 'event_basics')
    print(df)
    print("\n--------- Get event_basics df for 180423_1021 ---------\n")
    df = client.get_df( '180423_1021', 'event_basics')
    print(df)
    print("\n--------- Get event_basics array for 180423_1021 ---------\n")
    arr = client.get_array( '180423_1021', 'event_basics')
    print(arr.dtype.names)
    print(arr)

if __name__ == '__main__':
    run()
