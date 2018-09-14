#!/usr/bin/env python

import time
import json
from vmwvro2.workflow import Workflow, WorkflowRun
from vmwvro2.parameters import WorkflowParameter
from vmwvro2.sessions import Session
import settings

settings.init()
settings.loadConfig()

login = settings.config['default']['login']
password = settings.config['default']['password']

ratDev = Session(url="cidedevvro11.admnet.vodafone.com", username=login, password=password)
milDev = Session(url="ciitdevvro11.admnet.vodafone.com", username=login, password=password)
dubDev = Session(url="ciiedevvro11.admnet.vodafone.com", username=login, password=password)

ratProd1 = Session(url="cidevravro11.admnet.vodafone.com", username=login, password=password)
ratProd2 = Session(url="cidevravro12.admnet.vodafone.com", username=login, password=password)



#Workflow
wf = Workflow()
wf.id = "2294b1f0-46de-47dc-b740-f17d5d857502"
wf.param(name="ipAddress",    value="10.10.10.10", _type="string")
wf.param(name="ipSubnetName", value="*", _type="string")
wf.param(name="ipRangeName",  value="*", _type="string")
wf.param(name="spaceName",    value="*", _type="string")


#WorkflowRun
wfExeRat = WorkflowRun(wf)
wfExeMil = WorkflowRun(wf)
wfExeDub = WorkflowRun(wf)

wfExeRatP1 = WorkflowRun(wf)
wfExeRatP2 = WorkflowRun(wf)


wfExeRat.run(ratDev)
wfExeMil.run(milDev)
wfExeDub.run(milDev)

wfExeRatP1.run(ratProd1)
wfExeRatP2.run(ratProd2)



time.sleep(5)


wfExeRat.update()
wfExeMil.update()
wfExeDub.update()

wfExeRatP1.update()
wfExeRatP2.update()


print wfExeRat.state
print wfExeMil.state
print wfExeDub.state



#wfExe.status()
#print wfExe.state
#time.sleep(10)
