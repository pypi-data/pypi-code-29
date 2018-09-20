import os, logging

class DataSource:
    """
    Extracts raw data then restitute it as an arranged DataFrame.

    Args:
        preprocess (lambda): Preprocess DataFrame before transformation
    """
    def __init__(self, preprocess=None):
        self.outputs = []
        self.preprocess = preprocess or (lambda df: df)
        self.data = None
        self.df = None

    def add_output(self, name, function):
        """
        Adds an output to the DataSource. The order in which the outputs are appended is important if previous outputs are reused.

        Args:
            name (str): Name of the output
            function (lambda): Function to apply to DataFrame

        Examples:
            >>> add_output('double', lambda df: 2 * df['number'])
        """
        self.outputs.append((name, function))

    def transform(self, df):
        """
        Transforms a DataFrame in place. Computes all outputs of the DataFrame.

        Args:
            df (pandas.DataFrame): DataFrame to transform.
        """
        for name, function in self.outputs:
            df[name] = df.apply(function, axis=1)

    def get_dataframe(self, force_computation=False):
        """
        Preprocesses then transforms the return of run().

        Args:
            force_computation (bool, optional) : Defaults to False. If set to True, forces the computation of DataFrame at each call.

        Returns:
            pandas.DataFrame: Preprocessed and transformed DataFrame.
        """
        # returns df if it was already computed
        if self.df is not None and not force_computation: return self.df

        self.df = self.run(self.data)

        # compute df = transform(preprocess(df)
        self.df = self.preprocess(self.df)
        self.transform(self.df)

        return self.df

    def set_data(self, data):
        """
        Set data at runtime. Will be passed to run() function.

        Args:
            data (obj): Data to be passed to run().
        """
        self.data = data
