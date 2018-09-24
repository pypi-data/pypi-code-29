from sklearn.model_selection import cross_val_score

class OpenFlow:
    def __init__(self, model, defaults=None):
        self.model = model
        self.inputs = {}
        self.defaults = defaults or {}

    def get_input(self, name, ds):
        """
        Retrieves the content of an input given a DataSource. The input acts like a filter over the outputs of the DataSource.

        Args:
            name (str): The name of the input.
            ds (openflow.DataSource): The DataSource that will feed the data.

        Returns:
            pandas.DataFrame: The content of the input.
        """
        columns = self.inputs.get(name)
        df = ds.get_dataframe()

        # set defaults
        for column in columns:
            if column not in df.columns:
                df[column] = self.defaults.get(column)

        return df[columns]

    def add_input(self, name, outputs):
        """
        Adds an input.

        Args:
            name (str): The name of the input.
            columns (list(str)): The outputs to extract from the DataSource.
        """
        self.inputs[name] = outputs

    def train(self, ds, limit=None, x_output='x', y_output='y'):
        x = self.get_input(x_output, ds)
        y = self.get_input(y_output, ds)

        if limit: x, y = x[-limit:], y[-limit:]

        self.model.fit(x.values, y.values.ravel())

    def benchmark(self, ds, limit=None, x_output='x', y_output='y'):
        x = self.get_input(x_output, ds)
        y = self.get_input(y_output, ds)

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
