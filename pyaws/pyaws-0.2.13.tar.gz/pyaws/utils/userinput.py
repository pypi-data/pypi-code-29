"""
Python3 Module

Summary:
    User Input Manipulation

"""
from string import ascii_lowercase


def userchoice_mapping(choice):
    """
    Summary:
        Maps the number of an option presented to the user to the
        correct letters in sequential a-z series when choice parameter
        is provided as a number.

        When given a letter as an input parameter (choice is a single
        letter), returns the integer number corresponding to the letter
        in the alphabet (a-z)

        Examples:
            - userchoice_mapping(3) returns 'c'
            - userchoice_mapping('z') returns 26 (integer)
    Args:
        choice, TYPE: int or str
    Returns:
        ascii (lowercase), TYPE: str OR None
    """
    # prepare mapping dict containing all 26 letters
    map_dict = {}
    letters = ascii_lowercase
    for index in range(1, 27):
        map_dict[index] = letters[index - 1]
    # process user input
    try:
        if isinstance(choice, str):
            if choice in letters:
                for k, v in map_dict.items():
                    if v == choice.lower():
                        return k
            elif int(choice) in range(1, 27):
                # integer string provided
                return map_dict[int(choice)]
            else:
                # not in letters or integer string outside range
                return None
        elif choice not in range(1, 27):
            return None
    except KeyError:
        # integer outside range provided
        return None
    except ValueError:
        # string outside range provided
        return None
    return map_dict[choice]
