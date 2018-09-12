import os
import json


class config():
    env=None

    def __init__(self,e):
        self.env=e


    def check(self):
        """Check folders """
        base=self.env.base
        if (self.env.verbose==True):
            print("Check %s"%base)
        if (not os.path.isdir(base)):
            os.mkdir(base)
        if (not os.path.isdir(base+"/homes")):
            os.mkdir(base+"/homes")
        return 0

    def default_option(self,app):
        """Write default option from TPL """
        base=self.env.base
        print("create "+app+" option")
        default_json=json.loads(ReSubuser.TPL)
        json.dump(default_json, open(base+"/"+app+"/option","w"),indent=4)
        return 0

    def edit(self,app):
        """Open Editor to write option/dockerfile"""
        base=self.env.base
        if (self.env.verbose==True):
            print("Edit %s"%base+app)    
        if (not os.path.isdir(base+app)):
            os.mkdir(base+app)
        os.chdir(base+app)
        if (not os.path.isfile("option")):
            self.default_option(app)

        os.system("$EDITOR option Dockerfile")
        return
