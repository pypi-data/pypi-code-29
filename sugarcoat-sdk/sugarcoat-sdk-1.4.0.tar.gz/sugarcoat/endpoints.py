class BaseEndpoint(object):

	def __init__(self, request, endpoint):
		self.request = request
		self.endpoint = endpoint


class Endpoint(BaseEndpoint):
	def list(self):
		return self.request.get(self.endpoint)

	def create(self, payload):
		return self.request.post(self.endpoint, payload)

	def read(self, id):
		return self.request.get("{}/{}".format(self.endpoint, id))

	def update(self, id, payload):
		return self.request.put("{}/{}".format(self.endpoint, id), payload)

	def delete(self, id):
		return self.request.delete("{}/{}".format(self.endpoint, id))


class Endpoint_Second_Level(BaseEndpoint):
	def list(self, id):
		return self.request.get("{}/{}/{}".format(self.endpoint['first'], id, self.endpoint['second']))

	def create(self, first_id, second_id, payload):
		return self.request.post("{}/{}/{}/{}".format(self.endpoint['first'], first_id, self.endpoint['second'], second_id), payload)

	def read(self, first_id, second_id):
		return self.request.get("{}/{}/{}/{}".format(self.endpoint['first'], first_id, self.endpoint['second'], second_id))

	def update(self, first_id, second_id, payload):
		return self.request.put("{}/{}/{}/{}".format(self.endpoint['first'], first_id, self.endpoint['second'], second_id), payload)

	def delete(self, first_id, second_id):
		return self.request.delete("{}/{}/{}/{}".format(self.endpoint['first'], first_id, self.endpoint['second'], second_id))