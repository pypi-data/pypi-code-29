def compose_headers(token):
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Token {}'.format(token),
    }
