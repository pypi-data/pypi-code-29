#! usr/bin/python
'''
---------------------------------------------------

	File name	: main.py

---------------------------------------------------
	Description	: ATAMS Main Module
	
---------------------------------------------------	
	Package     : atams
	Version     : 0.1
	Language    : Python
	Authors		: 

Revision History:

Version		Created 			Notes
-----------------------------------------------------------------
'''

import os, signal, sys
import time
import mmap
from structures import *
from sqliteConn import SQLite
import shutil
import platform
import struct, ntplib, math
import filecmp
import win32api, datetime
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

from schedulevalidity import ScheduleValidity
from channelsvalidity import ChannelsValidity
from ephemerisvalidity import EphemerisValidity
from ChannelParams import ChannelsParams

from schevents import SchEvents
from schevents import ScheduleTracks

# Create instance of all structure objects from structures.py file
ChannelPlan 	= CHANNELPLAN()					# create instance of CHANNELPLAN object
Schedule 		= SCHEDULE()					# create instance of SCHEDULE object
Ephemeris 		= EPHEMERIS()					# create instance of EPHEMERIS object
Spacecraft 		= SPACECRAFT()					# create instance of SPACECRAFT object
StructSatellite = STRUCTSATELLITE()				# create instance of STRUCTSATELLITE object

if 'Windows' in platform.platform():
	OS_VER = 'WINDOWS'
elif 'centos' in platform.platform():
	OS_VER = 'CENTOS'
else:
	OS_VER = 'UBUNTU'
	
if OS_VER == 'WINDOWS':
	CUR_PATH = os.path.join('c:','\ATAMS','atams')
	BAK_PATH = os.path.join('c:','\ATAMS','BAK_DIR')
	SDB_VALID_DIR = os.path.join('c:','\ATAMS','SDB_VALID_DIR')
	PACKAGE_DIR = os.path.join('c:','\ATAMS','PACKAGE_DIR')
	SDB_FILES_DIR = os.path.join('c:','\ATAMS','atams','SDBFiles')
	SDKFunctions = CDLL(os.path.join(CUR_PATH,'libsdkwindows.so'))
elif OS_VER == 'CENTOS':
	CUR_PATH = os.getcwd()
	BAK_PATH = '/var/www/html/atams/BAK_DIR'
	SDB_VALID_DIR = '/etc/atams/sdbfiles'
	SDB_FILES_DIR = '/var/www/html/atams/SDBFiles' # SDB Files path
	PACKAGE_DIR = '/var/cache/yum/armhfp/7/softacu/packages'
	SDKFunctions = CDLL(os.path.join(CUR_PATH,'libo3bsdbsdk.so'))

if OS_VER != 'WINDOWS':
	from SetupRsync import SDBSetupRsync
	
MP_DB_NAME = os.path.join(CUR_PATH,'atams_mp.db')
CUR_DB_NAME = os.path.join(CUR_PATH,'atams_config.db')
BAK_DB_NAME = os.path.join(BAK_PATH,'atams_config.db')

print CUR_PATH, CUR_DB_NAME
print BAK_PATH, BAK_DB_NAME

SDKFunctions.EphemerisTLEs(str.encode(SDB_FILES_DIR), byref(Ephemeris))

def GetMonitorParams():
	print 'MonitorParams function called'
	global MP_DB_NAME, BAK_DB_NAME, MPdbconn
	# 
	if MPdbconn is not None:
		# Create table if it does not exist					
		result = SQLiteDB_MP.create_table(MPdbconn, MP_TABLE)
		print('succesfully created Monitor Params table')
		cursor = MPdbconn.execute('''SELECT * FROM MonitorParams''')
		rows = len(cursor.fetchall())
		if rows == 0:	# If there are no rows in the table
			# Insert default values into Table
			print('No rows in the table; insert default values to table')
			MPdbconn.execute(MP_INSERT,MP_DEFAULT_SET)
	else:
		print('Cannot create the database connection')

