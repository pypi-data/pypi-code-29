import tkinter

class Display:
    def __init__(self,width,height,title,resizableX=True,resizableY=True):
        self.size = [width,height]
        self.title = title
        self.root = tkinter.Tk()
        self.root.geometry(str(width)+"x"+str(height))
        self.root.title(self.title)
        self.root.resizable(resizableX, resizableY)
        self.hide()

    def update(self):
        self.root.update()

    def show(self):
        self.update()
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()

class init:
    def __init__(self):
        self.display = Display(640,480,"kirons_py3_module")

    def set_display(self,display):
        self.display = display
