import jwt
from flask import request

from diku_tools.diku_tools.canvas_session import CanvasSession
from diku_tools.diku_tools.encryption import AESCipher

jwt_secret = "Not very secret"
login_secret = "Not very secret!"


def get_user():
    jwt_token = request.headers["Auth"]
    user = jwt.decode(jwt_token, jwt_secret)
    cipher = AESCipher(login_secret)

    return {
        "username": cipher.decrypt(user["usr"]),
        "password": cipher.decrypt(user["psw"]),
        "token": user["tkn"]
    }


def get_session():
    user = get_user()
    return CanvasSession(**user)
