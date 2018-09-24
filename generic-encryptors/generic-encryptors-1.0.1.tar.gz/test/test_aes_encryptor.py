import unittest

from generic_encryptors import AesEncryptor
from generic_encryptors.encryptors.exceptions import HmacMissMatch

class TestAesEncryptor(unittest.TestCase):

    def test_aes_encryptor_encode_decode(self):
      encryptor = AesEncryptor(key=('1' * 32).encode('ascii'))
      msg = b'123in0i1n 0in\x10\x00\x00\x00\x94\xd0z\xa6\xac\x95\xb2\xf5\x10\xfa\xd7\x9c\xf9\x9a\x8a\xd5 \x00\x00\x00\x89K\x9bGuxf8|\xf5\x93\xb6-\xbf\xab\xd0\x15\x99\xae}cu\xceWnE\xfdj7\xb3X_hc\xdao>0\x86\xcf\xecSI^\xe5<\xcfh'
      self.assertEqual(msg,
          encryptor.decode(encryptor.encode(msg)))

    def test_aes_encryptor_aborts_on_invalid_hmac_single_char_edit(self):
      encryptor = AesEncryptor(key=('1' * 32).encode('ascii'))
      msg = b'123in0i1n 0in\x10\x00\x00\x00\x94\xd0z\xa6\xac\x95\xb2\xf5\x10\xfa\xd7\x9c\xf9\x9a\x8a\xd5 \x00\x00\x00\x89K\x9bGuxf8|\xf5\x93\xb6-\xbf\xab\xd0\x15\x99\xae}cu\xceWnE\xfdj7\xb3X_hc\xdao>0\x86\xcf\xecSI^\xe5<\xcfh'
      encrypted_msg = encryptor.encode(msg)
      encrypted_msg = encrypted_msg[0:20] + b'a' + encrypted_msg[21:]
      with self.assertRaises(HmacMissMatch) as context:
        encryptor.decode(encrypted_msg)

    def test_aes_encryptor_aborts_on_invalid_hmac_appended_data(self):
      encryptor = AesEncryptor(key=('1' * 32).encode('ascii'))
      msg = b'123in0i1n 0in\x10\x00\x00\x00\x94\xd0z\xa6\xac\x95\xb2\xf5\x10\xfa\xd7\x9c\xf9\x9a\x8a\xd5 \x00\x00\x00\x89K\x9bGuxf8|\xf5\x93\xb6-\xbf\xab\xd0\x15\x99\xae}cu\xceWnE\xfdj7\xb3X_hc\xdao>0\x86\xcf\xecSI^\xe5<\xcfh'
      encrypted_msg = encryptor.encode(msg) + b'a'
      with self.assertRaises(HmacMissMatch) as context:
        encryptor.decode(encrypted_msg)

    def test_aes_encryptor_fails_with_invalid_key(self):
      encryptor1 = AesEncryptor(key=('1' * 32).encode('ascii'))
      encryptor2 = AesEncryptor(key=('2' * 32).encode('ascii'))
      msg = b'123in0i1n 0in\x10\x00\x00\x00\x94\xd0z\xa6\xac\x95\xb2\xf5\x10\xfa\xd7\x9c\xf9\x9a\x8a\xd5 \x00\x00\x00\x89K\x9bGuxf8|\xf5\x93\xb6-\xbf\xab\xd0\x15\x99\xae}cu\xceWnE\xfdj7\xb3X_hc\xdao>0\x86\xcf\xecSI^\xe5<\xcfh'
      encrypted_msg = encryptor1.encode(msg)
      with self.assertRaises(HmacMissMatch) as context:
        encryptor2.decode(encrypted_msg)


    def test_different_aes_encryptors_suceed_with_same_key(self):
      encryptor1 = AesEncryptor(key=('1' * 32).encode('ascii'))
      encryptor2 = AesEncryptor(key=('1' * 32).encode('ascii'))
      msg = b'123in0i1n 0in\x10\x00\x00\x00\x94\xd0z\xa6\xac\x95\xb2\xf5\x10\xfa\xd7\x9c\xf9\x9a\x8a\xd5 \x00\x00\x00\x89K\x9bGuxf8|\xf5\x93\xb6-\xbf\xab\xd0\x15\x99\xae}cu\xceWnE\xfdj7\xb3X_hc\xdao>0\x86\xcf\xecSI^\xe5<\xcfh'
      encrypted_msg = encryptor1.encode(msg)
      self.assertEqual(msg, encryptor2.decode(encrypted_msg))


if __name__ == '__main__':
    unittest.main()