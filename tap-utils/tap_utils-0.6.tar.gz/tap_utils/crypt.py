import base64

from Crypto import Random
from Crypto.Cipher import AES


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key):
    message = pad(bytes(message, encoding="utf-8"))
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    byte_message = iv + cipher.encrypt(message)
    return base64.b64encode(byte_message)


def decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0").decode("utf-8")


key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

uid = "01917749-6133-4216-ad08-90048b451579"

message = {"type": "auth", "uid": uid, "hash": encrypt(uid, key)}

if message.get("uid") == decrypt(message.get("hash"), key):
    print("OK")