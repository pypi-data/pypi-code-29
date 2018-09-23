"""
Facility for printing messages to stdout
    - Python3 only
    - Developed & Tested under Python3.6

Message Prefixes:
    - INFO
    - ERROR
    - WARN
    - <any user defined>
"""
import inspect
from pyaws.colors import Colors


def stdout_message(message, prefix='INFO', quiet=False, multiline=False, indent=4, severity=''):
    """
    Summary:
        Prints message to cli stdout while indicating type and severity

    Args:
        :message (str): text characters to be printed to stdout
        :prefix (str):  4-letter string message type identifier.
        :quiet (bool):  Flag to suppress all output
        :multiline (bool): indicates multiline message; removes blank lines
            on either side of printed message
        :indent (int): left justified number of spaces to indent before
            printing message ouput
        :severity (str): header msg determined color instead of prefix

    .. code-block:: python

        # Examples:

            - INFO (default)
            - ERROR (error, problem occurred)
            - WARN (warning)
            - NOTE (important to know)

    Returns:
        TYPE: bool, Success (printed) | Failure (no output)
    """
    prefix = prefix.upper()
    tabspaces = int(indent)

    # prefix color handling
    critical_status = ('ERROR', 'FAIL', 'WTF', 'STOP', 'HALT', 'EXIT', 'F*CK')

    if quiet:

        return True

    elif severity.upper() and prefix not in critical_status:

        print(
            '[%s]: Prefix must be in critical status list: %s' %
            (inspect.stack()[0][3], str(critical_status))
            )
        return False

    else:

        try:

            if prefix in critical_status or severity.upper() == 'CRITICAL':
                header = (Colors.YELLOW + '\t[ ' + Colors.RED + prefix +
                          Colors.YELLOW + ' ]' + Colors.RESET + ': ')

            elif severity.upper() in ('WARN', 'WARNING'):
                header = (Colors.YELLOW + '\t[ ' + Colors.ORANGE + prefix +
                          Colors.YELLOW + ' ]' + Colors.RESET + ': ')

            elif prefix is 'OK' or prefix == 'OK':
                header = (
                        Colors.YELLOW + '\t[  ' + Colors.BOLD + Colors.GREEN + prefix +
                        Colors.YELLOW + '  ]' + Colors.RESET + ': ')

            elif prefix in ('DONE', 'GOOD'):
                header = (Colors.YELLOW + '\t[ ' + Colors.BOLD + Colors.GREEN + prefix +
                          Colors.YELLOW + ' ]' + Colors.RESET + ': ')

            else:    # default color scheme
                header = (Colors.YELLOW + '\t[ ' + Colors.DARKCYAN + prefix +
                          Colors.YELLOW + ' ]' + Colors.RESET + ': ')

            if multiline:
                print(header.expandtabs(tabspaces) + str(message))
            else:
                print('\n' + header.expandtabs(tabspaces) + str(message) + '\n')

        except Exception as e:
            print(f'{inspect.stack()[0][3]}: Problem sending msg to stdout: {e}')
            return False
            
    return True
