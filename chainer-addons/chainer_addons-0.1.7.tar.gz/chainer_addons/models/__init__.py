"""
here you can find some model definitions or modificated versions
of present models in chainer (eg. VGG19)
"""
import chainer
import chainer.functions as F
import chainer.links as L
from chainer.serializers import npz

from inspect import signature
from collections import OrderedDict

import numpy as np

def do_call(func, *args, **kw):
	sig = signature(func)
	train = kw.pop("train", True)
	if "train" in sig.parameters: 	kw["train"] = train
	elif "test" in sig.parameters:	kw["test"]  = not train

	return func(*args, **kw)

class Classifier(chainer.Chain):
	"""
		model wrapper, that is adapted for the DSL of
		the pretrained models in chainer
	"""
	def __init__(self, model, layer_name):
		super(Classifier, self).__init__()
		with self.init_scope():
			self.model = model

		self.layer_name = layer_name

	def __call__(self, X, y):
		activations = self.model(X, layers=[self.layer_name])
		pred = activations[self.layer_name]

		loss, accu = F.softmax_cross_entropy(pred, y), F.accuracy(pred, y)
		chainer.report({
			"loss": loss.data,
			"accuracy": accu.data,
		}, self)
		return loss

class PretrainedModelMixin(object):

	@classmethod
	def prepare(cls, img, size=None):
		size = size or cls.meta.input_size
		return cls.meta.prepare_func(img, size=(size, size))

	@classmethod
	def prepare_back(cls, img):
		img = img.transpose(1,2,0).copy()
		img += cls.meta.mean.squeeze()
		img = img[..., ::-1].astype(np.uint8)
		return img

	def load_pretrained(self, weights, n_classes):

		layer_name = self.meta.classifier_layers[-1]
		delattr(self, layer_name)
		layer = L.Linear(self.meta.feature_size, n_classes)
		setattr(self, layer_name, layer)

		if weights not in [None, "auto"]:
			npz.load_npz(weights, self)


	@property
	def functions(self):

		return OrderedDict(self._links)


	def __call__(self, X, layer_name=None):
		layer_name = layer_name or self.meta.classifier_layers[-1]
		activations = super(PretrainedModelMixin, self).__call__(X, layers=[layer_name])
		return activations[layer_name]


from chainer_addons.models.vgg import VGG19Layers
from chainer_addons.models.resnet import ResnetLayers, Resnet35Layers
