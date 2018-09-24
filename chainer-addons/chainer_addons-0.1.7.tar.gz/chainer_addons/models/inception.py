import chainer
import chainer.functions as F
import chainer.links as L

from chainer.serializers import load_hdf5

from os.path import isfile

import numpy as np

def __pooling_op(operation):
	if operation == "avg":
		return F.average_pooling_2d
	elif operation == "max":
		return F.max_pooling_2d
	else:
		raise ValueError("Unkown pooling operation: {}".format(operation))

def global_pooling(operation):
	def inner(x):
		ksize = x.shape[2:]
		return __pooling_op(operation)(x, ksize)
	return inner


def pooling(operation, ksize, stride=1, pad=0):
	def inner(x):
		return __pooling_op(operation)(x, ksize, stride, pad)
	return inner

def prepare(cls, x, size=(299, 299)):
	# TODO: resize

	x = x.astype(np.float32) - cls.meta.mean
	x = x.transpose(2,0,1)
	return x / 127.5

class Conv2D_BN(chainer.Chain):
	def __init__(self, insize, outsize, ksize, stride=1, pad=0, activation=F.relu):
		super(Conv2D_BN, self).__init__()
		assert callable(activation)

		with self.init_scope():
			self.conv = L.Convolution2D(insize, outsize,
				ksize=ksize, stride=stride, pad=pad, nobias=True)
			self.bn = L.BatchNormalization(outsize, use_gamma=False)

		self.activation = activation

	def __call__(self, x):
		x = self.conv(x)
		x = self.bn(x)
		return self.activation(x)

class InceptionHead(chainer.Chain):
	def __init__(self):
		super(InceptionHead, self).__init__()
		with self.init_scope():
			self.conv1 = Conv2D_BN(3,   32, ksize=3, stride=2)
			self.conv2 = Conv2D_BN(32,  32, ksize=3)
			self.conv3 = Conv2D_BN(32,  64, ksize=3)
			self.pool4 = pooling("max",     ksize=3, stride=2)

			self.conv5 = Conv2D_BN(64,  80, ksize=1)
			self.conv6 = Conv2D_BN(80, 192, ksize=3)
			self.pool7 = pooling("max",     ksize=3, stride=2)

	def __call__(self, x):
		x = self.conv1(x)
		x = self.conv2(x)
		x = self.conv3(x)
		x = self.pool4(x)
		x = self.conv5(x)
		x = self.conv6(x)
		x = self.pool7(x)
		return x

class Inception1(chainer.Chain):
	def __init__(self, insize, sizes, outputs, **pool_args):
		super(Inception1, self).__init__()

		out1x1, out5x5, out3x3, out_pool = outputs
		s5x5, s3x3_1, s3x3_2 = sizes

		with self.init_scope():
			self.conv1x1   = Conv2D_BN(insize, out1x1, ksize=1)

			self.conv5x5_1 = Conv2D_BN(insize, s5x5,   ksize=1)
			self.conv5x5_2 = Conv2D_BN(s5x5,   out5x5, ksize=5, pad=2)

			self.conv3x3_1 = Conv2D_BN(insize, s3x3_1, ksize=1)
			self.conv3x3_2 = Conv2D_BN(s3x3_1, s3x3_2, ksize=3, pad=1)
			self.conv3x3_3 = Conv2D_BN(s3x3_2, out3x3, ksize=3, pad=1)

			self.pool_conv = Conv2D_BN(insize, out_pool, ksize=1)
		self.pool = pooling(**pool_args)

	def __call__(self, x):

		y0 = self.conv1x1(x)
		y1 = self.conv5x5_2(self.conv5x5_1(x))
		y2 = self.conv3x3_3(self.conv3x3_2(self.conv3x3_1(x)))
		y3 = self.pool_conv(self.pool(x))
		return F.concat([y0, y1, y2, y3])

