import requests


def buscar_avatar(ususario):
    """
    Busca o avatar de um usuário no Github

    :param ususario: str com o nome de usuário no github
    :return: str com o link do avatar
    """

    url = f'https://api.github.com/users/{ususario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('fredericoaraujo'))