def GetConfigParams():
	print 'ConfigParams function called'
	global CUR_DB_NAME, BAK_DB_NAME, CONFdbconn
	# 
	if CONFdbconn is not None:
		# Create table if it does not exist					
		SQLiteDB_CONF.create_table(CONFdbconn, CONFIG_TABLE)
		print('succesfully created ConfigParams table')
		cursor = CONFdbconn.execute('''SELECT * FROM ConfigParams''')
		rows = len(cursor.fetchall())
		if rows == 0:	# If there are no rows in the table
			# Insert default values into Table
			print('No rows in the table; insert default values to table')
			CONFdbconn.execute(CONFIG_INSERT,CONFIG_DEFAULT_SET)
		
		if os.path.isfile(BAK_DB_NAME):	#If the backup db exists, Copy contents from backup
			try:
				print('Backup DB exists')
				conn = CONFdbconn.cursor()
				conn.execute('''ATTACH DATABASE ? AS ATAMS''', (BAK_DB_NAME,))
				conn.execute('''INSERT or IGNORE INTO ConfigParams SELECT * FROM ATAMS.ConfigParams''')
				conn.execute('''DETACH DATABASE ATAMS''')
				CONFdbconn.commit()
			except:
				CONFdbconn.execute(CONFIG_INSERT,CONFIG_DEFAULT_SET)				
	else:
		print('Cannot create the database connection')
		
def GetIPSettings():
	print 'IPSettings function called'
	global CUR_DB_NAME, BAK_DB_NAME, CONFdbconn
	# 
	if CONFdbconn is not None:
		# Create table if it does not exist					
		SQLiteDB_CONF.create_table(CONFdbconn, IP_TABLE)
		print('succesfully created IPSettings table')
		cursor = CONFdbconn.execute('''SELECT * FROM IPSettings''')
		rows = len(cursor.fetchall())
		if rows == 0:	# If there are no rows in the table
			# Insert default values into Table
			print('No rows in the table; insert default values to table')
			CONFdbconn.execute(IP_INSERT,IP_DEFAULT_SET)
		
		if os.path.isfile(BAK_DB_NAME):	#If the backup db exists, Copy contents from backup
			try:
				print('Backup DB exists')
				conn = CONFdbconn.cursor()
				conn.execute('''ATTACH DATABASE ? AS ATAMS''', (BAK_DB_NAME,))
				conn.execute('''INSERT or IGNORE INTO IPSettings SELECT * FROM ATAMS.IPSettings''')
				conn.execute('''DETACH DATABASE ATAMS''')
				CONFdbconn.commit()
			except:
				CONFdbconn.execute(IP_INSERT,IP_DEFAULT_SET)				
	else:
		print('Cannot create the database connection')

		
# Function to check presence of SDB Files
def SDBFilesPresenceCheck(files_dir):

	global prevstat_sch, prevstat_chn, prevstat_eph, prevstat_spc

	iFileCount = 0
	if(os.path.isfile(os.path.join(files_dir, 'channels'))):		# check if channels file exists or not
		iFileCount += 1
	if(os.path.isfile(os.path.join(files_dir, 'schedule'))):		# check if schedule file exists or not
		iFileCount += 1
	if(os.path.isfile(os.path.join(files_dir, 'ephemeris'))):		# check if ephemeris file exists or not
		iFileCount += 1
	if(os.path.isfile(os.path.join(files_dir, 'spacecraft'))):		# check if spacecraft file exists or not
		iFileCount += 1
		
	if iFileCount == 4:
		prevstat_sch = os.stat(os.path.join(files_dir,'schedule')).st_mtime
		prevstat_chn = os.stat(os.path.join(files_dir,'channels')).st_mtime
		prevstat_eph = os.stat(os.path.join(files_dir,'ephemeris')).st_mtime
		prevstat_spc = os.stat(os.path.join(files_dir,'spacecraft')).st_mtime
		return True
	else:
		return False		