class Inception2(chainer.Chain):
	def __init__(self, insize, sizes, outputs, **pool_args):
		super(Inception2, self).__init__()

		out1, out2 = outputs
		size1, size2 = sizes
		with self.init_scope():
			self.conv3x3   = Conv2D_BN(insize, out1 , ksize=3, stride=2)

			self.conv3x3_1 = Conv2D_BN(insize, size1, ksize=1)
			self.conv3x3_2 = Conv2D_BN(size1,  size2, ksize=3)
			self.conv3x3_3 = Conv2D_BN(size2,  out2,  ksize=3, stride=2, pad=1)

		self.pool = pooling(**pool_args)

	def __call__(self, x):
		y0 = self.conv3x3(x)
		y1 = self.conv3x3_3(self.conv3x3_2(self.conv3x3_1(x)))
		y2 = self.pool(x)
		return F.concat([y0, y1, y2])

class Inception3(chainer.Chain):
	def __init__(self, insize, sizes, outputs, **pool_args):
		super(Inception3, self).__init__()

		out1x1, out7x7, out7x7x2, out_pool = outputs
		s7x7_1, s7x7_2, s7x7x2_1, s7x7x2_2, s7x7x2_3, s7x7x2_4 = sizes

		with self.init_scope():
			self.conv1x1 = Conv2D_BN(insize,       out1x1, ksize=1)

			self.conv7x7_1 = Conv2D_BN(insize,     s7x7_1, ksize=1)
			self.conv7x7_2 = Conv2D_BN(s7x7_1,     s7x7_2, ksize=(1,7), pad=(0,3))
			self.conv7x7_3 = Conv2D_BN(s7x7_2,     out7x7, ksize=(7,1), pad=(3,0))

			self.conv7x7x2_1 = Conv2D_BN(insize,   s7x7x2_1, ksize=1)
			self.conv7x7x2_2 = Conv2D_BN(s7x7x2_1, s7x7x2_2, ksize=(7,1), pad=(0,3))
			self.conv7x7x2_3 = Conv2D_BN(s7x7x2_2, s7x7x2_3, ksize=(1,7), pad=(3,0))
			self.conv7x7x2_4 = Conv2D_BN(s7x7x2_3, s7x7x2_4, ksize=(7,1), pad=(0,3))
			self.conv7x7x2_5 = Conv2D_BN(s7x7x2_4, out7x7x2, ksize=(1,7), pad=(3,0))

			self.pool_conv = Conv2D_BN(insize, out_pool, ksize=1)

		self.pool = pooling(**pool_args)

	def __call__(self, x):
		y0 = self.conv1x1(x)
		y1 = self.conv7x7_3(self.conv7x7_2(self.conv7x7_1(x)))
		y2 = self.conv7x7x2_5(self.conv7x7x2_4(self.conv7x7x2_3(self.conv7x7x2_2(self.conv7x7x2_1(x)))))
		y3 = self.pool_conv(self.pool(x))

		return F.concat([y0, y1, y2, y3])

class Inception4(chainer.Chain):
	def __init__(self, insize, sizes, outputs, **pool_args):
		super(Inception4, self).__init__()

		out3x3, out7x7 = outputs
		s3x3, s7x7_1, s7x7_2, s7x7_3 = sizes

		with self.init_scope():
			self.conv3x3_1 = Conv2D_BN(insize, s3x3, ksize=1)
			self.conv3x3_2 = Conv2D_BN(s3x3, out3x3, ksize=3, stride=2)

			self.conv7x7_1 = Conv2D_BN(insize, s7x7_1, ksize=1)
			self.conv7x7_2 = Conv2D_BN(s7x7_1, s7x7_2, ksize=(1, 7), pad=(0, 3))
			self.conv7x7_3 = Conv2D_BN(s7x7_2, s7x7_3, ksize=(7, 1), pad=(3, 0))
			self.conv7x7_4 = Conv2D_BN(s7x7_3, out7x7, ksize=3, stride=2)

		self.pool = pooling(**pool_args)

	def __call__(self, x):

		y0 = self.conv3x3_2(self.conv3x3_1(x))
		y1 = self.conv7x7_4(self.conv7x7_3(self.conv7x7_2(self.conv7x7_1(x))))
		y2 = self.pool(x)

		return F.concat([y0, y1, y2])

