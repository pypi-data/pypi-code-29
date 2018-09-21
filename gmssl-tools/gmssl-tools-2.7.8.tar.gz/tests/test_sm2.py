# -*- coding: utf-8 -*-
import base64
import binascii
from gmssl import sm2, func


if __name__ == '__main__':
    private_key = '82902c35315686baa7f7bc19db4fe5f08e0ab5225787aacb67d78a41d892527d'
    public_key = '04ef39f3391c2d3aeaab6381c176af6edcb48b86cc6e001771eb08009fe4a81937a6cd355604c645e1a4e26b7c00d9269741ff8da25dfa0fa443c7d33df566d02c'

    sm2_crypt = sm2.CryptSM2(
        public_key=public_key, private_key=private_key)
    data = u"!@#123QWEqwe"
    # enc_data = sm2_crypt.encrypt(data)

    enc_data = '798effe3e52eef6fb036c9029f590e4e4252da9c20c1243c93f239e28fba0383d3b055cae5ac1b1543eeafa206f1780bd193ba6c519ec66524c189e7cf20fab8f3c5c922fb07d5cc26df5fd3a36816706bdb626c772fa78d757918b26fe06bc78d1567cacf5326'

    if enc_data.startswith('04') and len(enc_data) >= 208:
        enc_data = enc_data[2: len(enc_data)]
    dec_data = sm2_crypt.decrypt(enc_data)
    print("dec_data:%s" % dec_data)
    assert data == dec_data

    # print("-----------------test sign and verify---------------")
    # random_hex_str = func.random_hex(sm2_crypt.para_len)
    # sign = sm2_crypt.sign(data, random_hex_str)
    # print('sign:%s' % sign)
    # verify = sm2_crypt.verify(sign, data)
    # print('verify:%s' % verify)
    # assert verify
