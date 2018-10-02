#!/usr/bin/python


def string_opp(lst):
    '''Converted single characters from lower case to upper case, or vice versa.

    Args:
        lst: list containing read lines from file.

    Returns:
        lst: list containing converted read lines from file.
    '''
    length_list = len(lst)
    index = 0
    string_list = []
    while index < length_list:
        for char in lst[index]:
            string_list.append(str(char))
        str_len = len(string_list)
        str_index = 0
        while str_index < str_len:
            if string_list[str_index].isupper():
                string_list[str_index] = to_lower(string_list[str_index])
            elif string_list[str_index].islower():
                string_list[str_index] = to_upper(string_list[str_index])
            str_index += 1
        lst[index] = string_list
        string_list = []
        index += 1
    return lst


def to_lower(char):
    '''Convert upper case character to lower case.

    Args:
        char: string character value

    Returns:
        char: converted string character value

    '''
    if char.isupper():
        char = char.lower()
    return char


def to_upper(char):
    '''Convert lower case character to upper case.

    Args:
        char: string character value

    Returns:
        char: converted string character value

    '''
    if char.islower():
        char = char.upper()
    return char
