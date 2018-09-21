import os


class Environment:
    def __init__(self, bucket_name):
        '''
        Constructor for class Environment.
        Initialize environment used by Lambda script.

        @param bucket_name: String to name bucket
        '''
        if 'development' in bucket_name:
            self.environment = 'development'
        elif 'staging' in bucket_name:
            self.environment = 'staging'
        else:
            self.environment = 'production'


    def name(self):
        '''
        Get name environment used

        >>> Environment('my.bucket.name.for.development').name()
        'development'

        >>> Environment('my.bucket.name.staging').name()
        'staging'

        >>> Environment('my.bucket.name').name()
        'production'
        '''
        return self.environment


    def development(self):
        '''
        Environment development ?

        >>> Environment('my.bucket.name').development()
        False
        '''
        return self.environment == 'development'


    def staging(self):
        '''
        Environment staging ?

        >>> Environment('my.bucket.name.development').staging()
        False
        '''
        return self.environment == 'staging'


    def production(self):
        '''
        Environment production ?

        >>> Environment('my.bucket.name').production()
        True
        '''
        return self.environment == 'production'


    def  get_username(self):
        '''
        Read environment variable for username (email).

        >>> os.environ['USERNAME_DEVE'] = 'roger@dazzl.local'
        >>> os.environ['USERNAME_PROD'] = 'roger@dazzl.tv'
        >>> Environment('my.bucket.name').get_username()
        'roger@dazzl.tv'
        '''
        return os.getenv('USERNAME_{}'.format(self._suffix_env()))


    def get_password(self):
        '''
        Read environment variable for password.

        >>> os.environ['PASSWORD_DEVE'] = 'password-development'
        >>> os.environ['PASSWORD_STAG'] = 'password-staging'
        >>> os.environ['PASSWORD_PROD'] = 'password-production'
        >>> Environment('my.bucket.name.staging').get_password()
        'password-staging'
        '''
        return os.getenv('PASSWORD_{}'.format(self._suffix_env()))


    def get_api_endpoint(self):
        '''
        Read environment variable for API endpoint.

        >>> os.environ['URL_API_DEVE'] = 'https://api.dazzl.local'
        >>> os.environ['URL_API_PROD'] = 'https://api.dazzl.tv'
        >>> Environment('my.bucket.name.development').get_api_endpoint()
        'https://api.dazzl.local'
        '''
        return os.getenv('URL_API_{}'.format(self._suffix_env()))


    def _suffix_env(self):
        '''
        Get suffix for environment used by Lambda script.

        >>> Environment('my.bucket.name.staging')._suffix_env()
        'STAG'
        '''
        if (self.dev()):
            return 'DEVE'
        elif (self.staging()):
            return 'STAG'
        elif (self.prod()):
            return 'PROD'


    # Aliases method
    dev = development
    prod = production


if __name__ == "__main__":
    import doctest
    doctest.testmod(report=False, raise_on_error=True)