class Inception5(chainer.Chain):
	def __init__(self, insize, sizes, outputs, **pool_args):
		super(Inception5, self).__init__()

		out1x1, out3x3, out3x3x2, out_pool = outputs
		s3x3, s3x3x2_1, s3x3x2_2 = sizes

		with self.init_scope():

			self.conv1x1 = Conv2D_BN(insize, out1x1, ksize=1)

			self.conv3x3_1 = Conv2D_BN(insize, s3x3, ksize=1)
			self.conv3x3_2 = Conv2D_BN(s3x3, out3x3, ksize=(1, 3), pad=(0,1))
			self.conv3x3_3 = Conv2D_BN(s3x3, out3x3, ksize=(3, 1), pad=(1,0))

			self.conv3x3x2_1 = Conv2D_BN(insize  , s3x3x2_1, ksize=1)
			self.conv3x3x2_2 = Conv2D_BN(s3x3x2_1, s3x3x2_2, ksize=3, pad=1)
			self.conv3x3x2_3 = Conv2D_BN(s3x3x2_2, out3x3x2, ksize=(1, 3), pad=(0,1))
			self.conv3x3x2_4 = Conv2D_BN(s3x3x2_2, out3x3x2, ksize=(3, 1), pad=(1,0))

			self.pool_conv = Conv2D_BN(insize, out_pool, ksize=1)

		self.pool = pooling(**pool_args)


	def __call__(self, x):
		y0 = self.conv1x1(x)


		y1 = self.conv3x3_1(x)
		y1 = F.concat([self.conv3x3_2(y1), self.conv3x3_3(y1)])

		y2 = self.conv3x3x2_2(self.conv3x3x2_1(x))
		y2 = F.concat([self.conv3x3x2_3(y2), self.conv3x3x2_4(y2)])

		y3 = self.pool_conv(self.pool(x))

		return F.concat([y0, y1, y2, y3])

