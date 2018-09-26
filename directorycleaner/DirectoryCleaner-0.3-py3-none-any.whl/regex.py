import os
import re

def dir_regex(name):
    """
    Regex to check if there is a duplicate folder already.
    """
    pattern = re.compile(r"^\(\d+\).+")
    match = pattern.search(name)
    return match


def check_duplicate(txt, directory):
    """
    Checks for any duplicate folders. First checks to see if
    there is a regex match which must mean there is a folder with
    (digit) already so it will loop through until there isn't.
    If the regex check doesn't pass the first time then we can
    prepend the folder/file with (1).
    """
    while True:
        if os.path.exists(os.path.join(directory, txt)):
            match = dir_regex(txt)
            if match is not None:
                 positions = (txt.find("("), txt.find(")"))
                 num = txt[positions[0] + 1 : positions[1]]
                 num = int(num)
                 num += 1
                 num = str(num)
                 txt = "(" + num + ")" + txt[positions[1] + 1:]
            else:
                txt = "(1)" + txt
        else:
            break
    return txt
