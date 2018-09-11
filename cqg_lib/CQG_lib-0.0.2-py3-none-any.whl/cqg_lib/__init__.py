import pandas as pd

name = "cqg_lib"

class cqg():

    def __init__(self, current_path, how_many_curves_needed, data_arrays):
        self.current_path = current_path
        self.how_many_curves_needed = how_many_curves_needed
        self.data_arrays = data_arrays

    def data(self):

        df=pd.read_csv(self.current_path + "/mktdata.csv",header=None,sep=',').transpose()
        df.columns=['Open','High','Low','Close', 'min', 'ms']
        ts = df['min']*60 + df['ms']/1000 # in secs
        df = df.drop(['min', 'ms'], axis=1)
        df['Time'] = ts

        return df

    def connect(self):

        df = self.data(self)
        nulllist = ["nan"] * len(df['Time'])
        for i in range(self.how_many_curves_needed):
            print("curve")
            print(list(self.data_arrays[i]))
        for i in range(10 - self.how_many_curves_needed):
            print("curve")
            print(nulllist)
        #   print timestamp for IC to mark data point to specific bar
        print("curve")
        print(list(map(int, df['Time'])))

