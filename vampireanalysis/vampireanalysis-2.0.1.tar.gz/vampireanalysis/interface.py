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
	BuildModel = True
	direc = CPoutput
	if direc[-1] != '/':
		direc = direc + '/' 
	main(BuildModel,clnum,direc,entries)
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
	BuildModel = False
	direc = CPoutput
	if direc[-1] != '/':
		direc = direc + '/'
	entries['Status'].delete(0,END)
	entries['Status'].insert(0,'analysis initiated')
	main(BuildModel,clnum,direc,entries)
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
	fields = ('Modeling','CP output folder', 'Number of Clusters','','Preprocessing','CP output subfolder','','Status')
	ents,rows = makeform(root, fields)
	root.bind('<Return>', (lambda event, e=ents: fetch(e))) 
	#function 1
	b1 = Button(rows[1],text='Search Folder', width=12,command=(lambda e=ents: getCPdir(e)))
	b1.pack(side=RIGHT,padx=5,pady=5)
	#function 2
	b2 = Button(rows[3],text='build model',width=12,command=(lambda e=ents: build(e)))
	b2.pack(side=RIGHT,padx=5,pady=5)
	b3 = Button(rows[3],text='apply model',width=12,command=(lambda e=ents: apply(e)))
	b3.pack(side=RIGHT,padx=5,pady=5)
	#function 3
	b4 = Button(rows[5],text='Search Subfolder', width=12,command=(lambda e=ents: getCPsubdir(e)))
	b4.pack(side=RIGHT,padx=5,pady=5)
	#function 4
	remove = BooleanVar()
	b5 = Checkbutton(rows[6],text='Remove Binary Masks',variable=remove)
	b5.pack(side=LEFT,padx=5,pady=5)
	b6 = Button(rows[6],text='proceed', width=12,command=(lambda e=ents: preprocess(e,remove.get())))
	b6.pack(side=RIGHT,padx=5,pady=5)
	#terminate
	quit = Button(root, text='Quit', command=root.quit)
	quit.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()

