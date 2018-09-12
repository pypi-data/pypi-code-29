import docker
import os
import ReSubuser
import re
import json


class dockerwrap():
    env=None

    def __init__(self,e):
        self.env=e


    def build(self,app):
        base=self.env.base
        user=self.env.user
        uid=self.env.uid
        gid=self.env.gid

        if (not os.path.isdir(base+app)):
            os.mkdir(base+app)
        os.chdir(base+app)
        if (not os.path.isfile(base+app+"/option")):
            option(app)
        if (not os.path.isfile(base+app+'/Dockerfile')):
            print("no file %s"%(base+app))
            edit(app)
        client=docker.APIClient()
        b={"user":user,"uid":str(uid),"gid":str(gid)}
        line=client.build(tag='sub_'+app,path='.',rm=True,nocache=True,buildargs=b)
        for a in line:
            dec=json.loads(a.decode('utf-8'))
            if ("stream" in dec):
                print("[\033[31mBuild %s\033[00m]>>"%app+dec['stream'].strip())
        return line

    def listimg(self,disp=1):
        base=self.env.base
        l=[a for a in os.listdir(base) if (not a == 'homes') ]
        if (disp==1):
            for a in l:
                print("> %s"%a)
        return l


    def container(self,):
        client = docker.from_env()
        ctrs=[a.attrs['RepoTags'][0] for a in client.images.list() if (len(a.attrs['RepoTags'])>0)]
        img=self.listimg(disp=0)
        status={}
        for v,a in enumerate(img):
            print("Check container [{}] ".format(a),end="")
            if "sub_{}:latest".format(a) in ctrs:
                status[a]={'status':"ok"}
                print("\33[32mOk\33[00m")
            else:
                status[a]={'status':"nok"}
                print("\33[31mneed a build\33[00m")

        for a in status:
            if (status[a]['status']=="nok"):
                print("build %s"%a)
                self.build(a)

        return status

    def clean(self):
        client = docker.from_env()
        r=re.compile('sub_(.*):')
        ctrs=[a.attrs['RepoTags'][0] for a in client.images.list() if (len(a.attrs['RepoTags'])>0)]
        img=self.listimg(disp=0)
        for v in ctrs:
            image=r.findall(v)
            if (len(image)>0):
                if image[0] not in img:
                    print("sub_"+image[0]+" will be removed")
                    client.images.remove("sub_"+image[0])
