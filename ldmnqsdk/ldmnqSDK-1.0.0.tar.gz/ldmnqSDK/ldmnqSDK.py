import os, time
from PIL import Image

PATH = os.getcwd()

class LdADB():
    def __init__(self, PATH:"dnplayer.exe 和 adb.exe 存放的目录", picSharePath:"模拟器电脑端共享文件目录"):
        self.PATH = PATH
        self.picSharePath = picSharePath
        self.vmSize()

    def commend(self, cmd):
        return os.popen(f"{self.PATH}\\adb {cmd}")

    def shell(self,msg):
        return os.popen(f"{self.PATH}\\adb shell {msg}")

    def screencap(self, filePath="/sdcard/Pictures/tmp.png")->"PIL.PngImagePlugin.PngImageFile":
        self.commend(f"shell screencap -p {filePath}")
        time.sleep(0.1)
        fileName = filePath.replace('\\', '/').split('/')[-1]
        p = f"{self.picSharePath}\\{fileName}"
        while True:
            try:
                img = Image.open(p)
                break
            except Exception as e:
                if str(e)[:26] == "cannot identify image file":
                    time.sleep(0.1)
                else:
                    raise e
        return img

    def click(self, X, Y):
        '''click base pixel'''
        return self.shell(f"input tap {X} {Y}")

    def click_ratio(self,X:"a float between 0 and 1",Y:"a float between 0 and 1"):
        '''click base ratio,before use this method, confirm your vmSize hasn't changed'''
        return self.shell(f"input tap {X * self.size[0]} {Y * self.size[1]}")

    def input(self,text):
        return self.shell(f'''input text \"{text}\"''')

    def swipe(self,X1,Y1,X2,Y2):
        return self.shell(f'''input swipe {X1} {Y1} {X2} {Y2}''')

    def vmSize(self)->"list[width,height]":
        self.size = [int(x) for x in self.shell("wm size").read().split(":")[-1].split("x")]
        return self.size

    def key(self,k):
        return self.shell(f"input keyevent {k}")
