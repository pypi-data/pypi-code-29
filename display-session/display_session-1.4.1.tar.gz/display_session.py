import shutil


__title__ = "display-session"
__version__ = "1.4.1"
__author__ = "Nicholas Lawrence"
__license__ = "MIT"
__copyright__ = "Copyright 2018-2019 Nicholas Lawrence"


class DisplaySession:
    def __init__(
            self,
            byline,
            byline_actions=[],
            byline_action_delim="//",
            default_ansi="\033[36;40m"
    ):
        """
        Formats input strings using provided color, alignment, and byline arguments. Useful for making engaging CLIs.

        :param byline             : String that will proceed every .print call.
        :param byline_actions     : List of uncalled functions or methods to be called at every .print(). Possible values are datetime.now, psutil.cpu_pct, or other metrics.
        :param byline_action_delim: Char that will seperate byline_actions.
        :param default_ansi       : Default color scheme that only formats the byline and byline actions.
        :param columns            : Integer denoting width of the terminal.
        """

        self.byline              = byline
        self.byline_actions      = byline_actions
        self.byline_action_delim = byline_action_delim
        self.default_ansi        = default_ansi
        self.columns             = 100  # python 2 has limited support to discerning terminal width

        # TODO:
            # progress bars
            # parallelize byline_actions - only in specific cases is this actually not detrimental
            # benchmark compared to regular print

    @staticmethod
    def show_color_palette():
        """https://stackoverflow.com/questions/287871/print-in-terminal-with-colors/3332860"""
        for style in range(8):
            for fg in range(30, 38):
                s1 = ''
                for bg in range(40, 48):
                    fmt = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (fmt, fmt)
                print(s1)

    @staticmethod
    def color_msg(msg, color):
        """
        Encase input string with input ANSI color-code and ANSI color-reset-code.

        :param msg  : Input string
        :param color: ANSI color-code to style input string.

        :return: Input string wrapped with input ANSI color-code. Renders if printed.
        """
        return color + msg + "\033[0m"

    @staticmethod
    def _map_align(align):
        """
        Map human-readable alignment into format required for str.format method.

        :param align: human-readable string (center, left, right)

        :raises: ValueError

        :return: char denoting alignment for str.format method (<, >, ^)
        """
        if align == "center" : return "^"
        elif align == "left" : return "<"
        elif align == "right": return ">"
        else                 : raise ValueError("Entered string must be center, left, or right")

    @staticmethod
    def _pad_msg(msg, align="center"):
        """
        Ensure input string is padded by a single space dependent on the provided alignment. Exists
        to allow for flush left and right alignment and easier readability for center alignment.

        :param msg  : Input string
        :param align: Alignment to terminal (left, center, right)

        :raises: ValueError

        :return: Single space padded string dependent on provided alignment.
        """
        msg = msg.lstrip().rstrip()

        if align == "center" : return " " + msg + " "
        elif align == "right": return " " + msg
        elif align == "left" : return msg + " "
        else                 : raise ValueError("Entered string must be center, left, or right")

    def _align(self, msg, width, align, justify_char):
        """
        Leverage str.format method to pad provided string to provided width with provided char.

        Examples:

            self._align('This is a test', width=1, align='left', justify_char="_")
            This is a test _______________________________________________________

            self._align('This is a test', width=.5, align='right', justify_char="_")
                                                ____________________ This is a test


        :param msg         : Input string
        :param width       : Input width - corresponds to self._evaluate_terminal_width * width
        :param align       : Human-readable string denoting desired alignment method (left, center, right).
        :param justify_char: Desired char to fill provided width.

        :return: String of input text where remaining space is provided char. Orientation of char dependent on alignment.
        """
        template = "{0:{fill}{align}" + str(width) + "}"  # hack for format string to get max
        return template.format(msg, fill=justify_char, align=self._map_align(align))

    def header(self, msg=None, width=1, ansi=None, align="center", justify_char="_"):
        """
        User-facing method that aligns provided text, justifies with provided char, and accepts ANSI color-code.
        Defers to defaults if args not supplied.

        :param msg         : Input string
        :param width       : Input width where 1 is 100% of self.columns.
        :param ansi        : ANSI color-code of input string, does not effect justify_char.
        :param align       : Denotes position of justify char in relation to input text
        :param justify_char: Char used to justify input string to provided width.

        :return: None - Prints fully justified and ANSI-color-coded string.
        """
        ansi         = ansi or self.default_ansi
        align        = align.lower()
        justify_char = justify_char
        prepared_msg = self.color_msg(self._pad_msg(msg, align), ansi) if msg else justify_char
        width        = int(self.columns * width)

        justified_msg = self._align(msg=prepared_msg, width=width, align=align, justify_char=justify_char)

        print(justified_msg)

    def alert(self, msg, status=0):
        """
        Serves as easy way to print an input string with a good/neutral/bad sentiment.

        :param msg   : Input string
        :param status: Numeric flag that determines color of output message (1=good/green, 0=neutral/blue, -1=bad/red)

        :raises: ValueError

        :return: None - prints ANSI-colored input string.
        """
        if status == 1   : ansi = "\033[32m"  # green
        elif status == 0 : ansi = "\033[34m"  # blue
        elif status == -1: ansi = "\033[31m"  # red
        else             : raise ValueError("Entered number must be -1, 0, or 1")

        print(self.color_msg(msg, ansi))

    def report(self, msg):
        """
        Prints input message alongside ANSI-color-coded byline. If instantiation was provided functions or methods
        they are called here.

        :param msg: Input string

        :return: None - Prints ANSI-color-coded byline with any provided functions.
        """
        action_data = self._pad_msg(self.byline_action_delim).join(
            [self._pad_msg(self.byline)] + [str(func()) for func in self.byline_actions]
        )
        byline = self.color_msg(action_data, self.default_ansi) + ":"
        print(" ".join([byline, str(msg)]))
