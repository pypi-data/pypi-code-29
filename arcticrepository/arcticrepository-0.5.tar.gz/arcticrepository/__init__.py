from arctic import Arctic
import pandas as pd
import requests


class ArcticRepository:

    def __init__(self, config):
        self.config = config
        self.store = Arctic(config['arctic']['host'])
        self.store.initialize_library(config["arctic"]["collection"])
        self.library = self.store[config["arctic"]["collection"]]


    def checkIfNewVersion(self, symbol, dataFrame, metadata):
        """Check if an update or insert of the DataFrame is required"""
        #Check for symbol in arctic
        try:
            #If symbol already exists read it
            item = self.library.read(symbol)
        except:
            #If symbol does not exist this is a new version exit function and return True
            return True

        #If both time series data and metadata are the same return false
        #if data.equals(item.data) and dict(metadata) == dict(item.metadata):
        if dataFrame.equals(item.data) and metadata == item.metadata:
            return False
        else:
            return True


    def insert(self, id, data, metadata):
        """Upsert the DataFrame into Arctic and Indexer"""
        dataFrame = pd.DataFrame.from_dict(data)
        if(self.checkIfNewVersion(id, dataFrame, metadata)):
            self.library.write(id, dataFrame, metadata=metadata)
            r = requests.put(self.config["elastic"]["url"] + id + '?pretty',
                         json=metadata)
            r.raise_for_status()


    def read(self, name):
        """Read DataFrame from Arctic using the provided ticker"""
        return self.library.read(name)

    def get_info(self, name):
        """Read DataFrame from Arctic using the provided ticker"""
        return self.library.get_info(name)
