from tinydb.storages import Storage
from security import DefaultCryptography
import os
import json

class SecureStorage(Storage):

    def __init__(self, filename, password):
        if (os.path.isfile(filename)):
            self.file = open(filename, "rb+")


            self.header_length = int.from_bytes(self.file.read(2), byteorder='big')
            crypt_dependencies = self.file.read(self.header_length)


            self.cript = DefaultCryptography(password, crypt_dependencies)

            #Try to decrypt
            self.file.seek(2+self.header_length)
            self.cript.decrypt(self.file.read()).decode("utf-8")

        else:
            raise FileNotFoundError("Database file not found")

    @staticmethod
    def create(filename, password):
        if (os.path.isfile(filename)):
            raise Exception("Database file already exists")
        else:
            with open(filename, 'wb+') as file:
                crypt_dependencies = DefaultCryptography.generateCryptographyDependencies()
                cript = DefaultCryptography(password, crypt_dependencies)

                length_bytes = len(crypt_dependencies).to_bytes(2, byteorder='big') #2 bytes
                file.write(length_bytes)
                file.write(crypt_dependencies)
                
                data = cript.encrypt('{}')
                file.write(data)

    
    def read(self):
        self.file.seek(2+self.header_length)
        #import pdb;pdb.set_trace() 
        data = self.cript.decrypt(self.file.read()).decode("utf-8")
        
        return json.loads(data)

    def write(self, data):
        self.file.seek(2+self.header_length)
        crypted = self.cript.encrypt(json.dumps(data).encode("utf-8"))
        self.file.write(crypted)
        self.file.flush()
        os.fsync(self.file.fileno())
        self.file.truncate()

    def close(self):
        self.file.close()
        