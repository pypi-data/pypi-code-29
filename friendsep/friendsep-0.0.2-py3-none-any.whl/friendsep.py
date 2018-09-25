import os,sys
from os.path import expanduser
from random import randint
import subprocess

#print(os.getcwd())
def main():
    home=expanduser("~")
    os.chdir(home)
    friends_file=home+"/friends_path.txt"
    path=""
    if(os.path.exists(friends_file)):
        #print(friends_file)
        with open(friends_file) as f:
            path=f.read()
        print("\nPath to F.R.I.E.N.D.S folder: ",path)

    else:
        path=input("Enter the absolute path of the folder where F.R.I.E.N.D.S episodes are stored: ")
        path=path+"/"
        file=open("friends_path.txt","w")
        file.write(path)
        file.close()

    os.chdir(path)
    #Get a list of subdirectories in the directory
    ls=next(os.walk('.'))[1]
    inp=randint(0,len(ls)-1)
    npath=path+ls[inp]+"/"
    os.chdir(npath)
    fs=next(os.walk('.'))[2]
    inp1=randint(0,len(fs)-1)
    print("\nEnjoy watching F.R.I.E.N.D.S! :-D\n")

    p=subprocess.Popen(["vlc",fs[inp1]],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=p.communicate()

if __name__=="__main__":
    main()
    

