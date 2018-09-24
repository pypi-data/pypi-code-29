import os, logging

class DataSource:
    """
    Extracts raw data then restitute it as an arranged DataFrame.

    Args:
        preprocess (lambda): Preprocess DataFrame before transformation
    """
    def __init__(self, run, preprocess=None):
        self.run = run
        self.preprocess = preprocess or (lambda df: df)
        self.context = None
        self.df = None
        self.outputs = []

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
            df[name] = function(df)

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

        self.df = self.run(self.context)

        # compute df = transform(preprocess(df)
        self.df = self.preprocess(self.df)
        self.transform(self.df)

        return self.df

    def set_context(self, context):
        """
        Set context for runtime. Will be passed to run() function.

        Args:
            context (obj): Context to be passed to run().
        """
        self.context = context
