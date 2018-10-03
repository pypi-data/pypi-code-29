'''
---------------------------------------------------

	File name: schevents.py

---------------------------------------------------
	Description:   Generates Schedule Events from schedule file based on the input time and Mode of Operation

---------------------------------------------------	
	Package     : softacu
	Version     : 1.660
	Language    : Python
	Authors		: 

Revision History:

Version		Created 			Modification
-----------------------------------------------------------------
1.652		06-Jun-2018			Initial Release
1.653		09-Jun-2018			Modified PAST PURGE Generate events Logic
1.654		13-Jun-2018			Removed dummy Mute and End times for Past Schedule case
1.660		31-Jul-2018			Added HandoverCount as an argument.
'''

import time
import xml.etree.ElementTree as ET
import os
import datetime
import numpy as np
from schedulevalidity import ScheduleValidity
import threading

lock = threading.RLock()


def ScheduleTracks(ScheduleFilepath,Beam,EpochTime,iMode,schtype):

	SCH = np.zeros(16, dtype=[('dwStartTime','i4'),('dwHandoverTime','i4'),('dwEndTime', 'i4'), ('strSatelliteID', 'S10'), ('strBeam', 'S10'),('strRegion', 'S10'),	('dwPrePassTime', 'i4')])
	iSatelliteCount = 0
	strError = ''
	pattern = '%m/%d/%Y %H:%M:%S'
	zero_hour = "00:00:00"
	strEpoch = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime))
	var = strEpoch.split()
	Ddate_time = " ".join([var[0],zero_hour])
	DEpoch = int(time.mktime(time.strptime(Ddate_time, pattern)))
	yesterday_Epoch = int(DEpoch-86400)
	ret = 0
	if schtype == 'old':
		ScheduleFilepath = os.path.join(ScheduleFilepath,'schedule')	#Current Schedule
	else:
		ScheduleFilepath = os.path.join(ScheduleFilepath,'new_schedule')	#New Schedule
	 #Schedule file parsing
	try:
		tree = ET.parse(ScheduleFilepath)
	except:
		strError  = 'Invalid Schedule File'
		ret = -1
		return
	root = tree.getroot()
	if root.tag == 'Schedule':
		StrPeriod = root.attrib['Period']
		period = StrPeriod.split(':')
		hours = int(period[0])
		mins = int(period[1])
		secs = int(period[2].split('.')[0])
		iPeriod = (hours * 3600) + (mins * 60) + secs
		strAction = root.attrib['Action']
		pattern = '%m/%d/%Y %H:%M:%S'
		dwPrepassTime = 0
		dwHandoverTime = 0
		dwEndTime = 0
		dwStartTime = 0
		try:
			for node in tree.iter('Track'):
				for element in node.iter('Handover'): #Extract Handover element
					SCH[iSatelliteCount]['strBeam'] = element.attrib.get('Beam')
					SCH[iSatelliteCount]['strRegion'] = element.attrib.get('Region')
					strHandoverTime = element.attrib.get('Time')
					Handover_time = int(time.mktime(time.strptime(strHandoverTime, pattern)))
					if (Handover_time > (EpochTime-86400)): # Handover with Future Time
						dwHandoverTime = Handover_time
					else: # Bring CurSchedule track time to yesterday time
						var = strHandoverTime.split()
						Ddate_time = " ".join([var[0],zero_hour])
						DEpoch = int(time.mktime(time.strptime(Ddate_time, pattern)))
						diff = Handover_time - DEpoch
						dwHandoverTime = (int(diff) + int(yesterday_Epoch))
					SCH[iSatelliteCount]['dwHandoverTime'] = dwHandoverTime
						
					if SCH[iSatelliteCount]['strBeam'] == Beam:
						strPrePassTime = node.attrib.get('PrePassTime')
						Prepass_Time = int(time.mktime(time.strptime(strPrePassTime, pattern)))
						if (Prepass_Time > (EpochTime-86400)):
							dwPrepassTime = Prepass_Time
						else:
							var = strPrePassTime.split()
							Ddate_time = " ".join([var[0],zero_hour])
							DEpoch = int(time.mktime(time.strptime(Ddate_time, pattern)))
							diff = Prepass_Time - DEpoch
							dwPrepassTime = (int(diff) + int(yesterday_Epoch))
						SCH[iSatelliteCount]['dwPrePassTime'] = dwPrepassTime

						strStartTime = node.attrib.get('StartTime')
						Start_Time = int(time.mktime(time.strptime(strStartTime, pattern)))
						if (Start_Time > (EpochTime-86400)):
							dwStartTime = Start_Time
						else:
							var = strStartTime.split()
							Ddate_time = " ".join([var[0],zero_hour])
							DEpoch = int(time.mktime(time.strptime(Ddate_time, pattern)))
							diff = Start_Time - DEpoch
							dwStartTime = (int(diff) + int(yesterday_Epoch))
						SCH[iSatelliteCount]['dwStartTime'] = dwStartTime
			
						strEndTime = node.attrib.get('EndTime')
						End_Time = int(time.mktime(time.strptime(strEndTime, pattern)))
						if (End_Time > (EpochTime-86400)):
							dwEndTime = End_Time
						else:
							var = strEndTime.split()
							Ddate_time = " ".join([var[0],zero_hour])
							DEpoch = int(time.mktime(time.strptime(Ddate_time, pattern)))
							diff = End_Time - DEpoch
							dwEndTime = (int(diff) + int(yesterday_Epoch))
						SCH[iSatelliteCount]['dwEndTime'] = dwEndTime
						SCH[iSatelliteCount]['strSatelliteID'] = node.attrib.get('Satellite')
						iSatelliteCount = iSatelliteCount+1
						ret = 0
					else:
						strError = 'Beam Id is not Matched'
						ret = -1
		except:
			strError  = 'No tracks found'
			ret = -1
			return
	else:
		strError  = 'CurSchedule tag not found'
		ret = -1
		return
	if iSatelliteCount < 2:
		strError  = "CurSchedule file has no satellites for the Beam %s" % Beam
		ret = -1
		return
	else:
		SCH = SCH[0:iSatelliteCount]
		SCH.sort(order='dwStartTime')
		
		if iMode == 0:
			RefTime = SCH[0]['dwHandoverTime']
		else:
			RefTime = SCH[0]['dwHandoverTime']
			
		if EpochTime < RefTime:
			index = iSatelliteCount-1
		else:		
			bIndex = False
			while True:
				for index in range(iSatelliteCount):
					if iMode == 0:
						RefTime = SCH[index]['dwHandoverTime']
						FRefTime = SCH[(index+1)%iSatelliteCount]['dwHandoverTime']
					else:
						RefTime = SCH[index]['dwHandoverTime']
						FRefTime = SCH[(index+1)%iSatelliteCount]['dwHandoverTime']
						
					if (EpochTime >= RefTime) and (EpochTime < FRefTime):
						bIndex = True
						ret = 0
						break;
					else:
						SCH[index]['dwPrePassTime'] += iPeriod
						SCH[index]['dwStartTime'] += iPeriod
						SCH[index]['dwHandoverTime'] += iPeriod
						SCH[index]['dwEndTime'] += iPeriod
				if bIndex == True:
					break;
					
		iTrackIndex = index;
	iSatelliteCount = iSatelliteCount
	return [SCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError]
	
