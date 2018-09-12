import os
from os import environ
import json
name="ReSubuser"


class environnement():
    """Class configuration with local variables"""
    TPL="""
    {"rights":{
            "daemon":false,
            "display":false,
            "docker":false,
            "home":false,
            "pwd":false,
            "root":false,
            "sound":false,
            "ssh":false
              },
    "cmd":"/bin/sh"}
    """
    def __init__(self):
        self.base="/home/"+environ['USER']+"/.ReSubuser/"
        self.user=environ['USER']
        self.display=environ['DISPLAY']
        self.ssh_auth=environ['SSH_AUTH_SOCK']
        self.pwd=environ['PWD']
        self.uid=os.getuid()
        self.gid=os.getgid()
        self.verbose=False
        self.cmd=""
        self.term=""

    def __str__(self):
        print(dict(self))

"""Variables with all status"""
env=environnement()
