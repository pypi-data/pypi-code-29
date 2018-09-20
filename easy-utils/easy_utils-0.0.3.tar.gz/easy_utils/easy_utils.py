from time import sleep
from os import system, listdir, path, sys
from datetime import datetime
from subprocess import Popen, DEVNULL

def alert(alarm, x):
    for i in range(x):
        print(Fore.YELLOW + alarm+Style.RESET_ALL)
        sleep(1)
    return

def check_dir(child, parent):
    file_dest  =  parent + child
    if child[:-1] not in listdir(parent):
        command  = 'mkdir ' + file_dest
        system(command)
        print(command)
        return file_dest
    else:
        return file_dest

def check_file(fname, file_dest):
    if fname not in listdir(file_dest):
        return file_dest +fname
    else:
        return False

def log_it(text):
    fname = '. /log/'+str(datetime.today()).rsplit(' ',1)[0]+'.log'
    text = str(text)
    with open(fname, 'a+') as f:
        f.write(str(datetime.now())[:-7]+'\t'+text+'\n')
        f.close()

def run_in_background(args):
    Popen(args,stdout=DEVNULL, stderr=DEVNULL)
