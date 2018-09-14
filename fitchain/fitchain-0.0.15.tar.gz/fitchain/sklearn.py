import joblib
import os


def store_train_params(model_id, **kwargs):
    for key, val in kwargs.items():
        joblib.dump(val, '/data/out/%s_%s_train.pkl' % (model_id, key), True)


def store_validate_params(model_id, **kwargs):
    for key, val in kwargs.items():
        joblib.dump(val, '/data/out/%s_%s_test.pkl' % (model_id, key), True)


def fit(model_id, model, args):
    model.fit(**args)

    joblib.dump(model, '/data/out/%s.sklearn.old' % model_id, True)
    os.rename('/data/out/%s.sklearn.old' % model_id, '/data/out/%s.sklearn' % model_id)

