from chainer.function import Function
from chainer import cuda

class AlphaProd(Function):
	def __init__(self, eps):
		super(AlphaProd, self).__init__()
		self.eps = eps

	def forward(self, inputs):
		xp = cuda.get_array_module(*inputs)
		x, alpha = inputs
		abs_x = xp.maximum(xp.abs(x), self.eps)
		return xp.sign(x) * xp.power(abs_x, alpha - 1),

	def backward(self, inputs, gys):
		xp = cuda.get_array_module(*inputs)
		x, alpha = inputs
		gy = gys[0]

		abs_x = xp.maximum(xp.abs(x), self.eps)
		sgn_x = xp.sign(x)

		gx = xp.power(abs_x, alpha - 2) * xp.power(sgn_x, 2) * (alpha - 1)
		ga = xp.power(abs_x, alpha - 1) * sgn_x * xp.log(abs_x)

		gx = gx*gy
		ga = (ga*gy).sum().reshape(1)

		return gx, ga


def alpha_prod(x, alpha, eps=1e-5):
	return AlphaProd(eps)(x, alpha)
