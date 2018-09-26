# -*- coding: utf-8 -*-

from platform import system as os
import locale
import ctypes


def get_errors():
    if("es" in get_OS().get('lang')):
        help_msg = """
                        __  __                           ______ __     ____
                       / / / /____   _____ ____ _ _____ / ____// /    /  _/
                      / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                     / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                    /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                    Usage:
                    horas -h | --help
                        'Muestra esta ayuda'
                    horas -s | --show
                        'Abre el registro en Chrome si esta instalado o en la linea de comandos'
                    horas -r | --reset
                        'Resetea el registro'
                    horas -n | --new <project name> <hours>
                        'Crea una fila en el registro con el dia de hoy'
                    horas -n | --new <project name> <hours> <date (dd-mm)>
                        'Crea una fila en el registro con el dia que le pasemos'
                    horas -d | --delete
                        'Elimina la ultima fila del registro'
                    """
        chrome_error = """
                            __  __                           ______ __     ____
                           / / / /____   _____ ____ _ _____ / ____// /    /  _/
                          / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                         / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                        /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                        Instala Google Chrome y la extension Markdown Reader para la mejor visualizacion.
                        """
    else:
        help_msg = """
                        __  __                           ______ __     ____
                       / / / /____   _____ ____ _ _____ / ____// /    /  _/
                      / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                     / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                    /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                    Usage:
                    horas -h | --help
                        'Shows this help'
                    horas -s | --show
                        'Opens the schedule in Chrome if exists or as command line'
                    horas -r | --reset
                        'Resets the schedule'
                    horas -n | --new <project name> <hours>
                        'Adds row to the schedule with today date'
                    horas -n | --new <project name> <hours> <date (dd-mm)>
                        'Adds row to the schedule with the given date'
                    horas -d | --delete
                        'Deletes the last row added'
                    """
        chrome_error = """
                            __  __                           ______ __     ____
                           / / / /____   _____ ____ _ _____ / ____// /    /  _/
                          / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                         / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                        /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                        Install Chrome and Markdown Reader extension to get the best visualization.
                        """
    return {'help_msg': help_msg, 'chrome_error': chrome_error}


def get_OS():
    if os() == 'Linux':
        # Linux
        chrome_path = '/usr/bin/google-chrome %s'
        lang = locale.getlocale(locale.LC_MESSAGES)[0]
    elif os() == "Darwin":
        # MacOs
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        lang = locale.getlocale(locale.LC_MESSAGES)[0]
    elif os() == 'Windows':
        # Windows
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        lang = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage(
        )]
    return {'chrome': chrome_path, 'lang': lang}
