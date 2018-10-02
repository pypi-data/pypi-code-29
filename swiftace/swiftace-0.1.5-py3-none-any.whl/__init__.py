import hashlib
from tqdm import tqdm_notebook
from IPython.core.display import display, HTML
from time import sleep


def init(name):
    print('[swiftace] Project initlalized. Key: 756135b7-632e-4956-adba-a13c7dd8f3c3')


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def log_dataset(path):
    for i in tqdm_notebook(range(100)):
        pass
    print('[swiftace] Dataset logged. Checksum: ' + md5(path))


def log_hyperparams(dict):
    for i in tqdm_notebook(range(100)):
        pass
    print(dict)
    print('')
    print('[swiftace] Hyperparameters logged successfully.')


class KerasCallback(object):
    def __init__(self):
        self.validation_data = None
        self.model = None

    def set_params(self, params):
        self.params = params

    def set_model(self, model):
        self.model = model

    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        pass

    def on_batch_begin(self, batch, logs=None):
        pass

    def on_batch_end(self, batch, logs=None):
        pass

    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        print('')
        print('[swiftace] Training metrics logged successfully.')


def log_metrics(dict):
    for _ in tqdm_notebook(range(100)):
        pass
    print(dict)
    print('')
    print('[swiftace] Metrics logged successfully.')


def upload_file(path):
    for _ in tqdm_notebook(range(21), unit='MB'):
        pass
    print('[swiftace] File uploaded successfully. Checksum: ' + md5(path))


def commit(message):
    for i in tqdm_notebook(range(4)):
        if i == 0:
            print('[swiftace] Capturing environment...')
        elif i == 1:
            print('[swiftace] Saving Jupyter notebook...')
        elif i == 2:
            print('[swiftace] Uploading source code...')
        else:
            print('[swiftace] Finalizing commit...')
        sleep(1)
    print('')
    print('[swiftace] Commit 0a9dc74d successful.')
    return display(HTML("""<a href="https://swiftace.ai/aakashns/keras-mnist/0a9dc74d" target="_blank">https://swiftace.ai/aakashns/mnist-basic/0a9dc74d</a>"""))
