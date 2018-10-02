from arctic import Arctic
import pandas as pd
import requests


class ArcticRepository:

    def __init__(self, config):
        self.config = config
        self.store = Arctic(config['arctic']['host'])
        self.store.initialize_library(config["arctic"]["collection"])
        self.library = self.store[config["arctic"]["collection"]]

    def insert(self, id, data, metadata):
        dataFrame = pd.DataFrame.from_dict(data)
        self.library.write(id, dataFrame, metadata=metadata)
        r = requests.put(self.config["elastic"]["url"] + id + '?pretty',
                         json=metadata)
        r.raise_for_status()
