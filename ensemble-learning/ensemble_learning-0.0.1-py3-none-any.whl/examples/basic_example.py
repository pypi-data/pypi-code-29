import xgboost as xgb
from sklearn import datasets
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import *
from sklearn.model_selection import train_test_split

from ensemble_learning.EnsembleModels import EnsembleModels

# This example shows how to use the Ensemble Learning library. During this example
# it's used generated data for binary classification ( Hastie et al. 2009 )
X, y = datasets.make_hastie_10_2(n_samples=2000, random_state=42)

y[y < 1] = 0
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# Define several ML models
svm_model = svm.SVC(probability=True)
random_forest_model = RandomForestClassifier(max_depth=2, random_state=0)
xgb_model = xgb.XGBClassifier()

# Fit X_train and y_train data into the model
svm_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)
xgb_model.fit(X_train, y_train)

# Print F1-Score of ML models using X_test and y_test partitions
print("* F1-Score using SVM     : {} ".format(str(f1_score(y_test, svm_model.predict(X_test)))))
print("* F1-Score using RFOREST : {} ".format(str(f1_score(y_test, random_forest_model.predict(X_test)))))
print("* F1-Score using XGBOOST : {} ".format(str(f1_score(y_test, xgb_model.predict(X_test)))))

# Not let's use EnsembleModels package
models = [svm_model, random_forest_model, xgb_model]
EM = EnsembleModels(models, X_test, y_test)
print("--")
print(" Results with EM Package")
print(" * F1-Score using AVERAGING : {} ".format(str(f1_score(y_test, EM.averaging(proba=False)))))
print(" * F1-Score using VOTING    : {} ".format(str(f1_score(y_test, EM.voting(proba=False)))))
print(" * F1-Score using STACKING  : {} ".format(str(f1_score(y_test, EM.stacking(proba=False)))))
