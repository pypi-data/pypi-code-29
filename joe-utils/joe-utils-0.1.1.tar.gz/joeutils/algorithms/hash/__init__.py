"""Hashing algorithms."""
from string import ascii_letters, digits
from random import choice


def sk_generator(size=24, chars=ascii_letters+digits):
    """Secret key generator."""
    return ''.join(choice(chars) for _ in range(size))
