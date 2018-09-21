import os

from .acnt import File, FileMeta, MagicMethodsMeta

__all__ = 'MiniStorageMeta', 'MiniStorage'


class MiniStorageMeta(FileMeta, MagicMethodsMeta):
    def __init__(cls, name, parents, attrs):
        super(FileMeta, cls).__init__(name, parents, attrs)
        super(MagicMethodsMeta, cls).__init__(name, parents, attrs)


class MiniStorage(File, metaclass=MiniStorageMeta):
    def __key__(self):
        return self.data

    def __init__(self, path, data=None, read=True):
        super().__init__()
        self._path = path
        self.data = data
        if os.path.exists(path) and read:
            self.file = open(path, 'r+', encoding='utf-8')
            self.read()
        elif data is not None:
            open(path, 'w').close()
            self.file = open(path, 'r+', encoding='utf-8')
            self.data = data
            self.save()

    def __del__(self):
        try:
            self.file.close()
        except (NameError, AttributeError):
            pass

    def delete_file(self):
        self.file.close()
        os.remove(self.file.name)

    def read(self, path=None):
        if path is None:
            data = self.file.read()
            self.loads(data)
        else:
            file = open(path, 'r', encoding='utf-8')
            self.loads(file.read())
            file.close()

    def loads(self, data: str):
        if bytes(data[0], encoding='utf-8') == b'\xef\xbb\xbf':
            data = data[1:]
        self.data = eval(data)

    def save(self, path=None):
        if path is None:
            self.file.seek(0)
            self.file.truncate()
            self.file.write(self.dumps())
            self.file.read()
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.dumps())

    def dumps(self, data=None):
        if data is None:
            return repr(self.data)
        else:
            return repr(data)
