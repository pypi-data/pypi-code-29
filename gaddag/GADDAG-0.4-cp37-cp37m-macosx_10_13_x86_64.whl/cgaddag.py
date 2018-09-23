import ctypes
import os

MAX_CHARS = 27

PATH = os.path.dirname(__file__)
cgaddag = ctypes.cdll.LoadLibrary(os.path.join(PATH, "libcgaddag.so"))


class cResult(ctypes.Structure):
    pass

cResult._fields_ = [("str", ctypes.c_char_p),
                    ("next", ctypes.POINTER(cResult))]


class cGADDAG(ctypes.Structure):
    _fields_ = [("cap", ctypes.c_uint),
                ("num_words", ctypes.c_uint),
                ("num_nodes", ctypes.c_uint),
                ("num_edges", ctypes.c_uint),
                ("edges", ctypes.POINTER(ctypes.c_uint)),
                ("letter_sets", ctypes.POINTER(ctypes.c_uint))]


cgaddag.gdg_create.restype = ctypes.POINTER(cGADDAG)

cgaddag.gdg_save.restype = ctypes.c_longlong
cgaddag.gdg_save.argtypes = [ctypes.POINTER(cGADDAG),
                             ctypes.c_char_p]

cgaddag.gdg_save_compressed.restype = ctypes.c_longlong
cgaddag.gdg_save_compressed.argtypes = [ctypes.POINTER(cGADDAG),
                                        ctypes.c_char_p]

cgaddag.gdg_load.restype = ctypes.POINTER(cGADDAG)
cgaddag.gdg_load.argtypes = [ctypes.c_char_p]

cgaddag.gdg_add_word.restype = ctypes.c_void_p
cgaddag.gdg_add_word.argtypes = [ctypes.POINTER(cGADDAG),
                                 ctypes.c_char_p]

cgaddag.gdg_has.restype = ctypes.c_bool
cgaddag.gdg_has.argtypes = [ctypes.POINTER(cGADDAG),
                            ctypes.c_char_p]

cgaddag.gdg_starts_with.restype = ctypes.POINTER(cResult)
cgaddag.gdg_starts_with.argtypes = [ctypes.POINTER(cGADDAG),
                                    ctypes.c_char_p]

cgaddag.gdg_contains.restype = ctypes.POINTER(cResult)
cgaddag.gdg_contains.argtypes = [ctypes.POINTER(cGADDAG),
                                 ctypes.c_char_p]

cgaddag.gdg_ends_with.restype = ctypes.POINTER(cResult)
cgaddag.gdg_ends_with.argtypes = [ctypes.POINTER(cGADDAG),
                                  ctypes.c_char_p]

cgaddag.gdg_edges.restype = ctypes.c_void_p
cgaddag.gdg_edges.argtypes = [ctypes.POINTER(cGADDAG),
                              ctypes.c_uint,
                              ctypes.c_char_p]

cgaddag.gdg_letter_set.restype = ctypes.c_void_p
cgaddag.gdg_letter_set.argtypes = [ctypes.POINTER(cGADDAG),
                                   ctypes.c_uint,
                                   ctypes.c_char_p]

cgaddag.gdg_is_end.restype = ctypes.c_bool
cgaddag.gdg_is_end.argtypes = [ctypes.POINTER(cGADDAG),
                               ctypes.c_uint,
                               ctypes.c_char]

cgaddag.gdg_follow_edge.restype = ctypes.c_uint
cgaddag.gdg_follow_edge.argtypes = [ctypes.POINTER(cGADDAG),
                                    ctypes.c_uint,
                                    ctypes.c_char]

cgaddag.gdg_destroy.restype = ctypes.c_void_p
cgaddag.gdg_destroy.argtypes = [ctypes.POINTER(cGADDAG)]

cgaddag.gdg_destroy_result.restype = ctypes.c_void_p
cgaddag.gdg_destroy_result.argtypes = [ctypes.POINTER(cResult)]

