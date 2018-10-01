class PseudoAuthPolicy(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def authenticated_userid(self, req):
        return self.user_id

    def unauthenticated_userid(self, req):
        return self.user_id

    def effective_principals(self, req):
        return [self.user_id, Authenticated, Everyone]

    def remember(self, request, user_id, **kwargs):
        pass

    def forget(self, req):
        pass



def create_dummy_request(user_id):
    from pyramid.request import Request
    req = Request.blank('/', base_url=get_global_base_url())
    req._get_authentication_policy = lambda: PseudoAuthPolicy(user_id)
    return req

