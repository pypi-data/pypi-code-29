from keras.callbacks import Callback
import joblib
import os


def store_train_params(model_id, x, y):
    joblib.dump(x, '/data/out/%s_x_train.pkl' % model_id, True)
    joblib.dump(y, '/data/out/%s_y_train.pkl' % model_id, True)


def store_validate_params(model_id, x, y):
    joblib.dump(x, '/data/out/%s_x_test.pkl' % model_id, True)
    joblib.dump(y, '/data/out/%s_y_test.pkl' % model_id, True)


def fit(model_id, model, x_train, y_train, **kwargs):
    checkpoint = FitchainCheckpoint(model_id)

    callbacks_list = []

    # -- check if there are already callbacks defined
    if "callbacks" in kwargs:
        callbacks_list = kwargs["callbacks"]

    callbacks_list.append(checkpoint)

    return model.fit(x_train, y_train, callbacks=callbacks_list, **kwargs)


class FitchainCheckpoint(Callback):
    """Save the model after every epoch.

    # Arguments
        model_id: string, a unique identifier of the model being trained
    """

    def __init__(self, model_id):
        super(FitchainCheckpoint, self).__init__()
        self.model_id = model_id
        self.path = "/data/out/%s" % self.model_id

    def on_epoch_end(self, epoch, logs=None):
        self.model.save("%s_%d.keras.tmp" % (self.path, epoch), overwrite=True)
        os.rename("%s_%d.keras.tmp" % (self.path, epoch), "%s_%d.keras" % (self.path, epoch))