def GenerateEvents(SCH, iSatelliteCount, iPeriod, iCurrentAntenna, EventCount,schtype,iHandoverCount):

	SCHEVENTS = np.zeros(iSatelliteCount*EventCount, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
	if iCurrentAntenna == 1:
		iPreviousAntenna = 2
	elif iCurrentAntenna == 2:
		iPreviousAntenna = 1
	index = 0
	if EventCount == 4: # Single SAT
		print 'single Antenna Mode'
		for i in range(iSatelliteCount):
			SCHEVENTS[index] =   ('Retrace/StartTime', SCH[i]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime'])),SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+1] = ('UnMuteTime       ', SCH[i]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+2] = ('MuteTime         ', SCH[(i+1)%iSatelliteCount]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[(i+1)%iSatelliteCount]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+3] = ('EndTime          ', SCH[(i+1)%iSatelliteCount]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[(i+1)%iSatelliteCount]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			index += EventCount
		SCHEVENTS[-1][1] = SCHEVENTS[-1][1] + iPeriod
		SCHEVENTS[-1][2] = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS[-1][1]))
		SCHEVENTS[-2][1] = SCHEVENTS[-2][1] + iPeriod
		SCHEVENTS[-2][2] = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS[-2][1]))
	elif EventCount == 5: # Normal SAT
		for i in range(iSatelliteCount):
			if index == 0:
				SCH[-1]['dwEndTime'] = SCH[-1]['dwEndTime'] - iPeriod
			SCHEVENTS[index] =   ('Retrace/StartTime', SCH[i]['dwStartTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwStartTime'])),SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+1] = ('HandoverTime     ', SCH[i]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+2] = ('UnMuteTime       ', SCH[i]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+3] = ('MuteTime         ', SCH[i]['dwHandoverTime']+iHandoverCount, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime']+iHandoverCount)), SCH[(i-1)%iSatelliteCount]['strSatelliteID'],iPreviousAntenna)
			SCHEVENTS[index+4] = ('EndTime          ', SCH[(i-1)]['dwEndTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[(i-1)]['dwEndTime'])), SCH[(i-1)%iSatelliteCount]['strSatelliteID'],iPreviousAntenna)
			index += EventCount
			iCurrentAntenna, iPreviousAntenna = iPreviousAntenna, iCurrentAntenna
	elif EventCount == 6: # Normal DAT
		for i in range(iSatelliteCount):
			SCHEVENTS[index] = ('Retrace/StartTime   ', SCH[i]['dwStartTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwStartTime'])),SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+1] = ('HandoverTime        ', SCH[i]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+2] = ('UnMuteTime          ', SCH[i]['dwHandoverTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime'])), SCH[i]['strSatelliteID'],iCurrentAntenna)
			SCHEVENTS[index+3] = ('MuteTime            ', SCH[i]['dwHandoverTime']+iHandoverCount, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime']+iHandoverCount)), SCH[(i-1)%iSatelliteCount]['strSatelliteID'],iPreviousAntenna)
			SCHEVENTS[index+4] = ('EndTime             ', SCH[i]['dwHandoverTime']+iHandoverCount, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime']+iHandoverCount)), SCH[(i-1)%iSatelliteCount]['strSatelliteID'],iPreviousAntenna)
			SCHEVENTS[index+5] = ('DC Retrace/StartTime', SCH[i]['dwHandoverTime']+iHandoverCount, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCH[i]['dwHandoverTime']+iHandoverCount)), SCH[i]['strSatelliteID'],iPreviousAntenna)
			index += EventCount
			iCurrentAntenna, iPreviousAntenna = iPreviousAntenna, iCurrentAntenna
		
	np.argsort(SCHEVENTS[0][1])
		
	return SCHEVENTS

	