class InceptionV3(chainer.Chain):

	class meta:
		input_size = 448
		n_conv_maps = 2048
		feature_size = 2048
		mean = np.array([127.5, 127.5, 127.5], dtype=np.float32).reshape(3,1,1)
		prepare_func = prepare

		classifier_layers = ["..."]
		conv_map_layer = "..."
		feature_layer = "..."

	def __init__(self, pretrained_model, n_classes=1000):
		super(InceptionV3, self).__init__()

		with self.init_scope():
			self.head = InceptionHead()

			pool_args = dict(operation="avg", ksize=3, stride=1, pad=1)
			self.mixed00 = Inception1(insize=192, sizes=[48, 64, 96], outputs=[64, 64, 96, 32], **pool_args)
			self.mixed01 = Inception1(insize=256, sizes=[48, 64, 96], outputs=[64, 64, 96, 64], **pool_args)
			self.mixed02 = Inception1(insize=288, sizes=[48, 64, 96], outputs=[64, 64, 96, 64], **pool_args)

			pool_args = dict(operation="max", ksize=3, stride=2, pad=0)
			self.mixed03 = Inception2(288, sizes=[64, 96], outputs=[384, 96], **pool_args)

			pool_args = dict(operation="avg", ksize=3, stride=1, pad=1)
			self.mixed04 = Inception3(768, sizes=[128] * 6, outputs=[192] * 4, **pool_args)
			self.mixed05 = Inception3(768, sizes=[160] * 6, outputs=[192] * 4, **pool_args)
			self.mixed06 = Inception3(768, sizes=[160] * 6, outputs=[192] * 4, **pool_args)
			self.mixed07 = Inception3(768, sizes=[192] * 6, outputs=[192] * 4, **pool_args)

			pool_args = dict(operation="max", ksize=3, stride=2, pad=0)
			self.mixed08 = Inception4(768, sizes=[192] * 4, outputs=[320, 192], **pool_args)

			# here the middle outputs are doubled!
			pool_args = dict(operation="avg", ksize=3, stride=1, pad=1)
			self.mixed09 = Inception5(1280, sizes=[384, 448, 384], outputs=[320, 384, 384, 192], **pool_args)
			self.mixed10 = Inception5(2048, sizes=[384, 448, 384], outputs=[320, 384, 384, 192], **pool_args)

			self.pool = global_pooling("avg")
			self.fc = L.Linear(2048, n_classes)

		if pretrained_model is not None and isfile(pretrained_model):
			if pretrained_model.endswith(".h5"):
				self._load_from_keras(pretrained_model)
			else:
				from chainer.serializers import load_npz
				load_npz(pretrained_model, self)


	def extract(self, x):
		x = self.head(x)
		x = self.mixed00(x)
		x = self.mixed01(x)
		x = self.mixed02(x)
		x = self.mixed03(x)
		x = self.mixed04(x)
		x = self.mixed05(x)
		x = self.mixed06(x)
		x = self.mixed07(x)
		x = self.mixed08(x)
		x = self.mixed09(x)
		x = self.mixed10(x)

		return self.pool(x)

	def __call__(self, x, y=None):
		feat = self.extract(x)
		return self.fc(feat)


	def _load_from_keras(self, weights):
		import h5py
		def _assign(name, param, data):
			assert data.shape == param.shape, \
				"\"{}\" does not match the shape: {} != {}!".format(
					name, data.shape, param.shape)
			if isinstance(param, chainer.variable.Parameter):
				param.data[:] = data
			else:
				param[:] = data


		with h5py.File(weights, "r") as f:
			for name, link in self.namedlinks(skipself=True):
				if name not in chainer_to_keras_mapping: continue
				keras_key = chainer_to_keras_mapping[name]

				if isinstance(link, L.Convolution2D):
					W = np.asarray(f[keras_key][keras_key + "/kernel:0"])
					W = W.transpose(3,2,0,1)

					_assign(name, link.W, W)

				elif isinstance(link, L.Linear):
					W = np.asarray(f[keras_key][keras_key + "/kernel:0"])
					b = np.asarray(f[keras_key][keras_key + "/bias:0"])

					_assign(name, link.W, W.transpose(1,0))
					_assign(name, link.b, b)

				elif isinstance(link, L.BatchNormalization):
					beta = np.asarray(f[keras_key][keras_key + "/beta:0"])
					avg_mean = np.asarray(f[keras_key][keras_key + "/moving_mean:0"])
					avg_var = np.asarray(f[keras_key][keras_key + "/moving_variance:0"])

					_assign(name, link.beta, beta)
					_assign(name, link.avg_mean, avg_mean)
					_assign(name, link.avg_var, avg_var)

				else:
					raise ValueError("Unkown link type: {}!".format(type(link)))


