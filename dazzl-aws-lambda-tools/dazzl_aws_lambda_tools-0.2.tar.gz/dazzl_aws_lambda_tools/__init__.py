from .environment import Environment
from .logger import Logger
from .request import Request
from .bucket import Bucket

class Tools:
    def __init__(self, bucket_record):
        '''
        Constructor for this class.
        Initialize environment and level log for lambda function.
        '''
        self.bucket = Bucket(bucket_record)
        self.env = Environment(self.bucket.name())
        self.logger = Logger(self.env)
        self.logger.info_about_lambda(self.env)

        if (self.env.get_api_endpoint() != None):
            self.logger.info_about_requester(self.env)
            self.request = Request(self.env)


    def env(self):
        '''
        Return current environment.
        '''
        return self.env.name


    def bucket_name(self):
        '''
        Return name to bucket used by lambda function
        '''
        return self.bucket.name()


    def bucket_key(self):
        '''
        Return key to event pushed by bucket action.
        '''
        return self.bucket.key()


    def send_request(self, verb, path, body):
        '''
        Send request to API.
        '''
        self.request.send(verb, path, body)