# Validate and Parse all SDB files parameters
def ValidateSDBFiles(SDBPath):

	global SDKFunctions, iEpochTime, bFirstChannelsEffectivityCheck, ChannelPlan, Ephemeris, Spacecraft, SDB_VALID_DIR

	[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDBPath))	# Check validity
	if not Valid:
		return Output
	
	TempChannelPlan = CHANNELPLAN()
	ChannelsParams(str.encode(SDBPath), strChannelID, TempChannelPlan)
	if (TempChannelPlan.ret == -1):
		return TempChannelPlan.strError
		
	# parse channels parameters based on effectivity time
	if (iEpochTime < TempChannelPlan.dwEffectivity):
		# Initially if channels file has future effectivity time, pause simulation and wait for future effectivity time
		if bFirstChannelsEffectivityCheck:
			bFirstChannelsEffectivityCheck = False
			#statuslogger.critical('INIT  - the current channels file has future effectivity time - waiting in idle mode until effectivity time')
			print 'INIT  - the current channels file has future effectivity time - waiting in idle mode until effectivity time'
			time.sleep(TempChannelPlan.dwEffectivity - iEpochTime)
			ChannelPlan = TempChannelPlan            # update main ChannelPlan structure
	else:	# If channels effectivity time is less than test time, parse channels parameters
		bFirstChannelsEffectivityCheck = False
		ChannelsParams(str.encode(SDBPath), strChannelID, ChannelPlan)   
		if (ChannelPlan.ret == -1):
			return ChannelPlan.strError
		
	# parse Schedule File
	[Valid, Output, strAction, dwStartTime, dwHandoverTime,dwEndtime] = ScheduleValidity(str.encode(SDBPath), ChannelPlan.Channel.Satellite.strBeamID, iEpochTime, False)
	if not Valid:
		return Output
	
	print Valid, Output, strAction, dwStartTime, dwHandoverTime,dwEndtime
	
	[Valid,Output] = EphemerisValidity(str.encode(SDBPath)) #check Validity of Ephemeris file
	if not Valid:
		return Output
	
	print Valid,Output
	
	# parse ephemeris TLEs
	SDKFunctions.EphemerisTLEs(str.encode(SDBPath), byref(Ephemeris))
	if (Ephemeris.ret == -1):
		return Ephemeris.strError

		
	'''
	# parse spacecraft parameters
	SDKFunctions.SpacecraftParams(str.encode(SDBPath), byref(Spacecraft))
	if (Spacecraft.ret == -1):
		return Spacecraft.strError
	'''
	return False

	
def ScheduleHOSecCheck():
	global SDB_FILES_DIR, ChannelPlan, iAntennaMode, bHOSEC, iHOACT, iEpochTime,FScheduleEndTime, bNewSchedule
	
	schtype = 'old'
	[OLDSCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(str.encode(SDB_FILES_DIR),ChannelPlan.Channel.Satellite.strBeamID, iEpochTime,0,schtype)
	OLDSCH.sort(order='dwStartTime')
	
	OLDSCH[-1]['dwEndTime'] = OLDSCH[-1]['dwEndTime']-iPeriod
	OldSATStart1 = OLDSCH[0]['dwStartTime']
	OldSATEnd1 = OLDSCH[-1]['dwEndTime']
	OldSATStart2 = OLDSCH[1]['dwStartTime']
	OldSATEnd2 = OLDSCH[0]['dwEndTime']
	
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(OldSATStart1))),'OldSATStart1'
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(OldSATEnd1))),'OldSATEnd1'
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(OldSATStart2))),'OldSATStart2'
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(OldSATEnd2))),'OldSATEnd2'

	
	schtype = 'new'
	[NEWSCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(str.encode(SDB_FILES_DIR),ChannelPlan.Channel.Satellite.strBeamID, iEpochTime,0,schtype)
	NEWSCH.sort(order='dwStartTime')
	NEWSCH[-1]['dwEndTime'] = NEWSCH[-1]['dwEndTime']-iPeriod
	NewSATStart1 = NEWSCH[0]['dwStartTime']
	NewSATEnd1 = NEWSCH[-1]['dwEndTime']
	NewSATStart2 = NEWSCH[1]['dwStartTime']
	NewSATEnd2 = NEWSCH[0]['dwEndTime']
	print 'ScheduleHOSecCheck called'
	
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(NewSATStart1))),'NewSATStart1'
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(NewSATEnd1))),'NewSATEnd1'
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(NewSATStart2))),'NewSATStart2'
	print str.encode(time.strftime('%H:%M:%S', time.gmtime(NewSATEnd2))),'NewSATEnd2'

	
	if (OldSATStart1 < time.time() < OldSATEnd1):
		bHOSEC = True
		iHOACT = OldSATEnd1+1
		print ('[SDB       ] - New Schedule file is in Handover Section; takes effect at %s' %(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(iHOACT))))
	elif (OldSATStart2 < time.time() < OldSATEnd2):
		bHOSEC = True
		iHOACT = OldSATEnd2+1
		print ('[SDB       ] - New Schedule file is in Handover Section; takes effect at %s' %(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(iHOACT))))
	elif (NewSATStart1 < time.time() < NewSATEnd1): 
		bHOSEC = True
		iHOACT = NewSATEnd1+1
		print ('[SDB       ] - New Schedule file is in Handover Section; takes effect at %s' %(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(iHOACT))))
	elif (NewSATStart2 < time.time() < NewSATEnd2):
		bHOSEC = True
		iHOACT = NewSATEnd2+1
		print ('[SDB       ] - New Schedule file is in Handover Section; takes effect at %s' %(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(iHOACT))))
	else:
		bHOSEC = False
		iHOACT = 0
		print 'Schedule HO check else case'
		#ConfigParams.SchUploadTime = iEpochTime	
		#MonitorParams.iUploadTimeAnt = MonitorParams.iCurrentAntenna		
		bNewSchedule = True
		ModeChangeDecisions()
		if time.time() < NewSATEnd1:
			FScheduleEndTime = NewSATEnd1
		else:
			FScheduleEndTime = NewSATEnd2	
		print FScheduleEndTime,NewSATEnd1,NewSATEnd2,bNewSchedule,'FScheduleEndTime'
