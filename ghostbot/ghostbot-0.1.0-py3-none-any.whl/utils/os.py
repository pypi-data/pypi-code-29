import os
import socket
import shutil
import platform
import hashlib
import string
from tempfile import gettempdir
from urllib.request import urlretrieve
from tempfile import NamedTemporaryFile
from zlib import crc32
from pathlib import Path
from glob import glob
from enum import Enum


class OS(Enum):
    UNKNOWN = "unknown"
    LINUX = "linux"
    MACOS = "macos"
    WINDOWS = "windows"


class Processors(Enum):
    UNKNOWN = "unknown"
    ARM = "arm"
    INTEL = "intel"


class Architectures(Enum):
    UNKNOWN = "unknown"
    ARCH_32 = "32"
    ARCH_64 = "64"


class Computer(object):

    @classmethod
    def name(cls):
        return socket.gethostname()

    @classmethod
    def system(cls):
        return "{}_{}@{}".format(cls.os().value, cls.architecture().value, cls.processor().value)

    @classmethod
    def os(cls):
        system = platform.system().lower()
        if system in ["linux"]:
            result = OS.LINUX
        elif system in ["darwin"]:
            result = OS.MACOS
        elif system in ["windows"]:
            result = OS.WINDOWS
        else:
            result = OS.UNKNOWN
        return result

    @classmethod
    def processor(cls):
        processor = platform.machine().lower()
        if processor in ["arm"]:
            result = Processors.ARM
        elif processor in ["x86_32", "x86_64", "i386", "i686", "AMD64"]:
            result = Processors.INTEL
        else:
            result = Processors.UNKNOWN
        return result

    @classmethod
    def architecture(cls):
        architecture = platform.architecture()[0].lower()
        if architecture in ["32bit"]:
            result = Architectures.ARCH_32
        elif architecture in ["64bit"]:
            result = Architectures.ARCH_64
        else:
            result = Architectures.UNKNOWN
        return result


class FileTypes(Enum):
    FILE = "file"
    LINK = "link"
    DIRECTORY = "directory"
    ANY = "any"


class FileSystem(object):

    @classmethod
    def devnull(cls):
        return os.path.devnull

    @classmethod
    def abspath(cls, path):
        return os.path.abspath(path)

    @classmethod
    def homedir(cls):
        return os.path.expanduser("~")

    @classmethod
    def tempdir(cls, sub_directory=None):
        result = gettempdir()
        if sub_directory:
            result = os.path.join(result, sub_directory)
        if not os.path.exists(result):
            os.mkdir(result, mode=0o777)
        return result

    @classmethod
    def exists(cls, path, file_type=FileTypes.ANY):
        result = False
        if os.path.exists(path):
            if file_type == FileTypes.FILE and os.path.isfile(path):
                result = True
            elif file_type == FileTypes.LINK and os.path.islink(path):
                result = True
            elif file_type == FileTypes.DIRECTORY and os.path.isdir(path):
                result = True
            else:
                result = True
        return result

    @classmethod
    def walk(cls, path, include=None, exclude=None):
        pass

    @classmethod
    def parent(cls, path):
        return Path(path).parent

    @classmethod
    def directory(cls, path):
        return os.path.dirname(path)

    @classmethod
    def file(cls, path):
        return os.path.basename(path)

    @classmethod
    def extension(cls, path):
        return os.path.splitext(path)[1]

    @classmethod
    def join(cls, base, *paths):
        return os.path.join(base, *paths)

    @classmethod
    def make_directory(cls, path, mode=0o777, create_parents=True):
        if create_parents:
            os.makedirs(path, mode, exist_ok=True)
        else:
            os.mkdir(path, mode)

    @classmethod
    def copy_directory(cls, source, destination):
        shutil.copytree(source, destination)

    @classmethod
    def remove_directory(cls, path):
        shutil.rmtree(path)

    @classmethod
    def touch(cls, expression):
        for file in glob(expression):
            Path(file).touch()

    @classmethod
    def copy(cls, expression, destination):
        for file in glob(expression):
            shutil.copy(file, destination)

    @classmethod
    def rename(cls, before, after):
        shutil.move(before, after)

    @classmethod
    def move(cls, expression, destination):
        for file in glob(expression):
            shutil.move(file, destination)

    @classmethod
    def remove(cls, expression):
        for file in glob(expression):
            os.remove(file)


class Hash(object):

    @classmethod
    def digest(cls, data, digit=32):
        return hashlib.md5(data.encode("UTF-8")).hexdigest()[:digit]

    @classmethod
    def base62(cls, number):
        base = string.digits + string.ascii_lowercase + string.ascii_uppercase
        size = len(base)
        encode = []
        while True:
            number, modulo = divmod(number, size)
            encode.append(base[modulo])
            if number == 0:
                break
        return "".join(reversed(encode))

    @classmethod
    def sha1(cls, data):
        return hashlib.sha1(data.encode("UTF-8")).hexdigest()

    @classmethod
    def sha1_file(cls, file):
        return cls._digest(hashlib.sha1(), file)

    @classmethod
    def md5(cls, data):
        return hashlib.md5(data.encode("UTF-8")).hexdigest()

    @classmethod
    def md5_file(cls, file):
        return cls._digest(hashlib.md5(), file)

    @classmethod
    def _digest(cls, algorithm, file):
        with open(file, "rb") as fd:
            for chunk in iter(lambda: fd.read(2048 * algorithm.block_size), b""):
                algorithm.update(chunk)
        return algorithm.hexdigest()

    @classmethod
    def etag(cls, url):
        tmp = NamedTemporaryFile(delete=False)
        tmp.close()
        urlretrieve(url, tmp.name)
        with open(tmp.name, 'rb') as f:
            etag = hashlib.md5(f.read()).hexdigest()
        return etag

    @classmethod
    def crc32_file(cls, file):
        block_size = 65536
        bit_mask = 0xffffffff
        _crc = 0
        with open(file, "rb") as fd:
            for chunk in iter(lambda: fd.read(block_size), b""):
                _crc = crc32(chunk, _crc)
            return format(_crc & bit_mask, "08x")


class Process(object):
    pass
