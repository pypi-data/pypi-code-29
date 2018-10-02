import requests

API_URL = 'https://swiftai-217215.appspot.com'


class ApiError(Exception):
    """Error class for web API related Exceptions"""
    pass


def upload_conda_env(data, name):
    """Upload the anaconda environment to server"""
    files = {'env': ('environment.yml', data)}
    res = requests.post(f'{API_URL}/environment',
                        files=files, data={'name': name})
    if res.status_code == 200:
        res_json = res.json()
        env_hash = res_json['hash']
        return env_hash
    else:
        raise ApiError(f'Evironment upload failed! {res.content}')


def download_conda_env(env_id):
    """Download an anaconda environment to a string"""
    res = requests.get(f'{API_URL}/environment/{env_id}')
    if res.status_code == 200:
        return res.content
    else:
        raise ApiError(f'Environment download failed! {res.content}')
