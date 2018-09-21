class Parameters:
    def __init__(self, environment):
        '''
        Constructor for this class.
        Create parameters dict.
        '''
        self.environment = environment


    def token(self):
        '''
        Prepare body for request create token.

        # Used in this way, but not tested because __dict__ are unpredictable on the order
        >>> Parameters(env).token() # doctest: +SKIP
        {'username': 'roger@dazzl.local', 'password': 'yopyopy', 'grant_type': 'password'}

        >>> import os
        >>> from environment import Environment
        >>> os.environ['USERNAME_DEVE'] = 'roger@dazzl.local'
        >>> os.environ['PASSWORD_DEVE'] = 'yopyopy'
        >>> env = Environment('my.bucket.name.development')
        >>> sorted(Parameters(env).token().items())
        [('grant_type', 'password'), ('password', 'yopyopy'), ('username', 'roger@dazzl.local')]

        '''
        return {
            'username': self.environment.get_username(),
            'password': self.environment.get_password(),
            'grant_type': 'password'
        }


    def revoke(self, token):
        '''
        Prepare body for request revoke token.

        # Used in this way, but not tested because __dict__ are unpredictable on the order
        >>> Parameters(env).revoke('SuperToken') # doctest: +SKIP
        {'username': 'roger@dazzl.local', 'password': 'yopyop', 'token': 'SuperToken'}

        >>> import os
        >>> from environment import Environment
        >>> env = Environment('my.bucket.name')
        >>> os.environ['USERNAME_PROD'] = 'roger@dazzl.local'
        >>> os.environ['PASSWORD_PROD'] = 'yopyop'
        >>> sorted(Parameters(env).revoke('SuperToken').items())
        [('password', 'yopyop'), ('token', 'SuperToken'), ('username', 'roger@dazzl.local')]
        '''
        return {
            'username': self.environment.get_username(),
            'password': self.environment.get_password(),
            'token': token
        }


if __name__ == "__main__":
    import doctest
    doctest.testmod(report=False, raise_on_error=True)
