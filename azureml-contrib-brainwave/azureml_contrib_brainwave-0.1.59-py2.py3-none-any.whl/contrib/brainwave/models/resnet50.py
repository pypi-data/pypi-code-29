# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Module with the renset-50 model.
"""
from azureml.contrib.brainwave.models.brainwave_model import BrainwaveModel
import os
import requests
import zipfile
import tensorflow as tf


class AbstractResnet50(BrainwaveModel):
    """
    Abstract baseclass for resnet-50
    """
    _input_op = 'InputImage'
    _prefix = 'resnet_v1_50/'
    _output_op = '{0}pool5'.format(_prefix)
    _save_name = "resnet50"

    @classmethod
    def _download_classifier(cls, model_dir):
        rndir = os.path.join(model_dir, cls._modelname, cls._modelver)
        _classifier_location = os.path.join(rndir, "resnet50_classifier.pb")
        if not os.path.exists(_classifier_location):
            if not os.path.exists(rndir):
                os.makedirs(rndir)
            r = requests.get(cls.classifier_uri)
            model_zip_path = os.path.join(rndir, 'classifier.zip')
            with open(model_zip_path, 'wb') as output:
                output.write(r.content)
            zip_ref = zipfile.ZipFile(model_zip_path, 'r')
            zip_ref.extractall(rndir)
            zip_ref.close()
            os.remove(model_zip_path)
        return _classifier_location

    @classmethod
    def get_default_classifier(cls, input_tensor, model_dir):
        """
        Import a default Imagenet classifier for resnet-50 into the current graph.
        :param input_tensor: The input feature tensor for the classifier. Expected to be [?, 2048]
        :param model_dir: The directory to download the classifier into. Used as a cache locally.
        :return:
        """
        _classifier_location = cls._download_classifier(model_dir)

        input_map = {'Input': input_tensor}
        input_graph_def = tf.GraphDef()
        with tf.gfile.Open(_classifier_location, "rb") as f:
            data = f.read()

            input_graph_def.ParseFromString(data)

        tensors = tf.import_graph_def(input_graph_def, name='', input_map=input_map,
                                      return_elements=['Input:0', '{0}logits/Softmax:0'.format(cls._prefix)])
        return tensors[0], tensors[1]

    @property
    def output_dims(self):
        """
        Get output dimensions
        """
        return [None, 1, 1, 2048]

    @property
    def input_dims(self):
        """
        Get input dimensions
        """
        return [None, 244, 244, 3]


class Resnet50(AbstractResnet50):
    """
    Float-32 Version of Resnet-50.
    """
    _modelname = "rn50"
    _modelver = "1.1.1"

    classifier_uri = "https://go.microsoft.com/fwlink/?linkid=2017246&clcid=0x409"

    def __init__(self, model_base_path):
        """
        Create a Float-32 version of resnet 50.
        :param model_base_path: Path to download the model into. Used as a cache locally.
        """
        super().__init__(model_base_path, self._modelname, self._modelver,
                         "https://go.microsoft.com/fwlink/?linkid=2020823&clcid=0x409", self._save_name)


class QuantizedResnet50(AbstractResnet50):
    """
    Quantized version of Renset-50.
    """

    _modelname = "msfprn50"
    _modelver = "1.1.2"

    def __init__(self, model_base_path, is_frozen=False, custom_weights_directory=None):
        """
        Create a version of resnet 50 quantized for Project Brainwave.
        :param model_base_path: Path to download the model into. Used as a cache locally.
        :param is_frozen: Should the weights of the resnet-50 be frozen when it is imported. Freezing the weights can
        lead to faster training time, but may cause your model to perform worse overall. Defaults to false.
        :param custom_weights_directory: Directory to load pretrained resnet-50 weights from. Can load weights from
        either a float-32 version or a quantized version. If none, will load weights trained for accuracy on the
        Imagenet dataset.
        """
        super().__init__(model_base_path,
                         self._modelname,
                         self._modelver,
                         "https://go.microsoft.com/fwlink/?linkid=2020764&clcid=0x409",
                         self._save_name,
                         is_frozen=is_frozen,
                         weight_path=custom_weights_directory)
