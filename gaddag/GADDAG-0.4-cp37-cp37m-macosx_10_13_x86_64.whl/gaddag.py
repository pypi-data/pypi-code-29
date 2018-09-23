import ctypes
import os
import shutil
import tempfile

from .cgaddag import cgaddag
from .node import Node

class GADDAG():
    """
    A data structure allowing for extremely fast prefix, suffix and substring
    searching of words.
    """
    def __init__(self, words=None):
        """
        Create a new GADDAG, optionally adding `words` to it.
        """
        self.gdg = cgaddag.gdg_create().contents

        if words:
            if type(words) is str:
                raise TypeError("Input must be an iterable of strings")

            for word in words:
                self.add_word(word)

    def __len__(self):
        """
        Total number of words contained in the GADDAG.
        """
        return self.gdg.num_words

    def __contains__(self, word):
        """
        Check if `word` is contained in the GADDAG.
        """
        word = word.lower()

        return cgaddag.gdg_has(self.gdg, word.encode(encoding="ascii"))

    def __iter__(self):
        """
        Iterate over all words contained in the GADDAG.
        """
        for word in self.ends_with(""):
            yield word

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        if len(self) != len(other):
            return False

        return self.root == other.root

    def __del__(self):
        """
        Free the memory allocated to the internal cGADDAG.
        """
        cgaddag.gdg_destroy(self.gdg)

    @property
    def root(self):
        """
        Returns the root node of the GADDAG.
        """
        return Node(self.gdg, 0)

    def save(self, path, compressed=True, exist_ok=False):
        """
        Save the GADDAG to file.

        Args:
            path: path to save the GADDAG to.
            compressed: compress the saved GADDAG using gzip.
            exist_ok: overwrite existing file at `path`.
        """
        path = os.path.expandvars(os.path.expanduser(path))
        if os.path.isfile(path) and not exist_ok:
            raise OSError(17, os.strerror(17), path)

        if os.path.isdir(path):
            path = os.path.join(path, "out.gdg")

        if compressed:
            bytes_written = cgaddag.gdg_save_compressed(self.gdg, path.encode("ascii"))
        else:
            bytes_written = cgaddag.gdg_save(self.gdg, path.encode("ascii"))

        if bytes_written == -1:
            errno = ctypes.c_int.in_dll(ctypes.pythonapi, "errno").value
            raise OSError(errno, os.strerror(errno), path)

        return bytes_written

    def load(self, path):
        """
        Load a GADDAG from file, replacing the words currently in this GADDAG.

        Args:
            path: path to saved GADDAG to be loaded.
        """
        path = os.path.expandvars(os.path.expanduser(path))

        gdg = cgaddag.gdg_load(path.encode("ascii"))
        if not gdg:
            errno = ctypes.c_int.in_dll(ctypes.pythonapi, "errno").value
            raise OSError(errno, os.strerror(errno), path)

        self.__del__()
        self.gdg = gdg.contents

    def starts_with(self, prefix):
        """
        Find all words starting with a prefix.

        Args:
            prefix: A prefix to be searched for.

        Returns:
            A list of all words found.
        """
        prefix = prefix.lower()
        found_words = []

        res = cgaddag.gdg_starts_with(self.gdg, prefix.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.append(word)
            tmp = tmp.contents.next

        cgaddag.gdg_destroy_result(res)
        return found_words

    def contains(self, sub):
        """
        Find all words containing a substring.

        Args:
            sub: A substring to be searched for.

        Returns:
            A list of all words found.
        """
        sub = sub.lower()
        found_words = set()

        res = cgaddag.gdg_contains(self.gdg, sub.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.add(word)
            tmp = tmp.contents.next

        cgaddag.gdg_destroy_result(res)
        return list(found_words)

    def ends_with(self, suffix):
        """
        Find all words ending with a suffix.

        Args:
            suffix: A suffix to be searched for.

        Returns:
            A list of all words found.
        """
        suffix = suffix.lower()
        found_words = []

        res = cgaddag.gdg_ends_with(self.gdg, suffix.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.append(word)
            tmp = tmp.contents.next

        cgaddag.gdg_destroy_result(res)
        return found_words

    def add_word(self, word):
        """
        Add a word to the GADDAG.

        Args:
            word: A word to be added to the GADDAG.
        """
        word = word.lower()

        if not (word.isascii() and word.isalpha()):
            raise ValueError("Invalid character in word '{}'".format(word))

        word = word.encode(encoding="ascii")
        result = cgaddag.gdg_add_word(self.gdg, word)
        if result == 1:
            raise ValueError("Invalid character in word '{}'".format(word))
        elif result == 2:
            raise MemoryError("Out of memory, GADDAG is in an undefined state")


def load(path):
    """
    Load a GADDAG from file.

    Args:
        path: path to saved GADDAG to be loaded.

    Returns:
        Loaded GADDAG.
    """
    gdg = GADDAG()
    gdg.load(path)

    return gdg

