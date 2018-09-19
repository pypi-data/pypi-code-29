#!/usr/bin/python
# -*- coding=utf-8 -*-
 
import re
import sys,os
from xml.etree import ElementTree as et
import ConfigParser
import sys

class CommentedTreeBuilder (et.XMLTreeBuilder):
    def __init__ (self, html=0, target=None):
        et.XMLTreeBuilder.__init__(self, html, target)
        self._parser.CommentHandler = self.handle_comment
    def handle_comment (self, data):
        self._target.start(et.Comment, {})
        self._target.data(data)
        self._target.end(et.Comment)

class Conf():

    def xml2ini(self,oldfile,newfile,node,mynames):
        cf = ConfigParser.ConfigParser()
        tree = et.parse(oldfile)
        parents=tree.findall(node)
        for connection in parents:
            try:
                name = connection.attrib['name']
            except:
                continue
            if mynames:
                if "all" in mynames:
                    cf.add_section(name)
                    for server in connection[:mynames["all"]]:
                        k = server.attrib['ip']
                        v = server.attrib['port']
                        cf.set(name,k,v)
                        cf.write(open(newfile,'w'))
                elif name in mynames:
                    cf.add_section(name)
                    for server in connection[:mynames[name]]:
                        k = server.attrib['ip']
                        v = server.attrib['port']
                        cf.set(name,k,v)
                        cf.write(open(newfile,'w'))
                else:
                    continue
            else:
                cf.add_section(name)
                for server in connection:
                    k = server.attrib['ip']
                    v = server.attrib['port']
                    cf.set(name,k,v)
                    cf.write(open(newfile,'w'))
                
            
    
    def xml2xml(self,oldfile,newfile,node,start_port,mynames,ip="127.0.0.1"): 
        tree = et.parse(oldfile,parser=CommentedTreeBuilder())
        parents=tree.findall(node)
        i=0
        for parent in parents:
            try:
                name = parent.get("name")
            except:
                continue
            if mynames:
                if "all" in mynames:
                    kids = parent.getchildren()
                    children = kids[:mynames["all"]]
                    if ip:
                        for child in children:
                            child.set("ip",ip)
                            child.set("port",str(i+start_port))
                            i+=1
                    orphans = kids[mynames["all"]:]
                    for orphan  in orphans:
                        parent.remove(orphan)
                elif name in mynames:
                    kids = parent.getchildren()
                    children = kids[:mynames[name]]
                    if ip:
                        for child in children:
                            child.set("ip",ip)
                            child.set("port",str(i+start_port))
                            i+=1
                    orphans = kids[mynames[name]:]
                    for orphan  in orphans:
                        parent.remove(orphan)
                else:
                    continue
            else:
                children = parent.getchildren()
                for child in children:
                    child.set("ip",ip)
                    child.set("port",str(i+start_port))
                    i+=1

        tree.write(newfile, encoding="utf-8")

    def ini2lists(self,oldfile,start_port):
        cf = ConfigParser.ConfigParser()
        cf.read(oldfile)
        sections = cf.sections()
        result=[]
        m=0
        for section in sections:
            s1 = [(i[0],int(i[1])) for i in cf.items(section)]
            s2 = [("127.0.0.1",i+start_port+m) for i in range(len(s1))]
            result.append(zip(s1,s2))
            m+=len(s1)
        return result

def for_us():
    CONF=Conf()
    CONF.xml2ini("../conf/machine.xml","../conf/us.ini","connection",{})
    CONF.xml2xml("../conf/ac.xml","../conf/_us.xml","machine/bcgroup",41000,{})
    lists=CONF.ini2lists("../conf/ac.ini",41000)
def for_ac():
    CONF=Conf()
    CONF.xml2xml("/data1/test_ac/installed088/ac/bin/conf/ac.xml.bak","/data1/test_ac/installed088/ac/bin/conf/1ac.xml","machine/bcgroup",42000,{"all":1},"")
    CONF.xml2xml("/data1/test_ac/installed088/ac/bin/conf/1ac.xml","/data1/test_ac/installed088/ac/bin/conf/2ac.xml","machine/bcgroup",42000,{"all":1})
    CONF.xml2ini("/data1/test_ac/installed088/ac/bin/conf/1ac.xml","/data1/minisearch/upload/yulong11/conf/ac.ini","machine/bcgroup",{"all":1})
    lists=CONF.ini2lists("../conf/ac.ini",42000)

if __name__ == "__main__":
    for_ac()
