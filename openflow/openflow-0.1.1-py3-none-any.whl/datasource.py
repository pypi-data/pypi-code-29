import os, logging

import pandas as pd
import psycopg2
import psycopg2.extras

from .transformer import Transformer

class DataSource:
    def __init__(self, transformation, preprocess=None):
        self.transformer = Transformer(transformation)
        self.preprocess = preprocess
        self.data = None
        self.df = None

    def get_dataframe(self, force_computation=False):
        """
        Preprocesses then transforms the return of run().

        Parameters
        ----------
        force_computation : int, optional
            Default to False. If set to True, forces the computation of DataFrame at each call.

        Returns
        -------
        pandas.DataFrame
            Preprocessed and transformed DataFrame.
        """
        # returns df if already computed
        if self.df is not None and not force_computation: return self.df

        # compute df = transform(preprocess(run()))
        self.df = self.run(self.data)
        if self.preprocess: self.df = self.preprocess(self.df)
        self.df = self.transformer.transform(self.df)

        return self.df

    def set_data(self, data):
        """
        Set data at runtime. Will be passed to run() function.

        Parameters
        ----------
        data : Object
            Data to be passed to run().
        """
        self.data = data
