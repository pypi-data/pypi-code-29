#!/usr/bin/env python

import time
import json
from vmwvro2.workflow import Workflow, WorkflowRun
from vmwvro2.parameters import WorkflowParameter
from vmwvro2.sessions import Session
from vmwvro2.settings import settings

settings.init()
settings.loadConfig()

login = settings.config['default']['login']
password = settings.config['default']['password']
proxies = dict(https='socks5://127.0.0.1:8888')


vro =    Session(alias="dev-de", 
                 url="cidedevvro11.admnet.vodafone.com", 
                 username=login, 
                 password=password,
                 proxies=proxies)

ratDev = Session(alias="dev-de", 
                 url="cidedevvro11.admnet.vodafone.com", 
                 username=login, 
                 password=password,
                 proxies=proxies)

milDev = Session(alias="dev-it", 
                 url="ciitdevvro11.admnet.vodafone.com", 
                 username=login, 
                 password=password,
                 proxies=proxies)


#Workflow
wf = Workflow()
wf.id = "92bffd10-ea48-43e7-8970-b5dd6e577f5f"
wf.param(name="s1", value="my value")


#WorkflowRun
wfExe    = WorkflowRun(wf, ratDev)

#wfExeRat = WorkflowRun(wf)
#wfExeMil = WorkflowRun(wf)

#wfExe.run()
wfExe.from_file('./sample-json/exeDetail2.json')

print wfExe.href


wfExe.wait()
print wfExe
wfExe.print_paramenters()