# Check whether new SDB files are uploaded				
def NewSDBFileCheck():

	global prevstat_chn, prevstat_sch, prevstat_eph, prevstat_spc, SDB_VALID_DIR, SDB_FILES_DIR, ChannelPlan, bChannel_Future
	global bPastADDSchedule, bPastPURGESchedule, bHOSEC,iHOACT, iEpochTime, bNewSchedule,FScheduleEndTime

	curstat_sch = os.stat(os.path.join(SDB_VALID_DIR,'schedule')).st_mtime
	curstat_chn = os.stat(os.path.join(SDB_VALID_DIR,'channels')).st_mtime
	curstat_eph = os.stat(os.path.join(SDB_VALID_DIR,'ephemeris')).st_mtime
	curstat_spc = os.stat(os.path.join(SDB_VALID_DIR,'spacecraft')).st_mtime

	#print iEpochTime,'iEpochTime.....'
	if prevstat_chn != curstat_chn:		# If New channels file is found
		if not filecmp.cmp(os.path.join(SDB_VALID_DIR,'channels'),os.path.join(SDB_FILES_DIR,'channels')): # If uploaded file is different from internal file
			[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDB_VALID_DIR))	# Check validity			if Valid == False:
			if Valid == False:
				print ('[SDB       ] - channels file ERROR  - %s', Output)
			else:
				#ConfigParams.strChannelID = strChannelID
				if (iEpochTime < dwEffectivity):   # when effectivity time is more than the current time
					bChannel_Future = True
					print ('[SDB       ] - Channel file with Future effecitivity time %s Found'  %((str.encode(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dwEffectivity))))))
				else:	# Replace channels file immediately, parse during next pass, If new file needs to be parsed immediately, call parsing here
					bChannel_Future = False
					shutil.copyfile(os.path.join(SDB_VALID_DIR,'channels'), os.path.join(SDB_FILES_DIR,'channels'))
					#ChannelsParams(str.encode(SDBFilesPath), ConfigParams.strChannelID, byref(ChannelPlan))
					print ('[SDB       ] - channels file with past Effecitivity Time received and activated - old file replaced')
					
		else:		# If uploaded file is same as internal file
			bChannel_Future = False
			print('[SDB       ] - received channels file is identical to the current channels file')
		prevstat_chn = curstat_chn
	
	if bChannel_Future:      # Replace New Channel files to SDBFiles Directory when Current time exceeds Channel Future effecitivity time
		[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDB_VALID_DIR))
		if (iEpochTime >= dwEffectivity):
			bChannel_Future = False
			shutil.copyfile(os.path.join(SDB_VALID_DIR,'channels'), os.path.join(SDB_FILES_DIR,'channels'))
			#ChannelsParams(str.encode(SDBFilesPath), ConfigParams.strChannelID, byref(ChannelPlan))
			print ('[SDB       ] - new channels file activated at Effectivity Time - old file replaced')
	
	
	if prevstat_sch != curstat_sch:		# If New schedule file is found
		if bNewSchedule:
			strSch = 'new_schedule'
		else:
			strSch = 'schedule'
		if not filecmp.cmp(os.path.join(SDB_VALID_DIR,'schedule'),os.path.join(SDB_FILES_DIR,strSch)): # If uploaded file is different from internal file
			[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDB_FILES_DIR))
			[Valid, Output,strAction,dwStartTime,dwHandovertime,dwEndtime] = ScheduleValidity(str.encode(SDB_VALID_DIR),strBeamID, iEpochTime,False)
			if (Valid == False):
				print ('[SDB       ] - schedule file invalid - %s',Output)
			else:
				shutil.copyfile(os.path.join(SDB_VALID_DIR,'schedule'), os.path.join(SDB_FILES_DIR,'new_schedule'))
				print iEpochTime,dwStartTime,'iEpochTime'
				if iEpochTime < dwStartTime:
					print ('[SDB       ] - schedule file with Action '+ strAction +' and Future Track Start time received')
					bNewSchedule = True
					bHOSEC = False
					iHOACT = 0
					schtype = 'new'
					[SCH,iPeriod,strAction,iTrackIndex,iSatelliteCount,ret,strError] = ScheduleTracks(str.encode(SDB_FILES_DIR),ChannelPlan.Channel.Satellite.strBeamID, iEpochTime,0,schtype)
					SCH.sort(order='dwStartTime')
					ModeChangeDecisions()
					FScheduleEndTime = SCH[0]['dwHandoverTime']+26
				else:
					print ('[SDB       ] - schedule file with Action '+ strAction +' and Past Track Start time received')
					if strAction == 'ADD':
						bPastADDSchedule = True
					else:
						bPastPURGESchedule = True
					ScheduleHOSecCheck()
		else:
			print('[SDB       ] - received schedule file is identical to the current schedule file')
		prevstat_sch = curstat_sch
		
	if bHOSEC and time.time() >= iHOACT:
		bHOSEC = False
		ScheduleHOSecCheck()
		print 'ScheduleHOSecCheck called'
			
	if bNewSchedule and (time.time() > FScheduleEndTime):
		print 'new schedule file case'
		bNewSchedule = False
		bPastSchedule = False
		#MonitorParams.iUploadTimeAnt = MonitorParams.iCurrentAntenna
		bPastADDSchedule = False
		bPastPURGESchedule = False
		os.remove(os.path.join(SDB_FILES_DIR, 'schedule'))
		shutil.copyfile(os.path.join(SDB_FILES_DIR, 'new_schedule'), os.path.join(SDB_FILES_DIR, 'schedule'))
		os.remove(os.path.join(SDB_FILES_DIR, 'new_schedule'))
		print ('[SDB       ] - new schedule file activated')
	
	if prevstat_eph != curstat_eph:
		if not filecmp.cmp(os.path.join(SDB_VALID_DIR,'ephemeris'),os.path.join(SDB_FILES_DIR,'ephemeris')):	# If uploaded file is different from internal file
			[Valid,Output] = EphemerisValidity(str.encode(SDB_VALID_DIR))			# Check validity
			
			if Valid == False:
				print ('[SDB       ] - ephemeris ERROR - %s' , Output)
			else:
				shutil.copyfile(os.path.join(SDB_VALID_DIR,'ephemeris'), os.path.join(SDB_FILES_DIR,'ephemeris'))	# Replace File
				print('[SDB       ] - new ephemeris file received')
				# parse ephemeris TLEs
				SDKFunctions.EphemerisTLEs(str.encode(SDB_FILES_DIR), byref(Ephemeris))
				if (Ephemeris.ret == -1):
					return Ephemeris.strError
			prevstat_eph = curstat_eph
		else:	# If uploaded file is same as internal file
			print('[SDB       ] - received ephemeris file is identical to internal file')
		prevstat_eph = curstat_eph
	
		
