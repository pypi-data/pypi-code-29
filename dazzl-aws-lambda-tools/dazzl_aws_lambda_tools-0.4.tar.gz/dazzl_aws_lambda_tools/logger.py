import logging
import os

class Logger:
    def __init__(self, environment):
        '''
        Constructor for class Logger.
        Initialize logger used by Lambda script.

        Example without LOG_LEVEL variable environment :
            >>> from environment import Environment
            >>> env = Environment('my.bucket.name.staging')
            >>> Logger(env).level
            20

        Example with LOG_LEVEL variable environment :
            >>> from environment import Environment
            >>> os.environ['LOG_LEVEL'] = 'CRITICAL'
            >>> env = Environment('my.bucket.name.staging')
            >>> Logger(env).level
            50
        '''
        if (os.getenv('LOG_LEVEL')):
            self.level = self.eval_log_level()
        else:
            if environment.dev():
                self.level = logging.DEBUG
            elif environment.staging():
                self.level = logging.INFO
            elif environment.prod():
                self.level = logging.ERROR

        self.log = logging.getLogger()
        self.log.setLevel(self.level)


    def eval_log_level(self):
        '''
        Transform string in logging level.

        >>> from environment import Environment
        >>> os.environ['LOG_LEVEL'] = 'DEBUG'
        >>> env = Environment('my.bucket.name.staging')
        >>> Logger(env).eval_log_level()
        10
        '''
        return eval('logging.{}'.format(os.getenv('LOG_LEVEL').upper()))


    def info_about_lambda(self, env):
        '''
        Write info in log to lambda (cloudwatch)
        '''
        self.log.log(self.level,
                     'Environment [{}] and logger [{}] configured, ' \
                     'execute Lambda function.'.format(env.name(),
                                                       logging.getLevelName(self.level)))


    def info_about_requester(self, env):
        '''
        Write info about requester configured
        '''
        self.log.log(self.level,
                     'URL API Endpoint configured [{}] with user [{}]'
                     .format(env.get_api_endpoint(), env.get_username()))


if __name__ == "__main__":
    import doctest
    doctest.testmod(report=False, raise_on_error=True)
