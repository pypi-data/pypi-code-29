class Formatter:
    """Inherited class with methods called by numerous classes."""
    def __init__(self, info_type, info):
        self.type = info_type
        self.info = info

    def __str__(self):
        return self.create_string()

    def create_string(self):
        lst = [self.type, '------']
        for k, v in self.info().items():
            lst.append(self.format_string(k, v))
        return '\n'.join(lst)

    @staticmethod
    def format_string(key, value):
        return f'{key:16} : {value}'

    @staticmethod
    def format_size(num_bytes, binary=False, strip=True):
        """
        Format a number of bytes as a human readable size.

        Parameters
        ----------
        num_bytes : int
            The size to format.
        binary : bool, optional
            The base to group the number of bytes.
        strip : bool, optional
            If trailing zeros should be keeped or stripped.

        Returns
        -------
        str
            The human readable file size.
        """
        size_units = ['bytes', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

        if binary:
            base = 2 ** 10
        else:
            base = 10 ** 3

        for i, unit in reversed(list(enumerate(size_units))):
            divider = base ** i
            if num_bytes >= divider:
                formatted = '{:0.2f}'.format(num_bytes / divider, unit)
                if strip:
                    formatted = formatted.rstrip('0').rstrip('.')
                formatted = '{} {}'.format(formatted, unit)

                return formatted

        # Failed to match a unit
        return '0 {}'.format(size_units[0])