# System Clock Update Thread - Runs at every 1 second
def SystemClockUpdate():
	global iEpochTime, ntp, ntpresponse, OS_VER

	iEpochTime = time.time()	# current system time
	try:
		ntpresponse = ntp.request('pool.ntp.org')
		print ntpresponse,'ntpresponse'
		iNTPEpoch = ntpresponse.tx_time
		print iNTPEpoch,'iNTPEpoch'
		if iNTPEpoch > 100:		# If Valid EpochTime is available from NTP, update system hardware clock
			iEpochTime = iNTPEpoch
			if OS_VER == 'WINDOWS':
				utcTime = datetime.datetime.utcfromtimestamp(iEpochTime)
				win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(), utcTime.day, utcTime.hour, utcTime.minute, utcTime.second, 0)
			else:
				TempDate = 'date -s \'' + time.ctime(ntpresponse.tx_time) + '\''
				os.system(TempDate)
				os.system('hwclock -w')		# Write to hardware clock				
			print('[NTP       ] - Updated System Time: ' + time.ctime(ntpresponse.tx_time) + ' from NTP server')
		else:
			print('[NTP       ] - Unable to update time from NTP server - falback to RTC')
	except:
		print('[NTP       ] - Unable to connect to NTP server')

def ModeChangeDecisions():
	global SCHEVENTS, EventIndex, EventCount, SDB_FILES_DIR, ChannelPlan,strCurrentSatID,strNextSatID,strHwTime,strNextHwTime,bNewSchedule

	EventIndex = 0
	SatEvents = []
	HWEvents = []
	EventCount = 5
	newsch = bNewSchedule
	[SCHEVENTS] = SchEvents(str.encode(SDB_FILES_DIR),ChannelPlan.Channel.Satellite.strBeamID,time.time(),0,newsch,1,time.time(),26)
	print SCHEVENTS
	
	#[SCHEVENTS] = SchEvents(str.encode(SDB_FILES_DIR),ChannelPlan.Channel.Satellite.strBeamID,time.time(),1,False,1,time.time(),26)
	#print SCHEVENTS
	for i in range(len(SCHEVENTS)):
		if SCHEVENTS[i][0].rstrip() == 'Retrace/StartTime':
			SatEvents.append(SCHEVENTS[i]['strSatelliteID'])
			HWEvents.append(SCHEVENTS[i]['dwEpochTime'])
			print SCHEVENTS[i]['dwEpochTime'],SCHEVENTS[i]['strSatelliteID'],i,'dwEpochTime'
	strCurrentSatID = SatEvents[0]
	strNextSatID = SatEvents[1]
	strHwTime = str.encode(time.strftime('%H:%M:%S', time.gmtime(HWEvents[0])))
	strNextHwTime = HWEvents[1]
	print strHwTime,strNextHwTime,'strNextHwTime'
	
	
	
