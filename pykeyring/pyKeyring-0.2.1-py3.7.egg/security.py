from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

class DefaultCryptography:

    def __init__(self, password, dependencies):
        self.salt = dependencies
        self.password = password
        if (type(self.password) == str):
            self.password = self.password.encode("utf-8")
        self.key = self.deriveKey()
        self.f = Fernet(self.key)


    @staticmethod
    def generateCryptographyDependencies():
        salt = os.urandom(64)
        return salt
    
    def deriveKey(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(self.password)
        return base64.urlsafe_b64encode(key)

    def encrypt(self, raw_data):
        if (type(raw_data) == str):
            raw_data = raw_data.encode("utf-8")
        return self.f.encrypt(raw_data)

    def decrypt(self, encrypted_data):
        return self.f.decrypt(encrypted_data)

    def hash(self, raw_data):
        return hashes.SHA256(raw_data)