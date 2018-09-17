from sklearn.model_selection import cross_val_score

class OpenFlow:
    def __init__(self, model):
        self.model = model
        self.outputs = {}

    def get_output(self, ds, name):
        """
        Retrieves the content of an output given a DataSource. The output acts like a filter over the columns of the DataSource.

        Parameters
        ----------
        ds : openflow.DataSource
            The DataSource from which the data are extracted.
        name : str
            The name of the output.

        Returns
        -------
        pandas.DataFrame
            The content of the output.
        """
        columns = self.outputs.get(name)
        return ds.get_dataframe()[columns]

    def add_output(self, name, columns):
        """
        Adds an output to the DataSource.

        Parameters
        ----------
        name : str
            The name of the output.
        columns : array-like
            The columns to extract.
        """
        self.outputs[name] = columns

    def train(self, ds, limit=None, x_output='x', y_output='y'):
        x = self.get_output(ds, x_output)
        y = self.get_output(ds, y_output)

        if limit: x, y = x[-limit:], y[-limit:]

        self.model.fit(x.values, y.values.ravel())

    def benchmark(self, ds, limit=None, x_output='x', y_output='y'):
        x = self.get_output(ds, x_output)
        y = self.get_output(ds, y_output)

        if limit: x, y = x[-limit:], y[-limit:]

        return cross_val_score(self.model, x.values, y.values.ravel(), cv=5, scoring='neg_mean_squared_error')

# from utils import flatten
#
# class InputBuilder:
#     def __init__(self, defaults, features):
#         self.defaults = defaults
#         self.features = features
#
#     def get_input(self, request):
#         # merge request over defaults
#         merged_request = {**self.defaults, **request}
#         return flatten([f(merged_request) for f in self.features])
