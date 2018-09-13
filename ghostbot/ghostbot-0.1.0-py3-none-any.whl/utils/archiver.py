import zipfile
import tarfile


class ZipArchive(object):

    @classmethod
    def compress(cls, file, targets):
        archive = zipfile.ZipFile(file, "w", zipfile.ZIP_DEFLATED)
        for target in targets:
            archive.write(target)
        archive.close()

    @classmethod
    def decompress(cls, file, destination):
        with zipfile.ZipFile(file, "r") as archive:
            archive.extractall(destination)


class TarArchive(object):

    @classmethod
    def compress(cls, file, targets):
        archive = tarfile.open(file, mode="w:gz")
        for target in targets:
            archive.add(target)
        archive.close()

    @classmethod
    def decompress(cls, file, destination):
        with tarfile.open(file) as archive:
            archive.extractall(destination)
