import re

import numpy


code_label = [
    ('O', 0),
    ('N', 0), ('N', 1),
    ('V', 0), ('V', 1),
    ('M', 0), ('M', 1),
    ('E', 0), ('E', 1),
    ('I', 0), ('I', 1),
    ('J', 0), ('J', 1),
    ('S', 0), ('S', 1),
    ('U', 0), ('U', 1),
    ('X', 0), ('X', 1)
]


ascii_code = {
    ' ': 0,
    '!': 1,
    '"': 2,
    '#': 3,
    '$': 4,
    '%': 5,
    '&': 6,
    '\'': 7,
    '(': 8,
    ')': 9,
    '*': 10,
    '+': 11,
    ',': 12,
    '-': 13,
    '.': 14,
    '/': 15,
    '0': 16,
    '1': 16,
    '2': 16,
    '3': 16,
    '4': 16,
    '5': 16,
    '6': 16,
    '7': 16,
    '8': 16,
    '9': 16,
    ':': 17,
    ';': 18,
    '<': 19,
    '=': 20,
    '>': 21,
    '?': 22,
    '@': 23,
    'A': 24,
    'B': 24,
    'C': 24,
    'D': 24,
    'E': 24,
    'F': 24,
    'G': 24,
    'H': 24,
    'I': 24,
    'J': 24,
    'K': 24,
    'L': 24,
    'M': 24,
    'N': 24,
    'O': 24,
    'P': 24,
    'Q': 24,
    'R': 24,
    'S': 24,
    'T': 24,
    'U': 24,
    'V': 24,
    'W': 24,
    'X': 24,
    'Y': 24,
    'Z': 24,
    '[': 25,
    '\\': 26,
    ']': 27,
    '^': 28,
    '_': 29,
    '`': 30,
    'a': 24,
    'b': 24,
    'c': 24,
    'd': 24,
    'e': 24,
    'f': 24,
    'g': 24,
    'h': 24,
    'i': 24,
    'j': 24,
    'k': 24,
    'l': 24,
    'm': 24,
    'n': 24,
    'o': 24,
    'p': 24,
    'q': 24,
    'r': 24,
    's': 24,
    't': 24,
    'u': 24,
    'v': 24,
    'w': 24,
    'x': 24,
    'y': 24,
    'z': 24,
    '{': 31,
    '|': 32,
    '}': 33,
    '~': 34,
}


HANGUL_START_CODE = ord('가')

NUM_HANGUL_INITIALS = 19
NUM_HANGUL_VOWELS = 21
NUM_HANGUL_FINALS = 28
NUM_NON_HANGUL = max(ascii_code.values()) + len([' ', '\w', '\W'])
NUM_ALL_LETTER = (NUM_NON_HANGUL +
                  NUM_HANGUL_INITIALS +
                  NUM_HANGUL_VOWELS +
                  NUM_HANGUL_FINALS)


def decompose_hangul(hangul_code):
    code = hangul_code - HANGUL_START_CODE
    final = int(code % NUM_HANGUL_FINALS)
    code /= NUM_HANGUL_FINALS
    vowel = int(code % NUM_HANGUL_VOWELS)
    code /= NUM_HANGUL_VOWELS
    initial = int(code)

    return 0, initial + 1, vowel + 1, final


char_re = re.compile('\w')


def codify_letter(letter):
    code = ord(letter)

    if '가' <= letter <= '힣':
        idx = decompose_hangul(code)
    elif letter in ascii_code:
        idx = ascii_code[letter], 0, 0, 0
    elif char_re.match(letter):
        idx = 35, 0, 0, 0
    else:
        idx = 36, 0, 0, 0

    return (
        idx[0],
        idx[1] + NUM_NON_HANGUL,
        idx[2] + NUM_NON_HANGUL + NUM_HANGUL_INITIALS,
        idx[3] + NUM_NON_HANGUL + NUM_HANGUL_INITIALS + NUM_HANGUL_VOWELS)


def texts_to_matrix(texts):
    """
    Convert texts into a matrix
    """
    n = len(texts)
    x = numpy.zeros((n, 100, NUM_ALL_LETTER))
    for i, text in enumerate(texts):
        for j, letter in enumerate(text):
            k = codify_letter(letter)
            x[i, j, k] = 1
    return x
