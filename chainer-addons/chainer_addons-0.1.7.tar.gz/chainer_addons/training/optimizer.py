from enum import Enum, EnumMeta
import chainer
from chainer.optimizers import MomentumSGD, Adam, RMSprop
from chainer.training import extensions

class BaseTypeMeta(EnumMeta):
	def __contains__(cls, item):
		if isinstance(item, str):
			return item.lower() in cls.as_choices()
		else:
			return super(BaseTypeMeta, cls).__contains__(item)

	def __getitem__(cls, key):
		return cls.as_choices()[key.lower()]

class BaseType(Enum, metaclass=BaseTypeMeta):
	@classmethod
	def as_choices(cls):
		return {e.name.lower(): e for e in cls}

	@classmethod
	def get(cls, key):
		if isinstance(key, str):
			return cls[key] if key in cls else cls.Default
		elif isinstance(key, cls):
			return key
		else:
			raise ValueError("Unknown optimizer type: \"{}\"".format(key.__class__.__name__))

class OptimizerType(BaseType):
	SGD = MomentumSGD
	RMSPROP = RMSprop
	ADAM = Adam
	Default = SGD

def optimizer(opt_type_name, model, lr=1e-2, decay=5e-3, *args, **kw):
	opt_type = OptimizerType.get(opt_type_name)
	opt_args = dict(alpha=lr) if opt_type == OptimizerType.ADAM else dict(lr=lr)
	kw.update(opt_args)
	opt = opt_type.value(*args, **kw)
	opt.setup(model)
	if decay:
		opt.add_hook(chainer.optimizer.WeightDecay(decay))
	return opt

def lr_shift(opt, init, rate, target):
	attr = "alpha" if isinstance(opt, Adam) else "lr"

	return extensions.ExponentialShift(
		optimizer=opt, attr=attr,
		init=init, rate=rate, target=target)

def no_grad(arr):
	return arr.data if isinstance(arr, chainer.Variable) else arr

if __name__ == '__main__':
	print(optimizer("adam", chainer.Chain()))
