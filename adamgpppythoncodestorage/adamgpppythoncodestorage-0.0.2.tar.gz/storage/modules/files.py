import os
import imghdr


class ExtensionsConstants:
    EXT_JPG = 'jpg'
    EXT_JPEG = 'jpeg'
    EXT_PNG = 'png'
    EXT_SVG = 'svg'
    
    
class Extensions:
    
    IMAGE_FILES_EXTENSIONS = (
        ExtensionsConstants.EXT_JPEG,
        ExtensionsConstants.EXT_JPG,
        ExtensionsConstants.EXT_PNG,
        ExtensionsConstants.EXT_SVG
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
        
        return imghdr.what(self._path) in Extensions.IMAGE_FILES_EXTENSIONS
    
    @property
    def name(self):
        return os.path.basename(self._path)

