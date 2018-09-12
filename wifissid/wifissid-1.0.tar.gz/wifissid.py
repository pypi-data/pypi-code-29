import subprocess
#rom subprocess import check_output
import sys
def __subprocess_check_output__(*args, **kwargs):
    #also works for Popen. It creates a new *hidden* window, so it will work in frozen apps (.exe).
    IS_WIN32 = 'win32' in str(sys.platform).lower()
    if IS_WIN32:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        kwargs['startupinfo'] = startupinfo
    retcode = subprocess.check_output(*args, **kwargs)
    return retcode

def showssid():
    x=__subprocess_check_output__("netsh WLAN show interfaces")
    x=x.decode(encoding='iso-8859-1')
    x=x.split()
    y=x.index('SSID')
    return x[y+2]
