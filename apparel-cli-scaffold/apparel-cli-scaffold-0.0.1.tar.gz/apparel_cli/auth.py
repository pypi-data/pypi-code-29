import zign.api


def get_auth_headers(app_name: str) -> dict:
    encoded_scopes = ['uid']
    token = zign.api.get_token(app_name, encoded_scopes)
    return {'Authorization': 'Bearer {}'.format(token)}