# Exit handler 
def ExitHandler(signum, frame):
	# Create backup of monitor parameters database
	global BAK_DB_NAME,CUR_DB_NAME, CONFdbconn
	print 'Application Exit'

	cursor = CONFdbconn.cursor()
	# Lock database before making a backup
	cursor.execute('begin immediate')
	# Make new backup file
	shutil.copyfile(CUR_DB_NAME, BAK_DB_NAME)
	print ("\nCreating {}...".format(BAK_DB_NAME))
	# Unlock database
	CONFdbconn.rollback()
	CONFdbconn.close()
	sys.exit(1)		
	
if __name__ == '__main__':

	signal.signal(signal.SIGINT, ExitHandler)

	iEpochTime = 0
	EventCount = 5		# Schedule Event Count based on the Mode of Operation
	EventIndex = 0		# Index poiting to Schedule Events table
	temptime = 0
	FScheduleEndTime = 0
	strCurrentSatID = ''
	strNextSatID = ''
	strHwTime = ''
	strNextHwTime = ''
	bNewSchedule = False
	bHOSEC = False
	bChannel_Future = False
	# Create/ connect to existing database
	SQLiteDB_MP = SQLite()
	MPdbconn = SQLiteDB_MP.create_connection(MP_DB_NAME)
	SQLiteDB_CONF = SQLite()
	CONFdbconn = SQLiteDB_CONF.create_connection(CUR_DB_NAME)
	
	# Read Monitor Parameters database	
	GetMonitorParams()
	GetConfigParams()
	GetIPSettings()
	MPdbconn.execute(''' UPDATE MonitorParams SET strATAMSver = ? WHERE id = ? ''', ('0.2',1))
	
	
	# System CLock Update
	ntp = ntplib.NTPClient()
	#print ntp
	iEpochTime = 0
	Timeupdate = 0
	while True:					# Wait unitl system time is updated to current time
		if iEpochTime > 946684800:
			break;
		else:
			SystemClockUpdate()
		time.sleep(1)
	
	if OS_VER != 'WINDOWS':

		#Initialize Rsync daemon
		RsyncPassword = 'o3b'
		SDBSetupRsync(str.encode(SDB_VALID_DIR), str.encode(RsyncPassword))
		with open('/var/log/rsyncd.log','r') as f:
			logstr = f.readlines()
			rsyncmsg = 	logstr[-1].split('\n')
			print rsyncmsg[0],'rsyncmsg'
			#statuslogger.info('[INIT      ] - %s' % rsyncmsg[0])
	
	
	
	# Check SDB files presence 
	bFilePresent = SDBFilesPresenceCheck(SDB_VALID_DIR)	# checks if all the 4 SDB files are present in validation directory
	print bFilePresent,'bFilePresent'
	FilePresenceCount = 0
	while True:
		if bFilePresent:
			break;
		else:
			if FilePresenceCount<4:
				FilePresenceCount = FilePresenceCount + 1
				print ('SDB Files Missing')
			elif FilePresenceCount == 4:
				FilePresenceCount = FilePresenceCount+1
				print('[INIT      ] - SDB files missing; repeated 5 times')
			bFilePresent = SDBFilesPresenceCheck(SDB_VALID_DIR)
		time.sleep(2)
	FilePresenceCount = 0
	print ('[INIT      ] - Found all SDB Files')
	
	# Validate SDB files
	SDBError = ValidateSDBFiles(SDB_VALID_DIR)	# Validate SDB Files	
	SDBMsgcount = 0
	
	while True:									# Wait until SDB files are validated
		if SDBError:
			if SDBMsgcount < 4:
				SDBMsgcount = SDBMsgcount+1
				#statuslogger.critical(SDBError)
				print SDBError
			elif SDBMsgcount == 4:
				SDBMsgcount = SDBMsgcount+1
				print(SDBError)
				print('[INIT      ] - SDB error message is repeated 5 times')
			SDBError = ValidateSDBFiles(SDB_VALID_DIR)		# parse and validate all SDB Files
		else:
			break
		time.sleep(5)
	print('[INIT      ] - Validated SDB Files')	
	
	if os.path.isfile(os.path.join(SDB_FILES_DIR,'channels')):
		os.remove(os.path.join(SDB_FILES_DIR,'channels'))
	shutil.copyfile(os.path.join(SDB_VALID_DIR,'channels'), os.path.join(SDB_FILES_DIR,'channels'))
	if os.path.isfile(os.path.join(SDB_FILES_DIR,'ephemeris')):
		os.remove(os.path.join(SDB_FILES_DIR,'ephemeris'))
	shutil.copyfile(os.path.join(SDB_VALID_DIR,'ephemeris'), os.path.join(SDB_FILES_DIR,'ephemeris'))
	if os.path.isfile(os.path.join(SDB_FILES_DIR,'spacecraft')):
		os.remove(os.path.join(SDB_FILES_DIR,'spacecraft'))
	shutil.copyfile(os.path.join(SDB_VALID_DIR,'spacecraft'), os.path.join(SDB_FILES_DIR,'spacecraft'))
	if not (os.path.isfile(os.path.join(SDB_FILES_DIR,'schedule'))): 	#If there is no file available; Copy existing schedule file
		shutil.copyfile(os.path.join(SDB_VALID_DIR,'schedule'), os.path.join(SDB_FILES_DIR,'schedule'))
	
	if not (os.path.isfile(os.path.join(SDB_FILES_DIR,'new_schedule'))): 	#If there is no file available; assign NewSchedule = False
		FScheduleEndTime = 0
		bNewSchedule = False
	
	if scheduler.running:
		scheduler.shutdown()
	scheduler.start()
	scheduler.add_job(NewSDBFileCheck, 'interval', seconds=2)

	dLat = 0
	dLong = 0
	SatelliteID = 'O3B M001'
	ModeChangeDecisions()
	
	#print SCHEVENTS
	MPdbconn.execute(''' UPDATE MonitorParams SET strCurrentSatID = ? WHERE id = ? ''', (strCurrentSatID,1))
	MPdbconn.execute(''' UPDATE MonitorParams SET strNextSatID = ? WHERE id = ? ''', (strNextSatID,1))
	MPdbconn.execute(''' UPDATE MonitorParams SET strHandoverTime = ? WHERE id = ? ''', (strHwTime,1))
	while True:
		iEpochTime = time.time()
		currentTimeins = math.floor(iEpochTime)	# Current Time in seconds
		SDKFunctions.SatelliteParams(byref(Ephemeris),SatelliteID,str(iEpochTime),byref(StructSatellite))
		dLat = StructSatellite.dLatitude
		dLong = StructSatellite.dLongitude
		#print temptime,currentTimeins,SCHEVENTS[EventIndex]['dwEpochTime']
		if (temptime != currentTimeins) and (currentTimeins == SCHEVENTS[EventIndex]['dwEpochTime']):
			temptime = currentTimeins
			#print SCHEVENTS[EventIndex][0].rstrip() 
			if SCHEVENTS[EventIndex][0].rstrip() == 'MuteTime':	#Mute, End, Retrace, Start and UnMute
				EventIndex += 1
			#print SCHEVENTS[EventIndex][0].rstrip() 
			if SCHEVENTS[EventIndex][0].rstrip() == 'EndTime':
				EventIndex += 1
			#print SCHEVENTS[EventIndex][0].rstrip() ,SCHEVENTS[EventIndex]['dwEpochTime'],currentTimeins
			if (SCHEVENTS[EventIndex][0].rstrip() == 'Retrace/StartTime') and (currentTimeins == SCHEVENTS[EventIndex]['dwEpochTime']):
				strCurrentSatID = SCHEVENTS[EventIndex]['strSatelliteID']
				strNextSatID = SCHEVENTS[EventIndex+EventCount]['strSatelliteID']
				strHwTime = str.encode(time.strftime('%H:%M:%S', time.gmtime(SCHEVENTS[EventIndex]['dwEpochTime'])))
				strNextHwTime = (SCHEVENTS[EventIndex+EventCount]['dwEpochTime'])
				MPdbconn.execute(''' UPDATE MonitorParams SET strCurrentSatID = ? WHERE id = ? ''', (strCurrentSatID,1))
				MPdbconn.execute(''' UPDATE MonitorParams SET strNextSatID = ? WHERE id = ? ''', (strNextSatID,1))
				MPdbconn.execute(''' UPDATE MonitorParams SET strHandoverTime = ? WHERE id = ? ''', (strHwTime,1))
		elif (currentTimeins > SCHEVENTS[EventIndex]['dwEpochTime']):
			EventIndex = EventIndex + 1
		
		if EventIndex >= (len(SCHEVENTS) - 2*EventCount):
			ModeChangeDecisions()
		

		TimeToHw = int(strNextHwTime - int(iEpochTime))
		
		UTCTime = str.encode(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(iEpochTime)))
		MPdbconn.execute(''' UPDATE MonitorParams SET strUTCTime = ? WHERE id = ? ''', (UTCTime,1))
		MPdbconn.execute(''' UPDATE MonitorParams SET dLatitude = ? WHERE id = ? ''', (dLat,1))
		MPdbconn.execute(''' UPDATE MonitorParams SET dLongitude = ? WHERE id = ? ''', (dLong,1))
		MPdbconn.execute(''' UPDATE MonitorParams SET iHandoverCounter = ? WHERE id = ? ''', (TimeToHw,1))
		MPdbconn.commit()
		
		cur = MPdbconn.cursor()
		cur.execute('SELECT * from MonitorParams WHERE id = ?', (1,))
		#print cur.fetchall()
		
		time.sleep(1)