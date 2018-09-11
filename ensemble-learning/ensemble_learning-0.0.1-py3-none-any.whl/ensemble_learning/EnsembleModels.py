import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split


class EnsembleModels:

    def __init__(self, models, X_test, y_test):
        """
         Ensemble models of different ML Algorithms using different Ensemble Methods
            # Arguments
                models: Array
                    Array of objects models (pre trained models)

                X_test : numpy.ndarray
                    Data for prediction

                y_test : numpy.ndarray (Not used)
                    Data Labels of the prediction
        """
        super().__init__()

        self.models = models
        self.X_test = X_test
        self.y_test = y_test

        self.predictions_df = pd.DataFrame()
        for idx, model in enumerate(models):

            model_type = str(type(model))
            model_type = model_type.replace("<class '", "")
            model_type = model_type.replace("'>", "")

            y_predict = model.predict_proba(X_test)[:, 1]
            model_name = str(idx) + "_" + model_type
            self.predictions_df[model_name] = y_predict

    def averaging(self, proba=False):
        """
            Averaging : Calculate the prediction using the average of the
            different predictions of the model
            # Arguments
               proba: If True  will returns the probability estimates
        """
        average = self.predictions_df.mean(axis=1)
        if not proba:
            return (average > 0.5).astype(np.int_).values
        return average.values

    def voting(self, proba=False):
        """
            Voting : Calculate the prediction using the mode of the
            different predictions of the model
            # Arguments
               proba: If True  will returns the probability estimates
        """
        mode = self.predictions_df.mode(axis=1)[0]
        if not proba:
            return (mode > 0.5).astype(np.int_).values
        return mode.values

    def stacking(self, proba=False):
        """
            Voting : Calculate the prediction using stacking (under dev)
            # Arguments
               proba: If True  will returns the probability estimates
        """
        X_train, X_test, y_train, y_test = train_test_split(self.predictions_df, self.y_test, test_size=0.25,
                                                            random_state=42, stratify=self.y_test)
        xgb_model = xgb.XGBClassifier()
        xgb_model.fit(X_train, y_train)

        pred = xgb_model.predict_proba(self.predictions_df)[:, 1]
        if not proba:
            return (pred > 0.5).astype(np.int_)
        return pred
