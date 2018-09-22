#import sys
#almost the same as read_par_trilegal.py

class read(object):
   def __init__(self,par_file_name):
#def read(self,par_file_name):
      
      par_file=open(par_file_name,'r')
      par_name=[]; par_val=[]
      for line in par_file:
         pos=line.find('#')
         if (pos != -1): line=line[0:pos]

         pos=line.find('=')
         if (pos != -1): par_name.append(line[0:pos].strip())
         else: continue
         val_tmp=line[pos+1:].strip()
         if (val_tmp[0]!=val_tmp[-1] or (val_tmp[0]!="\'" and val_tmp[0]!="\"")):
            raise ValueError('quotations non-existing or un-matched for parameter:'+par_name[-1])
         par_val.append(val_tmp[1:-1])

         #pos1=line.find("'")
         #pos2=line.rfind("'")
         #if (pos1 == -1 or pos2 == -1 or pos1 == pos2):
         #   print "wrong parameter line, unmached '"
         #   exit(2)
         #else: par_val.append(line[pos1+1:pos2])
      par_file.close()
      self.par_name=par_name[1:]
      self.par_val=par_val[1:]
      self.obj={}
      for i1,par_i in enumerate(par_name): self.obj[par_i]=par_val[i1]
