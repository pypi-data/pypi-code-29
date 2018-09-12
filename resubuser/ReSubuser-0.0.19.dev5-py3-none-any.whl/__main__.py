from ReSubuser import cmdline

import os

def client():
    cmd=cmdline.cmdline()
    if (not cmd.env.internal):
        os.system(cmd.command())

if __name__=="__main__":
    print("[ ReSubuser ]")
    client()
