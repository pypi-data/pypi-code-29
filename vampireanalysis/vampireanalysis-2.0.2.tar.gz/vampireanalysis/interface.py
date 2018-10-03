#!/usr/bin/env python

from Tkinter import *
import tkFileDialog as fd
from unicodedata import normalize 
from main import *
from masksort import *
from UI_generator import *
from mask_reader_individual import *
from mask_remover import *


def makeform(root, fields):
	entries = {}
	rows= []
	for field in fields:
		row = Frame(root)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		if not field == 'Modeling' and not field =='Preprocessing' and not field =='':
			ent = Entry(row)
			if field == 'Number of Clusters':
				ent.insert(0,"choose a number [0 - 100]")
			elif field == 'Status':
				ent.insert(0,'Welcome to the Vampire Analysis. - Kyu Sang Han')
			elif field == 'Model Name':
				ent.insert(0,'Type your model name here to tag your result figures')
			else:ent.insert(0,"click search button")
			ent.pack(side=RIGHT, expand=YES, fill=X)
			entries[field] = ent
			lab = Label(row, width=22, text=field+": ", anchor='w')
			lab.pack(side=LEFT)
		else: 
			lab = Label(row, width=40, text=field, anchor='w',font=("Helvetica", 16))
			lab.pack(side=LEFT)
		rows.append(row)

	return entries,rows

def getCPdir(entries):
	# global b1
	# b1.config(text='Search Again')
	print ('you pressed search folder')
	CPoutput = StringVar()
	foldername = fd.askdirectory()
	CPoutput.set(foldername)
	CPoutput = CPoutput.get()
	entries['CP output folder'].delete(0,END)
	entries['CP output folder'].insert(0,CPoutput)

def getCPsubdir(entries):
	# b4.config(text='Search Again')
	print ('you pressed search subfolder')
	CPsub=StringVar()
	foldername = fd.askdirectory()
	CPsub.set(foldername)
	CPsub = CPsub.get()
	entries['CP output subfolder'].delete(0,END)
	entries['CP output subfolder'].insert(0,CPsub)

def build(entries):
	start = time.time()
	# global b2
	# b2.config(text='build again')
	print ('you pressed build')
	CPoutput = entries['CP output folder'].get()
	clnum = entries['Number of Clusters'].get()
	modelname = entries['Model Name'].get()
	BuildModel = True
	direc = CPoutput
	if direc[-1] != '/':
		direc = direc + '/' 
	main(BuildModel,clnum,direc,entries,modelname)
	print 'build finished'
	end = time.time()
	print 'elapsed time is ' + str(end-start) + 'seconds for build'

def apply(entries):
	start = time.time()
	# global b3
	# b3.config(text='apply again')
	print ('you pressed apply')
	CPoutput = entries['CP output folder'].get()
	clnum = entries['Number of Clusters'].get()
	modelname = entries['Model Name'].get()
	BuildModel = False
	direc = CPoutput
	if direc[-1] != '/':
		direc = direc + '/'
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'analysis initiated')
	main(BuildModel,clnum,direc,entries,modelname)
	print 'apply finished'
	end = time.time()	
	print 'elapsed time is ' + str(end-start) + 'seconds for apply'

def preprocess(entries,remove):
	start = time.time()
	# global b6
	# b6.config(text='process again')
	CPsub = entries['CP output subfolder'].get()
	print('you pressed process')
	direc = CPsub
	if direc[-1] != '/': direc = direc + '/'
	unorganized = [x for x in os.listdir(direc) if x.lower().endswith(('.tiff','.png','jpg','jpeg'))]
	if len(unorganized)>0: 
		masksort(direc,remove)
		UI_generator(direc)
		print 'preprocessing complete... now generating property chart'
		mask_reader_individual(direc) #this is get bdprop
	if remove == True: mask_remover(direc)
	print 'preprocessing finished'
	end = time.time()
	print 'elapsed time is ' + str(end-start) + 'seconds for preprocess'
	

# if __name__ == "__main__":
def interface():
	root = Tk()
	root.title("Vampire Analysis")
	fields = ('Preprocessing','CP output subfolder','','Modeling','CP output folder', 'Number of Clusters','Model Name','','','Status')
	ents,rows = makeform(root, fields)
	root.bind('<Return>', (lambda event, e=ents: fetch(e))) 
	#function 3
	b1 = Button(rows[1],text='Search Subfolder', width=12,command=(lambda e=ents: getCPsubdir(e)))
	b1.pack(side=RIGHT,padx=5,pady=5)
	#function 4
	remove = BooleanVar()
	b2 = Checkbutton(rows[2],text='Remove Binary Masks',variable=remove)
	b2.pack(side=LEFT,padx=5,pady=5)
	b3 = Button(rows[2],text='proceed', width=12,command=(lambda e=ents: preprocess(e,remove.get())))
	b3.pack(side=RIGHT,padx=5,pady=5)
	#function 1
	b4 = Button(rows[4],text='Search Folder', width=12,command=(lambda e=ents: getCPdir(e)))
	b4.pack(side=RIGHT,padx=5,pady=5)
	#function 2
	b5 = Button(rows[7],text='build model',width=12,command=(lambda e=ents: build(e)))
	b5.pack(side=RIGHT,padx=5,pady=5)
	b6 = Button(rows[7],text='apply model',width=12,command=(lambda e=ents: apply(e)))
	b6.pack(side=RIGHT,padx=5,pady=5)
	#terminate
	quit = Button(root, text='Quit', command=root.quit)
	quit.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()

