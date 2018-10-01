import os, winshell
from win32com.client import Dispatch

path = r"C:\Users\ae\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Launchy.lnk"
target = "G:\My Drive\Launchy\Launchy\Launchy.exe"

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.save()