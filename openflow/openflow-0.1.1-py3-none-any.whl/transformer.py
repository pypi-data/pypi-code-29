class Transformer:
    """
    Transforms DataFrame into another DataFrame.

    Parameters
    ----------
    transformation : array-like
        Array of tuples. First value is the name of the computed column. Second value is the transformation to be applied to a DataFrame in order to compute the column.

    Examples
    --------
    >>> openflow.Transformer([('double', lambda df: 2 * df['number']), ('datetime', lambda df: pandas.to_datetime(df['timestamp'], unit='s'))])
    """
    def __init__(self, transformation):
        self.transformation = transformation

    def transform(self, df):
        """
        Transforms a DataFrame. Starts with a copy of the DataFrame. The order of the transformation functions is important if transformed columns are reused.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame to transform.

        Returns
        -------
        pandas.DataFrame
            Transformed DataFrame.
        """
        copy = df.copy()
        for column, function in self.transformation:
            copy[column] = copy.apply(function, axis=1)
        return copy
