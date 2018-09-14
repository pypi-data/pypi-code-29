import os
import webbrowser


class weby:
    def __init__(self):
        self.titleElement = ""
        self.fractionOneHTML = "<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible' content='ie=edge'><title id='title'></title><link rel='stylesheet' href='style.css'></head><body>"
        self.fractionTwoHTML = "</body>"
        fileHTMLname = "index.html"
        fileCSSname = "style.css"
        # erasing contents
        fileHTML = open(fileHTMLname, "w")
        fileHTML.write("")
        fileHTML.close()
        # writing fraction one
        self.fileHTML = open(fileHTMLname, "a+")
        self.fileHTML.write(self.fractionOneHTML)
        # erasing contents
        fileCSS = open(fileCSSname, "w")
        fileCSS.write("")
        fileCSS.close()
        # reopening
        self.fileCSS = open(fileCSSname, "a+")
    def writeText(self, text, color="", size="", weight=""):
        element = "<span style='"
        if color != "":
            element = element + "color:" + color + ";"
        if size != "":
            element = element + "font-size:" + size + ";"
        if weight != "":
            element = element + "font-weight:" + weight + ";"
        element = element + "'>" + text + "</span>"
        self.fileHTML.write(element)
    def setBG(self, color):
        element = "body {background-color: "
        element = element + color
        element = element + ";}"
        self.fileCSS.write(element)
    def setTitle(self, title):
        self.titleElement = "<script>document.getElementById('title').innerHTML = '"
        self.titleElement = self.titleElement + title
        self.titleElement = self.titleElement + "';</script>"
    def setFrame(self, src, height=None, width=None):
        element = "<iframe src='"
        element = element + src
        element = element + "' style='"
        if height != None:
            element = element + "height: "
            element = element + height
            element = element + ";"
        if width != None:
            element = element + "width: "
            element = element + width
            element = element + ";"
        element = element + "'></iframe>"
        self.fileHTML.write(element)
    def makeImage(self, src, height=None, width=None):
        element = "<img src='"
        element = element + src
        element = element + "' style='"
        if height != None:
            element = element + "height: "
            element = element + height
            element = element + ";"
        if width != None:
            element = element + "width: "
            element = element + width
            element = element + ";"
        element = element + "'>"
        self.fileHTML.write(element)
    def makeLink(self, address, text=""):
        element = "<a href='"
        element = element + address
        element = element + "'>"
        element = element + text
        element = element + "</a>"
        self.fileHTML.write(element)
    def Line(self):
        self.fileHTML.write("<br><br>")
    def mainloop(self):
        self.fileHTML.write(self.titleElement)
        self.fileHTML.write(self.fractionTwoHTML)
        webbrowser.open('file://' + os.path.realpath("index.html"), new=1)
        # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('file://' + os.path.realpath("index.html"), new=1)