def SchEvents(ScheduleFilepath,Beam,EpochTime,iMode,newsch,iCurrentAntenna,iSchUploadTime,iHandoverCount):
													
	with lock:
		schtype = 'old'
		[SCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(ScheduleFilepath,Beam,EpochTime,iMode,schtype)
		SCH.sort(order='dwStartTime')

		if iMode == 0:
			EventCount = 4
		elif iMode == 2:
			EventCount = 6
		else:
			EventCount = 5
		SCHEVENTS = GenerateEvents(SCH, iSatelliteCount, iPeriod, iCurrentAntenna,EventCount,schtype,iHandoverCount)		
		
		if newsch == 1:
			schtype = 'new'
			[Valid, Output, strAction, dwStartTime,dwHandovertime,dwEndTime] = ScheduleValidity(ScheduleFilepath,Beam,EpochTime,newsch)

			if Valid == True:
				if EpochTime > dwStartTime:	# Past Time	
					bInstantSwitch = False
					if  strAction == 'ADD':
						#print 'PAST ADD'
						SCHEVENTS_OLD = SCHEVENTS[0:2*EventCount]
						#Old SATID correspoding to primary antenna (HW + 26 to Next HW + 26)
						if (SCH[0]['dwHandoverTime']+iHandoverCount < EpochTime < SCH[1]['dwHandoverTime']+iHandoverCount): # If Uploaded time is less than Handover Window; 
							#print 'Old Start to HW case'
							OldSatID = SCH[0]['strSatelliteID']	
							PrimaryAnt = iCurrentAntenna
						else:
							OldSatID = SCH[-1]['strSatelliteID']
							PrimaryAnt = 3-iCurrentAntenna
						FutureEvents = [i for i in SCHEVENTS_OLD['dwEpochTime'] if i >= EpochTime]
						SCHEVENTS_OLD = SCHEVENTS_OLD[0:len(SCHEVENTS_OLD)-len(FutureEvents)]
						[SCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(ScheduleFilepath,Beam,EpochTime,iMode,schtype)
						SCH.sort(order='dwStartTime')
							
						if EventCount != 4 and (SCH[1]['dwStartTime'] < EpochTime < SCH[1]['dwHandoverTime']):
							#print 'binstant switch'
							bInstantSwitch = True

						SCHEVENTS_NEW = GenerateEvents(SCH, iSatelliteCount, iPeriod, PrimaryAnt,EventCount,schtype,iHandoverCount)
						SCHEVENTS_NEW = SCHEVENTS_NEW[EventCount:-1]
						if bInstantSwitch:
							SCHEVENTS_NEW[0]['dwEpochTime'] = EpochTime + 5
							SCHEVENTS_NEW[0]['strEpochTime'] = time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime+5))

						if EventCount != 4:
							SCHEVENTS_NEW[3][3] = OldSatID
							SCHEVENTS_NEW[4][3] = OldSatID
						if EventCount == 4 and (SCHEVENTS_OLD is not None):
							if (SCHEVENTS_OLD[-1][0].rstrip() != 'EndTime'):
								TEMPEVENTS = np.zeros(2, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
								TEMPEVENTS[0] = ('MuteTime         ', SCHEVENTS_NEW[1]['dwEpochTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS_NEW[1]['dwEpochTime'])),OldSatID,iCurrentAntenna)
								TEMPEVENTS[1] = ('EndTime          ', SCHEVENTS_NEW[1]['dwEpochTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS_NEW[1]['dwEpochTime'])), OldSatID,iCurrentAntenna)
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW),axis=0)
						else:
							SCHEVENTS = np.concatenate((SCHEVENTS_OLD,SCHEVENTS_NEW),axis=0)
					else: # PURGE
						#print 'PAST PURGE'
						bSameSAT = False
						SCHEVENTS_OLD = SCHEVENTS[0:2*EventCount]
							#Old SATID correspoding to primary antenna (HW + 26 to Next HW + 26)
						if SCH[0]['dwHandoverTime']+iHandoverCount < EpochTime < (SCH[1]['dwHandoverTime'] + iHandoverCount): # If Uploaded time is less than Handover Window; 
							OldAntID_PRI = iCurrentAntenna #SCHEVENTS_OLD[-1]['AntennaID']
							OldAntID_SEC = 3-iCurrentAntenna #SCHEVENTS_OLD[0]['AntennaID']
						else:
							OldAntID_PRI = 3-iCurrentAntenna #SCHEVENTS_OLD[0]['AntennaID']
							OldAntID_SEC = iCurrentAntenna #SCHEVENTS_OLD[-1]['AntennaID']
						if EpochTime < SCH[0]['dwHandoverTime']+iHandoverCount:
							OldSatID_PRI = SCH[-1]['strSatelliteID']	
							OldSatID_SEC = SCH[0]['strSatelliteID']
						elif SCH[0]['dwHandoverTime']+iHandoverCount < EpochTime < (SCH[1]['dwStartTime']): # If Uploaded time is less than Handover Window; 
							OldSatID_PRI = SCH[0]['strSatelliteID']	
							OldSatID_SEC = SCH[-1]['strSatelliteID']
						else:
							OldSatID_PRI = SCH[0]['strSatelliteID']	
							OldSatID_SEC = SCH[1]['strSatelliteID']
						FutureEvents = [i for i in SCHEVENTS_OLD['dwEpochTime'] if i >= EpochTime]
						SCHEVENTS_OLD = SCHEVENTS_OLD[0:len(SCHEVENTS_OLD)-len(FutureEvents)]
						[SCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(ScheduleFilepath,Beam,EpochTime,iMode,schtype)
						SCH.sort(order='dwStartTime')
						if EventCount == 4:
							SCHEVENTS_NEW = GenerateEvents(SCH, iSatelliteCount, iPeriod, iCurrentAntenna,EventCount,schtype,iHandoverCount)
						else:
							SCHEVENTS_NEW = GenerateEvents(SCH, iSatelliteCount, iPeriod, OldAntID_SEC,EventCount,schtype,iHandoverCount)
						SCHEVENTS_TEMP = SCHEVENTS_NEW[0:EventCount]
						if EventCount != 4 and (SCH[0]['dwStartTime'] < EpochTime < SCH[0]['dwHandoverTime']):
							NewSatID = SCHEVENTS_TEMP[-2]['strSatelliteID']
							NewAntID = SCHEVENTS_TEMP[0]['AntennaID']
						else:
							NewSatID = SCHEVENTS_TEMP[0]['strSatelliteID']
							NewAntID = SCHEVENTS_TEMP[-2]['AntennaID']
						EpochTime = EpochTime+5
						# Compare old Schedule sat ID and new schedule sat ID; If same no change is required; if different, change the SAT ID-> may require a flag
						if NewSatID == OldSatID_PRI:	#Same Satellite Case
							#print 'Same Satellite Case', NewSatID, OldSatID_PRI
							if EventCount != 4:
								SCHEVENTS_NEW = GenerateEvents(SCH, iSatelliteCount, iPeriod, NewAntID,EventCount,schtype,iHandoverCount)
							if EventCount == 5:	# Normal SAT
								#TEMPEVENTS = np.zeros(2, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
								#TEMPEVENTS[0] = ('MuteTime         ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_SEC,OldAntID_SEC)
								#TEMPEVENTS[1] = ('EndTime          ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_SEC,OldAntID_SEC)
								#SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW[EventCount:-1]),axis=0)
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,SCHEVENTS_NEW[EventCount:-1]),axis=0)
							elif EventCount == 6:	# Normal DAT
								#TEMPEVENTS = np.zeros(3, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
								#TEMPEVENTS[0] = ('MuteTime            ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_SEC,OldAntID_SEC)
								#TEMPEVENTS[1] = ('EndTime             ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_SEC,OldAntID_SEC)							
								#TEMPEVENTS[2] = ('DC Retrace/StartTime', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_PRI,OldAntID_SEC)							
								#SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW[EventCount:-1]),axis=0)
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,SCHEVENTS_NEW[EventCount:-1]),axis=0)
							if EventCount == 4:	# Single SAT
								SCHEVENTS_NEW = SCHEVENTS_NEW[EventCount:-1]
								if (SCHEVENTS_OLD[-1][0].rstrip() != 'EndTime'):
									TEMPEVENTS = np.zeros(2, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
									TEMPEVENTS[0] = ('MuteTime         ', SCHEVENTS_NEW[1]['dwEpochTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS_NEW[1]['dwEpochTime'])),OldSatID_PRI,iCurrentAntenna)
									TEMPEVENTS[1] = ('EndTime          ', SCHEVENTS_NEW[1]['dwEpochTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS_NEW[1]['dwEpochTime'])),OldSatID_PRI,iCurrentAntenna)
								else:
									TEMPEVENTS = []
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW),axis=0)
						else:
							StartEvents = [i for i in SCH['dwStartTime'] if i > EpochTime]
							NxtStartTime = StartEvents[0]
							if EventCount == 5:	# Normal SAT
								TEMPEVENTS = np.zeros(5, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
								HWTime = max(min(EpochTime+15,NxtStartTime-27),EpochTime+2)
								MuteTime = HWTime + max(min(iHandoverCount,NxtStartTime-EpochTime-1),1)			
								EndTime = HWTime + (MuteTime - HWTime)
								TEMPEVENTS[0] = ('Retrace/StartTime', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),NewSatID,OldAntID_SEC)
								TEMPEVENTS[1] = ('HandoverTime     ', HWTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(HWTime)),NewSatID,OldAntID_SEC)
								TEMPEVENTS[2] = ('UnMuteTime       ', HWTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(HWTime)),NewSatID,OldAntID_SEC)
								TEMPEVENTS[3] = ('MuteTime         ', MuteTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(MuteTime)),OldSatID_PRI,OldAntID_PRI)
								TEMPEVENTS[4] = ('EndTime          ', EndTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EndTime)),OldSatID_PRI,OldAntID_PRI)														
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW[EventCount:-1]),axis=0)
							elif EventCount == 6:	# Normal DAT
								TEMPEVENTS = np.zeros(6, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
								HWTime = max(min(EpochTime+15,NxtStartTime-27),EpochTime+2)
								MuteTime = HWTime+max(min(iHandoverCount,NxtStartTime-EpochTime-1),1)			
								EndTime = HWTime + (MuteTime - HWTime)
								TEMPEVENTS[0] = ('Retrace/StartTime   ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),NewSatID,OldAntID_SEC)							
								TEMPEVENTS[1] = ('HandoverTime        ', HWTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(HWTime)),NewSatID,OldAntID_SEC)							
								TEMPEVENTS[2] = ('UnMuteTime          ', HWTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(HWTime)),NewSatID,OldAntID_SEC)
								TEMPEVENTS[3] = ('MuteTime            ', MuteTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(MuteTime)),OldSatID_PRI,OldAntID_PRI)
								TEMPEVENTS[4] = ('EndTime             ', MuteTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(MuteTime)),OldSatID_PRI,OldAntID_PRI)							
								TEMPEVENTS[5] = ('DC Retrace/StartTime', MuteTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(MuteTime)),NewSatID,OldAntID_PRI)							
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW[EventCount:-1]),axis=0)
							elif EventCount == 4:	# Single SAT
								TEMPEVENTS = np.zeros(4, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
								TEMPEVENTS[0] = ('MuteTime         ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_PRI,iCurrentAntenna)
								TEMPEVENTS[1] = ('EndTime          ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),OldSatID_PRI,iCurrentAntenna)
								TEMPEVENTS[2] = ('Retrace/StartTime', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),NewSatID,iCurrentAntenna)
								TEMPEVENTS[3] = ('UnMuteTime       ', EpochTime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(EpochTime)),NewSatID,iCurrentAntenna)
								SCHEVENTS_NEW = SCHEVENTS_NEW[EventCount:-1]
								if (SCHEVENTS_OLD[-1][0].rstrip() != 'EndTime'):
									TEMPEVENTS1 = np.zeros(2, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
									TEMPEVENTS1[0] = ('MuteTime         ', SCHEVENTS_NEW[1]['dwEpochTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS_NEW[1]['dwEpochTime'])),NewSatID,iCurrentAntenna)
									TEMPEVENTS1[1] = ('EndTime          ', SCHEVENTS_NEW[1]['dwEpochTime'], time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(SCHEVENTS_NEW[1]['dwEpochTime'])),NewSatID,iCurrentAntenna)
								else:
									TEMPEVENTS = []
								SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,TEMPEVENTS1,SCHEVENTS_NEW),axis=0)
				else: # Future Time
					FutureEvents = [i for i in SCHEVENTS['dwEpochTime'] if i >= dwStartTime]
					if 0 < len(FutureEvents) < len(SCHEVENTS):
						SCHEVENTS_OLD = SCHEVENTS[0:len(SCHEVENTS)-len(FutureEvents)]
						if strAction == 'ADD':
							pass
						else: # PURGE
							StartTimeEvents = []
							for i in range(len(SCHEVENTS_OLD)):
								if SCHEVENTS_OLD[i][0].rstrip() == 'Retrace/StartTime':
									StartTimeEvents.append(SCHEVENTS_OLD[i]['dwEpochTime'])
							FuturePurgeEvents = [i for i in SCHEVENTS_OLD['dwEpochTime'] if i >= StartTimeEvents[-1]]
							SCHEVENTS_OLD = SCHEVENTS_OLD[0:len(SCHEVENTS_OLD)-len(FuturePurgeEvents)]
							
						StartTimeEvents = []
						SatelliteEvents = []
						AntennaEvents= []
						for i in range(len(SCHEVENTS_OLD)):
							if SCHEVENTS_OLD[i][0].rstrip() == 'Retrace/StartTime':
								StartTimeEvents.append(SCHEVENTS_OLD[i]['dwEpochTime'])
								SatelliteEvents.append(SCHEVENTS_OLD[i]['strSatelliteID'])
								AntennaEvents.append(SCHEVENTS_OLD[i]['AntennaID'])
						OldAntID = AntennaEvents[-1]
						OldSatID = SatelliteEvents[-1]
						if EventCount != 4:
							if (SCHEVENTS_OLD[-1][0].rstrip() not in ('MuteTime','EndTime','DC Retrace/StartTime')):
								OldSatID = SatelliteEvents[-2]
								iCurrentAntenna = OldAntID
							else:						
								iCurrentAntenna = 3 - OldAntID #Start with the other Antenna 
								
						[SCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(ScheduleFilepath,Beam,EpochTime,iMode,schtype)
						SCH.sort(order='dwStartTime')
						SCHEVENTS_NEW = GenerateEvents(SCH, iSatelliteCount, iPeriod, iCurrentAntenna,EventCount,schtype,iHandoverCount)
						if EventCount in (5,6):
							SCHEVENTS_NEW[3][3] = OldSatID
							SCHEVENTS_NEW[4][3] = OldSatID
						
						if EventCount == 4 and (SCHEVENTS_OLD[-1][0].rstrip() != 'EndTime'):
							TEMPEVENTS = np.zeros(2, dtype=[('strEventName', 'S20'),('dwEpochTime', 'i4'),('strEpochTime', 'S20'),('strSatelliteID', 'S10'),('AntennaID', 'i2')])	
							TEMPEVENTS[0] = ('MuteTime         ', dwHandovertime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(dwHandovertime)),OldSatID,iCurrentAntenna)
							TEMPEVENTS[1] = ('EndTime          ', dwHandovertime, time.strftime("%m/%d/%Y %H:%M:%S", time.gmtime(dwHandovertime)), OldSatID,iCurrentAntenna)
							SCHEVENTS = np.concatenate((SCHEVENTS_OLD,TEMPEVENTS,SCHEVENTS_NEW),axis=0)
						else:
							SCHEVENTS = np.concatenate((SCHEVENTS_OLD,SCHEVENTS_NEW),axis=0)					
			else:
				pass
			
		return [SCHEVENTS]

