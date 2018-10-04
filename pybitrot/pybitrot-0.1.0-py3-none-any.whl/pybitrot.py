#!/usr/bin/env python

__all__ = [
    'rol8', 'rol16', 'rol32', 'rol64',
    'ror8', 'ror16', 'ror32', 'ror64'
]


def rol8(int_type, offset):
    """rol8(int_type, offset) -> int

    Returns the value of int_type rotated left by (offset mod 8) bits.
    """
    return rol(int_type, 8, offset)


def rol16(int_type, offset):
    """rol16(int_type, offset) -> int

    Returns the value of int_type rotated left by (offset mod 16) bits.
    """
    return rol(int_type, 16, offset)


def rol32(int_type, offset):
    """rol32(int_type, offset) -> int

    Returns the value of int_type rotated left by (offset mod 32) bits.
    """
    return rol(int_type, 32, offset)


def rol64(int_type, offset):
    """rol64(int_type, offset) -> int

    Returns the value of int_type rotated left by (offset mod 64) bits.
    """
    return rol(int_type, 64, offset)


def ror8(int_type, offset):
    """ror8(int_type, offset) -> int

    Returns the value of int_type rotated right by (offset mod 8) bits.
    """
    return ror(int_type, 8, offset)


def ror16(int_type, offset):
    """ror16(int_type, offset) -> int

    Returns the value of int_type rotated right by (offset mod 16) bits.
    """
    return ror(int_type, 16, offset)


def ror32(int_type, offset):
    """ror32(int_type, offset) -> int

    Returns the value of int_type rotated right by (offset mod 32) bits.
    """
    return ror(int_type, 32, offset)


def ror64(int_type, offset):
    """ror64(int_type, offset) -> int

    Returns the value of int_type rotated right by (offset mod 64) bits.
    """
    return ror(int_type, 64, offset)


def rol(int_type, size, offset):
    """rol(int_type, size, offset) -> int

    Returns the value of int_type rotated left by (offset mod size) bits.
    """
    mask = (1 << size) - 1
    offset %= size
    left = (int_type << offset) & mask
    circular = (int_type & mask) >> (size - offset)
    return left | circular


def ror(int_type, size, offset):
    """ror(int_type, size, offset) -> int

    Returns the value of int_type rotated right by (offset mod size) bits.
    """
    mask = (1 << size) - 1
    offset %= size
    right = (int_type & mask) >> offset
    circular = (int_type << (size - offset)) & mask
    return circular | right
