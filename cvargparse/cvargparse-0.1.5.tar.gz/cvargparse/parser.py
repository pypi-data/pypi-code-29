import argparse, logging

from cvargparse.argument import Argument as Arg
from cvargparse.factory import BaseFactory

class BaseParser(argparse.ArgumentParser):
	def __init__(self, arglist=[], nologging=False, sysargs=None, *args, **kw):
		super(BaseParser, self).__init__(*args, **kw)
		self.__nologging = nologging
		self.__sysargs = sysargs
		if isinstance(arglist, BaseFactory):
			arglist = arglist.get()

		for arg in arglist:
			if isinstance(arg, Arg):
				self.add_argument(*arg.args, **arg.kw)
			else:
				self.add_argument(*arg[0], **arg[1])


		if not self.has_logging: return

		self.add_argument(
			'--logfile', type=str, default='',
			help='file for logging output')

		self.add_argument(
			'--loglevel', type=str, default='INFO',
			help='logging level. see logging module for more information')

		self.__args = None


	@property
	def args(self):
		if self.__args is None:
			self.__args = self.parse_args(self.__sysargs)

		return self.__args


	@property
	def has_logging(self):
		return not self.__nologging

	def init_logger(self, simple=False):
		if not self.has_logging: return
		fmt = '%(message)s' if simple else '%(levelname)s - [%(asctime)s] %(filename)s:%(lineno)d [%(funcName)s]: %(message)s'
		logging.basicConfig(
			format=fmt,
			level=getattr(logging, self.args.loglevel.upper(), logging.DEBUG),
			filename=self.args.logfile or None,
			filemode="w")


class GPUParser(BaseParser):
	def __init__(self, *args, **kw):
		super(GPUParser, self).__init__(*args, **kw)
		self.add_argument(
			"--gpu", "-g", type=int, nargs="+", default=[-1],
			help="which GPU to use. select -1 for CPU only")
