# -*- coding: UTF-8 -*-
"""
A simple TkInter/Qt popup with customizable title that displays text. 

The dialog also displays a button for launching a simulation. 
"""
import sys, platform, subprocess

try:
	from PyQt5.QtWidgets import *
	from PyQt5.QtGui import *
	from PyQt5.QtCore import *
	toolkit="Qt"
except:
	try:
		from tkinter import *
		from tkinter.ttk import Frame, Label, Entry, Button
		toolkit="Tkinter"
	except:
		toolkit=None

	
__all__ = [ "popup" ]

if toolkit == "Tkinter":
	class MessageBox(Frame):
		def __init__(
			self, root, title, message, 
			simulator=None, simulatorFile=None, 
		):
			self.title = title
			self.message = message
			self.root = root
			self.simulator=simulator
			self.simulatorFile=simulatorFile
			
			super().__init__()   
			self.initUI()
			
		def initUI(self):
	
			self.master.title(self.title)
			self.pack(fill=BOTH, expand=True)

			frame1 = Frame(self)
			frame1.pack(side=TOP, fill=BOTH, expand=True)
			
			frame2 = Frame(self)
			frame2.pack(side=TOP, expand=False)
			
			vscroll=Scrollbar(frame1)
			vscroll.pack(side=RIGHT, fill=Y)
			
			hscroll=Scrollbar(frame1, orient=HORIZONTAL)
			hscroll.pack(side=BOTTOM, fill=X)
			
			txt = Text(frame1, wrap=NONE)
			txt.configure(font='monospace 10')
			txt.pack(side=TOP, fill=BOTH, expand=True, pady=5, padx=5)
			txt.insert(END, self.message)
			txt.config(state=DISABLED)
			
			ok = Button(frame2, text="Close", command=self.close)
			ok.pack(side=LEFT, fill=Y, expand=False, anchor=CENTER, padx=10)
			ok.focus_set()
			self.master.bind("<Escape>", self.close)
			
			if self.simulator is not None and self.simulatorFile is not None:
				lnch = Button(frame2, text="Simulate", command=self.launch)
				lnch.pack(side=LEFT, fill=Y, expand=False, anchor=CENTER, padx=10)
				lnch.focus_set()
				self.master.bind("s", self.launch)
				self.master.bind("<Return>", self.launch)
				
			hscroll.config(command=txt.xview)
			vscroll.config(command=txt.yview)
			
			txt['yscrollcommand'] = vscroll.set
			txt['xscrollcommand'] = hscroll.set
			
		def close(self, event=None):
			self.root.destroy()
		
		def launch(self, event=None):
			if self.simulator is not None and self.simulatorFile is not None:
				if self.simulator=="SpiceOpus":
					from ..simulator.spiceopus import SpiceOpus
					sim=SpiceOpus.findSimulator()
					if sim is not None:
						p=subprocess.Popen(
							[sim, self.simulatorFile], 
						)
			self.root.destroy()
		
	def popup(title, text, simulator=None, simulatorFile=None, error=False):
		root = Tk()
		app = MessageBox(root, title, text, simulator, simulatorFile)
		root.geometry("640x480")
		root.mainloop()  

elif toolkit == "Qt":
	class PopupWidget(QWidget):
		def __init__(
			self, title="KiCad netlister", message="", 
			simulator=None, simulatorFile=None, 
			parent=None, *args
		):
			QWidget.__init__(self, parent)
			
			self.title=title
			self.message=message
			self.simulator=simulator
			self.simulatorFile=simulatorFile
			
			vl=QVBoxLayout(self)
			
			self.txt=QPlainTextEdit(self)
			self.txt.setPlainText(self.message)
			self.txt.setReadOnly(True)
			if platform.platform().startswith('Windows'):
				self.txt.setStyleSheet("font-family: Lucida Console; font-size: 10;")
			else:
				self.txt.setStyleSheet("font-family: Monospace; font-size: 10;")
			vl.addWidget(self.txt)
			
			hl=QHBoxLayout()
			vl.addLayout(hl)
			
			self.btn=QPushButton("Close", self)
			hl.addStretch(2)
			hl.addWidget(self.btn)
			if self.simulator is not None and self.simulatorFile is not None:
				self.launchBtn=QPushButton("Simulate", self)
				hl.addStretch(1)
				hl.addWidget(self.launchBtn)
				self.launchBtn.setFocus()
			hl.addStretch(2)
			
			self.setLayout(vl)
			
			self.setWindowTitle(title)
			
			self.act=QAction("Close", self)
			self.act.setShortcuts([
				QKeySequence(Qt.Key_Escape), 
			])
			self.act.triggered.connect(self.close)
			self.act.setShortcutContext(Qt.WidgetWithChildrenShortcut)
			self.addAction(self.act)
			self.btn.clicked.connect(self.close)
			
			if self.simulator is not None and self.simulatorFile is not None:
				self.actLnch=QAction("Launch", self)
				self.actLnch.setShortcuts([
					QKeySequence(Qt.Key_S),
					QKeySequence(Qt.Key_Enter), 
					QKeySequence(Qt.Key_Return), 
				])
				self.actLnch.triggered.connect(self.launch)
				self.actLnch.setShortcutContext(Qt.WidgetWithChildrenShortcut)
				self.addAction(self.actLnch)
				self.launchBtn.clicked.connect(self.launch)
	
		@pyqtSlot()
		def launch(self):
			if self.simulator is not None and self.simulatorFile is not None:
				if self.simulator=="SpiceOpus":
					from ..simulator.spiceopus import SpiceOpus
					sim=SpiceOpus.findSimulator()
					if sim is not None:
						p=subprocess.Popen(
							[sim, self.simulatorFile], 
						)
					# print("hello")
			self.close()
		
	def popup(title, text, simulator=None, simulatorFile=None, error=False):
		app=QApplication(sys.argv)
		w=PopupWidget(title, text, simulator, simulatorFile)
		w.resize(600, 400)
		w.show()
		app.exec_()
		
else:
	def popup(title, text, error=False):
		stream=sys.stdout if not error else sys.stderr
		stream.write(title+"\n")
		stream.write("---------"+"\n")
		stream.write(text+"\n")
		stream.flush()
		
if __name__ == '__main__':
	popup("Title", "Hello", simulator="lala", simulatorFile="gaga")