chainer_to_keras_mapping = {
  "/head/conv1/conv": "conv2d_1",
  "/head/conv1/bn": "batch_normalization_1",

  "/head/conv2/conv": "conv2d_2",
  "/head/conv2/bn": "batch_normalization_2",

  "/head/conv3/conv": "conv2d_3",
  "/head/conv3/bn": "batch_normalization_3",

  "/head/conv5/conv": "conv2d_4",
  "/head/conv5/bn": "batch_normalization_4",

  "/head/conv6/conv": "conv2d_5",
  "/head/conv6/bn": "batch_normalization_5",

  "/mixed00/conv1x1/conv": "conv2d_6",
  "/mixed00/conv1x1/bn": "batch_normalization_6",

  "/mixed00/conv5x5_1/conv": "conv2d_7",
  "/mixed00/conv5x5_1/bn": "batch_normalization_7",

  "/mixed00/conv5x5_2/conv": "conv2d_8",
  "/mixed00/conv5x5_2/bn": "batch_normalization_8",

  "/mixed00/conv3x3_1/conv": "conv2d_9",
  "/mixed00/conv3x3_1/bn": "batch_normalization_9",

  "/mixed00/conv3x3_2/conv": "conv2d_10",
  "/mixed00/conv3x3_2/bn": "batch_normalization_10",

  "/mixed00/conv3x3_3/conv": "conv2d_11",
  "/mixed00/conv3x3_3/bn": "batch_normalization_11",

  "/mixed00/pool_conv/conv": "conv2d_12",
  "/mixed00/pool_conv/bn": "batch_normalization_12",


  "/mixed01/conv1x1/conv": "conv2d_13",
  "/mixed01/conv1x1/bn": "batch_normalization_13",

  "/mixed01/conv5x5_1/conv": "conv2d_14",
  "/mixed01/conv5x5_1/bn": "batch_normalization_14",

  "/mixed01/conv5x5_2/conv": "conv2d_15",
  "/mixed01/conv5x5_2/bn": "batch_normalization_15",

  "/mixed01/conv3x3_1/conv": "conv2d_16",
  "/mixed01/conv3x3_1/bn": "batch_normalization_16",

  "/mixed01/conv3x3_2/conv": "conv2d_17",
  "/mixed01/conv3x3_2/bn": "batch_normalization_17",

  "/mixed01/conv3x3_3/conv": "conv2d_18",
  "/mixed01/conv3x3_3/bn": "batch_normalization_18",

  "/mixed01/pool_conv/conv": "conv2d_19",
  "/mixed01/pool_conv/bn": "batch_normalization_19",


  "/mixed02/conv1x1/conv": "conv2d_20",
  "/mixed02/conv1x1/bn": "batch_normalization_20",

  "/mixed02/conv5x5_1/conv": "conv2d_21",
  "/mixed02/conv5x5_1/bn": "batch_normalization_21",

  "/mixed02/conv5x5_2/conv": "conv2d_22",
  "/mixed02/conv5x5_2/bn": "batch_normalization_22",

  "/mixed02/conv3x3_1/conv": "conv2d_23",
  "/mixed02/conv3x3_1/bn": "batch_normalization_23",

  "/mixed02/conv3x3_2/conv": "conv2d_24",
  "/mixed02/conv3x3_2/bn": "batch_normalization_24",

  "/mixed02/conv3x3_3/conv": "conv2d_25",
  "/mixed02/conv3x3_3/bn": "batch_normalization_25",

  "/mixed02/pool_conv/conv": "conv2d_26",
  "/mixed02/pool_conv/bn": "batch_normalization_26",


  "/mixed03/conv3x3/conv": "conv2d_27",
  "/mixed03/conv3x3/bn": "batch_normalization_27",

  "/mixed03/conv3x3_1/conv": "conv2d_28",
  "/mixed03/conv3x3_1/bn": "batch_normalization_28",

  "/mixed03/conv3x3_2/conv": "conv2d_29",
  "/mixed03/conv3x3_2/bn": "batch_normalization_29",

  "/mixed03/conv3x3_3/conv": "conv2d_30",
  "/mixed03/conv3x3_3/bn": "batch_normalization_30",


  "/mixed04/conv1x1/conv": "conv2d_31",
  "/mixed04/conv1x1/bn": "batch_normalization_31",

  "/mixed04/conv7x7_1/conv": "conv2d_32",
  "/mixed04/conv7x7_1/bn": "batch_normalization_32",

  "/mixed04/conv7x7_2/conv": "conv2d_33",
  "/mixed04/conv7x7_2/bn": "batch_normalization_33",

  "/mixed04/conv7x7_3/conv": "conv2d_34",
  "/mixed04/conv7x7_3/bn": "batch_normalization_34",

  "/mixed04/conv7x7x2_1/conv": "conv2d_35",
  "/mixed04/conv7x7x2_1/bn": "batch_normalization_35",

  "/mixed04/conv7x7x2_2/conv": "conv2d_36",
  "/mixed04/conv7x7x2_2/bn": "batch_normalization_36",

  "/mixed04/conv7x7x2_3/conv": "conv2d_37",
  "/mixed04/conv7x7x2_3/bn": "batch_normalization_37",

  "/mixed04/conv7x7x2_4/conv": "conv2d_38",
  "/mixed04/conv7x7x2_4/bn": "batch_normalization_38",

  "/mixed04/conv7x7x2_5/conv": "conv2d_39",
  "/mixed04/conv7x7x2_5/bn": "batch_normalization_39",

  "/mixed04/pool_conv/conv": "conv2d_40",
  "/mixed04/pool_conv/bn": "batch_normalization_40",


  "/mixed05/conv1x1/conv": "conv2d_41",
  "/mixed05/conv1x1/bn": "batch_normalization_41",

  "/mixed05/conv7x7_1/conv": "conv2d_42",
  "/mixed05/conv7x7_1/bn": "batch_normalization_42",

  "/mixed05/conv7x7_2/conv": "conv2d_43",
  "/mixed05/conv7x7_2/bn": "batch_normalization_43",

  "/mixed05/conv7x7_3/conv": "conv2d_44",
  "/mixed05/conv7x7_3/bn": "batch_normalization_44",

  "/mixed05/conv7x7x2_1/conv": "conv2d_45",
  "/mixed05/conv7x7x2_1/bn": "batch_normalization_45",

  "/mixed05/conv7x7x2_2/conv": "conv2d_46",
  "/mixed05/conv7x7x2_2/bn": "batch_normalization_46",

  "/mixed05/conv7x7x2_3/conv": "conv2d_47",
  "/mixed05/conv7x7x2_3/bn": "batch_normalization_47",

  "/mixed05/conv7x7x2_4/conv": "conv2d_48",
  "/mixed05/conv7x7x2_4/bn": "batch_normalization_48",

  "/mixed05/conv7x7x2_5/conv": "conv2d_49",
  "/mixed05/conv7x7x2_5/bn": "batch_normalization_49",

  "/mixed05/pool_conv/conv": "conv2d_50",
  "/mixed05/pool_conv/bn": "batch_normalization_50",


  "/mixed06/conv1x1/conv": "conv2d_51",
  "/mixed06/conv1x1/bn": "batch_normalization_51",

  "/mixed06/conv7x7_1/conv": "conv2d_52",
  "/mixed06/conv7x7_1/bn": "batch_normalization_52",

  "/mixed06/conv7x7_2/conv": "conv2d_53",
  "/mixed06/conv7x7_2/bn": "batch_normalization_53",

  "/mixed06/conv7x7_3/conv": "conv2d_54",
  "/mixed06/conv7x7_3/bn": "batch_normalization_54",

  "/mixed06/conv7x7x2_1/conv": "conv2d_55",
  "/mixed06/conv7x7x2_1/bn": "batch_normalization_55",

  "/mixed06/conv7x7x2_2/conv": "conv2d_56",
  "/mixed06/conv7x7x2_2/bn": "batch_normalization_56",

  "/mixed06/conv7x7x2_3/conv": "conv2d_57",
  "/mixed06/conv7x7x2_3/bn": "batch_normalization_57",

  "/mixed06/conv7x7x2_4/conv": "conv2d_58",
  "/mixed06/conv7x7x2_4/bn": "batch_normalization_58",

  "/mixed06/conv7x7x2_5/conv": "conv2d_59",
  "/mixed06/conv7x7x2_5/bn": "batch_normalization_59",

  "/mixed06/pool_conv/conv": "conv2d_60",
  "/mixed06/pool_conv/bn": "batch_normalization_60",


  "/mixed07/conv1x1/conv": "conv2d_61",
  "/mixed07/conv1x1/bn": "batch_normalization_61",

  "/mixed07/conv7x7_1/conv": "conv2d_62",
  "/mixed07/conv7x7_1/bn": "batch_normalization_62",

  "/mixed07/conv7x7_2/conv": "conv2d_63",
  "/mixed07/conv7x7_2/bn": "batch_normalization_63",

  "/mixed07/conv7x7_3/conv": "conv2d_64",
  "/mixed07/conv7x7_3/bn": "batch_normalization_64",

  "/mixed07/conv7x7x2_1/conv": "conv2d_65",
  "/mixed07/conv7x7x2_1/bn": "batch_normalization_65",

  "/mixed07/conv7x7x2_2/conv": "conv2d_66",
  "/mixed07/conv7x7x2_2/bn": "batch_normalization_66",

  "/mixed07/conv7x7x2_3/conv": "conv2d_67",
  "/mixed07/conv7x7x2_3/bn": "batch_normalization_67",

  "/mixed07/conv7x7x2_4/conv": "conv2d_68",
  "/mixed07/conv7x7x2_4/bn": "batch_normalization_68",

  "/mixed07/conv7x7x2_5/conv": "conv2d_69",
  "/mixed07/conv7x7x2_5/bn": "batch_normalization_69",

  "/mixed07/pool_conv/conv": "conv2d_70",
  "/mixed07/pool_conv/bn": "batch_normalization_70",


  "/mixed08/conv3x3_1/conv": "conv2d_71",
  "/mixed08/conv3x3_1/bn": "batch_normalization_71",

  "/mixed08/conv3x3_2/conv": "conv2d_72",
  "/mixed08/conv3x3_2/bn": "batch_normalization_72",

  "/mixed08/conv7x7_1/conv": "conv2d_73",
  "/mixed08/conv7x7_1/bn": "batch_normalization_73",

  "/mixed08/conv7x7_2/conv": "conv2d_74",
  "/mixed08/conv7x7_2/bn": "batch_normalization_74",

  "/mixed08/conv7x7_3/conv": "conv2d_75",
  "/mixed08/conv7x7_3/bn": "batch_normalization_75",

  "/mixed08/conv7x7_4/conv": "conv2d_76",
  "/mixed08/conv7x7_4/bn": "batch_normalization_76",


  "/mixed09/conv1x1/conv": "conv2d_77",
  "/mixed09/conv1x1/bn": "batch_normalization_77",

  "/mixed09/conv3x3_1/conv": "conv2d_78",
  "/mixed09/conv3x3_1/bn": "batch_normalization_78",

  "/mixed09/conv3x3_2/conv": "conv2d_79",
  "/mixed09/conv3x3_2/bn": "batch_normalization_79",

  "/mixed09/conv3x3_3/conv": "conv2d_80",
  "/mixed09/conv3x3_3/bn": "batch_normalization_80",

  "/mixed09/conv3x3x2_1/conv": "conv2d_81",
  "/mixed09/conv3x3x2_1/bn": "batch_normalization_81",

  "/mixed09/conv3x3x2_2/conv": "conv2d_82",
  "/mixed09/conv3x3x2_2/bn": "batch_normalization_82",

  "/mixed09/conv3x3x2_3/conv": "conv2d_83",
  "/mixed09/conv3x3x2_3/bn": "batch_normalization_83",

  "/mixed09/conv3x3x2_4/conv": "conv2d_84",
  "/mixed09/conv3x3x2_4/bn": "batch_normalization_84",

  "/mixed09/pool_conv/conv": "conv2d_85",
  "/mixed09/pool_conv/bn": "batch_normalization_85",


  "/mixed10/conv1x1/conv": "conv2d_86",
  "/mixed10/conv1x1/bn": "batch_normalization_86",

  "/mixed10/conv3x3_1/conv": "conv2d_87",
  "/mixed10/conv3x3_1/bn": "batch_normalization_87",

  "/mixed10/conv3x3_2/conv": "conv2d_88",
  "/mixed10/conv3x3_2/bn": "batch_normalization_88",

  "/mixed10/conv3x3_3/conv": "conv2d_89",
  "/mixed10/conv3x3_3/bn": "batch_normalization_89",

  "/mixed10/conv3x3x2_1/conv": "conv2d_90",
  "/mixed10/conv3x3x2_1/bn": "batch_normalization_90",

  "/mixed10/conv3x3x2_2/conv": "conv2d_91",
  "/mixed10/conv3x3x2_2/bn": "batch_normalization_91",

  "/mixed10/conv3x3x2_3/conv": "conv2d_92",
  "/mixed10/conv3x3x2_3/bn": "batch_normalization_92",

  "/mixed10/conv3x3x2_4/conv": "conv2d_93",
  "/mixed10/conv3x3x2_4/bn": "batch_normalization_93",

  "/mixed10/pool_conv/conv": "conv2d_94",
  "/mixed10/pool_conv/bn": "batch_normalization_94",

  "/fc": "predictions",

}


if __name__ == '__main__':
	import sys
	pretrained_model = None

	if len(sys.argv) >= 2:
		pretrained_model = sys.argv[1]

	model = InceptionV3(pretrained_model, n_classes=1000)

	model.to_gpu(0)
	var = model.xp.array(np.random.randn(8, 3, 299, 299).astype(np.float32))

	with chainer.using_config("train", False):
		pred = model(var)
	import pdb; pdb.set_trace()


