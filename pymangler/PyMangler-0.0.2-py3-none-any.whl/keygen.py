# Generate an encryption key to run with PyMangler
# https://github.com/Wykleph/PyMangler
#


if __name__ == '__main__':
    try:
        from PyMangler.mangle import Encryptor
    except ImportError:
        from .mangle import Encryptor

    def main():
        print('Generating key...')
        s = Encryptor().save_key_file()
        print('Key generated.\nValidating key for prosperity...')

        m = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        en = s.encrypt(m)
        de = s.decrypt(en)

        if de != m:
            print('key:', ''.join(s.characters))
            print('\nstring: {}'.format(len(m)), m)
            print('\nencrypted:', en)
            print('\ndecrypted:', de)

            raise Exception('Decrypted text did not match the encrypted string.  Something went wrong.')

        print('Key is valid.  Encryptor working successfully!')

    main()
