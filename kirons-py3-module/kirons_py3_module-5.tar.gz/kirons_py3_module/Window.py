import tkinter
from kirons_py3_module import Colors

class Canvas:
    def __init__(self,width,height,parent):
        self.canv = tkinter.Canvas(parent,width=width,height=height)
        self.canv.pack()

    def draw_rect(self,x1,y1,x2,y2,color,outline_color=None):
        if outline_color == None:
            self.canv.create_rectangle(x1,y1,x2,y2,fill=color)
        else:
            self.canv.create_rectangle(x1,y1,x2,y2,fill=color,outline=outline_color)

class Display:
    def __init__(self,width,height,title,resizableX=True,resizableY=True):
        self.size = [width,height]
        self.title = title
        self.root = tkinter.Tk()
        self.root.geometry(str(width)+"x"+str(height))
        self.root.title(self.title)
        self.root.resizable(resizableX, resizableY)
        self.canvas = Canvas(width,height,self.root)
        self.canvas.draw_rect(0,0,width,height,Colors.Black,Colors.Black)
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
        self.canvas = self.display.canvas

    def set_display(self,display):
        self.display = display
        self.canvas = self.display.canvas
