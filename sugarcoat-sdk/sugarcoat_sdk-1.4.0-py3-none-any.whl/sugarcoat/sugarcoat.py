from .endpoints import Endpoint, Endpoint_Second_Level
from .request import Request
from . import config


class Sugarcoat:
	endpoints = {
		"Store": "stores",
		"Product": "products",
		"Basket": "baskets",
		"ProductTypes": "product-types",
		"User": "users",
		"Customer": "customers",
		"Order": "orders",
		"Search": "search",
		"DiscountCodes": "discount_codes"
	}

	endpoints_second_level = {
		"BasketProducts": {'first': 'baskets','second': 'products'},
		"BasketDiscount": {'first': 'baskets','second': 'discount_code'},
		"ProductTypeProducts": {'first': 'product-types', 'second': 'products'},
		"OrderComplete": {'first': 'orders', 'second': 'complete'},
		"OrderFail": {'first': 'orders', 'second': 'fail'}
	}

	def __init__(self, path=None, key=None):
		self.path = path if not None else config.API_PATH
		self.key = key if not None else config.API_KEY
		self.request = Request(self.path, self.key)

	def build_endpoint(self, name, base_object, params={}):
		return type(name, (base_object, object), params)

	def __getattr__(self, name):
		if name in self.endpoints:
			obj = self.build_endpoint(name, Endpoint)
			endpoint = obj(self.request, self.endpoints[name])
		elif name in self.endpoints_second_level:
			obj = self.build_endpoint(name, Endpoint_Second_Level, self.endpoints_second_level[name])
			endpoint = obj(self.request, self.endpoints_second_level[name])
		else:
			raise RuntimeError("No such wrapper: {}".format(name))

		return endpoint