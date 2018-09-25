import os
import imghdr


class Extensions:

    EXT_JPG = 'jpg'
    EXT_JPEG = 'jpeg'
    EXT_PNG = 'png'
    EXT_SVG = 'svg'

    GROUP_TYPE_IMAGE = (
        EXT_JPEG,
        EXT_JPG,
        EXT_PNG,
        EXT_SVG,
    )


class File:

    def __init__(self, path, raise_exception=True):
        self._path = path
        self._raise_exception = raise_exception

        if not self.exists():
            if self._raise_exception:
                raise Exception('File does not exist!')
            else:
                return None

    def exists(self):
        return self.is_file or self.is_symlink

    @property
    def path(self):
        return self._path

    @property
    def is_file(self):
        return os.path.isfile(self._path)

    @property
    def is_symlink(self):
        return os.path.islink(self._path)

    @property
    def is_image(self):
        if not self.exists():
            return False

        return imghdr.what(self._path) in Extensions.GROUP_TYPE_IMAGE

    @property
    def name(self):
        return os.path.basename(self._path)
