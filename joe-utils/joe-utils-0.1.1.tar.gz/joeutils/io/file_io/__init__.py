"""File IO."""


def re_readable_read(file):
    """Read file and reset cursor/pointer to allow fast, simple re-read.

    Side Effects:
        Mutates file stream object passed as argument by moving cursor/pointer
        from from position at start of function call and setting it to position
        '0'. If file stream has not been read before calling this function,
        there will be no effective change.

    Returns:
         str: Contents of read file.
    """
    file_contents = file.read()
    file.seek(0)
    return file_contents


def open_and_read(file):
    """Alias: read_contents"""
    read_contents(file)


def read_contents(file):
    """Open file and read it.

    Returns:
        str: File contents.
    """
    # with open(file, 'r') as stream:
    #     return re_readable_read(stream)

    # return re_readable_read(open(file, 'r'))

    return open(file, 'r').read()
