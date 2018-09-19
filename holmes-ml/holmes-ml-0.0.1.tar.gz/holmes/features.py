__author__ = 'Bryan Farris'
import featuretools as ft
import os
import pickle
from featuretools.primitives import Mean, Std, Count, Sum, AvgTimeBetween, NUnique, Mode, Day, Weekend
import shutil
from dataloader import DataLoader

class FeatureSynthesis():
    """
    Responsible for performing deep feature synthesis on an entity set.
    """

    @staticmethod
    def synthesize(es, baseline=False, out_path="out", verbose=False):

        # Recreate Out Path Directory
        try:
            shutil.rmtree(out_path)
        except:
            pass
        os.mkdir(out_path)

        # Try to load features that were saved from first run
        feature_list_file = os.path.join(out_path, 'feature_list')
        try:
            feature_list = ft.load_features(feature_list_file, es)
        except:
            if baseline:
                # Implement baseline by running dfs with minimal options
                agg_primitives = []
                trans_primitives = []
                max_depth = 1
            else:
                agg_primitives = [Mean, Std, Count, Sum,
                                  NUnique, Mode, AvgTimeBetween]
                trans_primitives = [Day, Weekend]
                max_depth = 3

            feature_list = ft.dfs(entityset=es,
                                  target_entity="transactions",
                                  agg_primitives=agg_primitives,
                                  trans_primitives=trans_primitives,
                                  ignore_variables={'transactions': [DataLoader.card_id_field()]},
                                  max_depth=max_depth,
                                  features_only=True,
                                  verbose=verbose)

            # Save features
            ft.save_features(feature_list, feature_list_file)
            categorical_indicies = [i for i, f in enumerate(feature_list)
                                    if issubclass(f.variable_type, ft.variable_types.Discrete)]
            pickle.dump(categorical_indicies, open(os.path.join(out_path, 'cat_indicies.p'), 'wb'))

        return feature_list

    @staticmethod
    def feature_matrix(es, transactions, feature_list, approximate=None, training_window="90 days", verbose=None):
        # Cutoff times per instance
        cutoff_times = transactions[[DataLoader.transaction_id_field(), DataLoader.transaction_date_field()]]
        cutoff_times.columns = ["instance_id", "time"]

        feature_matrix = ft.calculate_feature_matrix(features=feature_list, entityset=es, approximate=approximate,
                                                     training_window=training_window, cutoff_time=cutoff_times,
                                                     verbose=verbose)
        return feature_matrix
