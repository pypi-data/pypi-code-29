'''
---------------------------------------------------

	File name: atams.py

---------------------------------------------------
	Description:   ATAMS Web GUI interface program written using Flask framework 
				   Uses JSON data format for asynchronous browser/server communication
				   Uses memory mapped files to share information with ATAMS main application

---------------------------------------------------	
	Package     : atams
	Version     : 0.1
	Language    : Python
	Authors		: 

Revision History:

Version		Created 			Modification
-----------------------------------------------------------------
'''


from flask import Flask, request, render_template, flash, redirect, url_for, jsonify, send_from_directory,make_response
from werkzeug import secure_filename
import os, time
import platform
from structures import *
from sqliteConn import SQLite
from schevents import SchEvents

from schedulevalidity import ScheduleValidity
from channelsvalidity import ChannelsValidity
from ephemerisvalidity import EphemerisValidity

# Create instance of all structure objects from structures.py file
ChannelPlan 	= CHANNELPLAN()					# create instance of CHANNELPLAN object
Schedule 		= SCHEDULE()					# create instance of SCHEDULE object
Ephemeris 		= EPHEMERIS()					# create instance of EPHEMERIS object
Spacecraft 		= SPACECRAFT()					# create instance of SPACECRAFT object
StructSatellite = STRUCTSATELLITE()				# create instance of STRUCTSATELLITE object

app = Flask(__name__)
OPERATOR_PW = 'O3b'
INSTALLER_PW = 'O3b4u!'

if 'Windows' in platform.platform():
	OS_VER = 'WINDOWS'
elif 'centos' in platform.platform():
	OS_VER = 'CENTOS'
else:
	OS_VER = 'UBUNTU'


if OS_VER == 'WINDOWS':
	CUR_PATH = os.path.join('c:','\ATAMS','atams')
	SDB_VALID_DIR = os.path.join('c:','\ATAMS','SDB_VALID_DIR')
	PACKAGE_DIR = os.path.join('c:','\ATAMS','PACKAGE_DIR')
	SDKFunctions = CDLL(os.path.join(CUR_PATH,'libsdkwindows.so'))
elif OS_VER == 'CENTOS':
	CUR_PATH = '/var/www/html/atams'
	SDB_VALID_DIR = '/etc/atams/sdbfiles'
	PACKAGE_DIR = '/var/cache/yum/armhfp/7/softacu/packages'
	SDKFunctions = CDLL(os.path.join(CUR_PATH,'libo3bsdbsdk.so'))

@app.before_first_request
def Initialization():
	global MPdbconn, cur, CUR_PATH
	
	# Create/ connect to existing database
	MP_DB_NAME = os.path.join(CUR_PATH,'atams_mp.db')
	SQLiteDB = SQLite()
	MPdbconn = SQLiteDB.create_connection(MP_DB_NAME)
	if MPdbconn is not None:
		cur = MPdbconn.cursor()
	else:
		cur = None
	print 'cur', cur

# calling main route
@app.route('/')
def index():
	return render_template("main.html")
	
# Get Time
@app.route('/headerinfo', methods=["GET"])
def headerinfo():

	global cur
	if cur is not None:
		MP_LIST = list(cur.execute('SELECT * from MonitorParams WHERE id = ?', (1,)))[0]
		
		strUTCTime = MP_LIST[1]
		strATAMSver = MP_LIST[2]
		strATAMSStatus = MP_LIST[3]
		dLatitude = round(MP_LIST[4] * 100.0)/100.0
		dLongitude = round(MP_LIST[5] * 100.0)/100.0
		strTrackingMethod = MP_LIST[6]
		strCurrentSatID = MP_LIST[7]
		strNextSatID = MP_LIST[8]
		strHandoverTime = MP_LIST[9]
		iHandoverCounter = MP_LIST[10]
		dFrequency = MP_LIST[11]
		dBandwidth = MP_LIST[12]
		strPol = MP_LIST[13]
		strRxStatus = MP_LIST[14]
		bModManStatus = MP_LIST[15]
		bAntennaStatus = MP_LIST[16]
		
		UTCTime = strUTCTime.split(' ')
		headerinfo = [UTCTime[0], UTCTime[1], strATAMSver]
		MonitorParams = [strATAMSStatus, dLatitude, dLongitude, strTrackingMethod, strCurrentSatID, strNextSatID, strHandoverTime, iHandoverCounter,
													dFrequency, dBandwidth, strPol, strRxStatus, bModManStatus, bAntennaStatus]
		return jsonify(headerinfo = headerinfo, MonitorParams=MonitorParams)

	
@app.route('/HandoverEvents', methods=["GET","POST"])
def HandoverEvents():
	
	global SchEvents, SCHEVENTS
		
	iEpochTime = int(time.time())
	SDBFileDir = '/var/www/html/atams/SDBFiles'
	iMode = 0
	newsch = False
	iCurrentAntenna = 1
	[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDBFileDir))
	#SDKFunctions.ChannelsParams(str.encode(SDBFileDir), strChannelID, byref(ChannelPlan))
	#if not ConfigParams.bNewSchedule:
		#ConfigParams.bPastSchedule = False
		#MonitorParams.iUploadTimeAnt = MonitorParams.iCurrentAntenna
	
	[SCHEVENTS] = SchEvents(str.encode(SDBFileDir),strBeamID,iEpochTime,iMode,newsch,iCurrentAntenna,iEpochTime,26)
	print SCHEVENTS
	strEpochTime, strSettingSatID, strRisingSatID = [], [], []
	for i in range(len(SCHEVENTS)):
		if SCHEVENTS[i][0].rstrip() == 'Retrace/StartTime':
			strEpochTime.append(SCHEVENTS[i]['strEpochTime'])
			strSettingSatID.append(SCHEVENTS[i]['strSatelliteID'])
			strRisingSatID.append(SCHEVENTS[i-1]['strSatelliteID'])
	
	
	
	return jsonify(strEpochTime = strEpochTime, strSettingSatID = strSettingSatID, strRisingSatID = strRisingSatID)
	
	
	
# verify operator password
@app.route('/submitOperatorPW', methods=["GET","POST"])
def submitOperatorPW():
	global OPERATOR_PW
	
	result = False
	if request.method == "POST":
		password = request.json['data']
		if password == OPERATOR_PW:
			result=True
		else:
			result=False
		return jsonify(result)
	else:
		return "error"

# verify installer password
@app.route('/submitInstallerPW', methods=["GET","POST"])
def submitInstallerPW():
	global INSTALLER_PW
	
	result = False
	if request.method == "POST":
		password = request.json['data']
		if password == INSTALLER_PW:
			result=True
		else:
			result=False
		return jsonify(result)
	else:
		return "error"

# Restart Software
@app.route('/restartSoftware', methods=["GET","POST"])
def restartSoftware():
	if request.method == "POST":
		restartButton = request.json['data']
		#print restartButton,'restartButton'
		if restartButton == 1 :
			result = 'successfully sent command to Modman AMIP'
		elif restartButton == 2:
			result = 'successfully sent command to Modman API'
		elif restartButton == 3:
			result = 'successfully sent command to Antenna AMIP'
		elif restartButton == 4:
			result = 'successfully restarted ATAMS Software'
		elif restartButton == 5:
			result = 'successfully restrted ATAMS GUI'
		print result,'print result'
		return jsonify(result)
	else:
		return "error"
	
		
		
# Upload SDB files
@app.route('/uploadSDB', methods=["GET","POST"])
def uploadSDB():

	global SDB_VALID_DIR, OS_VER

	strAction = ''
	schresult = 'schedule file is not selected'
	chnresult = 'channels file is not selected'
	ephresult = 'ephemeris file is not selected'
	spcresult = 'spacecraft file is not selected'
	bSchedule,bChannels,bEphemeris,bSpacecraft = False,False,False,False

	iEpochTime = time.time()

	for file in request.files.getlist("chnfile"):
		filename = secure_filename(file.filename)
		#destination = "/".join([SDB_VALID_DIR, filename])
		destination = os.path.join(SDB_VALID_DIR,filename)
		file.save(destination)
		if (OS_VER == 'WINDOWS') and (os.path.isfile(os.path.join(SDB_VALID_DIR,'channels'))):
			os.remove(os.path.join(SDB_VALID_DIR,'channels'))
			#windll.kernel32.MoveFileExW(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'channels'), 0x1)
		#else:
		os.rename(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'channels'))
		[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDB_VALID_DIR))	# Check validity
		if (Valid == False):
			chnresult = 'Channels File Error: '+Output
			bChannels = False
		else:
			chnresult = 'Channels File upload successful'
			bChannels = True
	for file in request.files.getlist("schfile"):
	
		filename = secure_filename(file.filename)
		#destination = "/".join([SDB_VALID_DIR, filename])
		destination = os.path.join(SDB_VALID_DIR,filename)
		file.save(destination)
		if (OS_VER == 'WINDOWS') and (os.path.isfile(os.path.join(SDB_VALID_DIR,'schedule'))):
			os.remove(os.path.join(SDB_VALID_DIR,'schedule'))
			#windll.kernel32.MoveFileExW(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'schedule'), 0x1)
		#else:
		os.rename(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'schedule'))
		[Valid,Output,dwEffectivity,strChannelID,strBeamID] = ChannelsValidity(str.encode(SDB_VALID_DIR))	# Check validity
		#SDKFunctions.ChannelsParams(str.encode(SDBFILES_DIRECTORY), strChannelID, byref(ChannelPlan))
		[Valid, Output,strAction,dwStartTime,dwHandovertime,dwEndtime] = ScheduleValidity(str.encode(SDB_VALID_DIR),strBeamID,iEpochTime,False)
		if (Valid == False):
			schresult = Output
			bSchedule = False
		else:
			if iEpochTime < dwStartTime:
				schresult = 'Schedule File with Action '+ strAction +' and Future time Uploaded'
			else:
				schresult = 'Schedule File with Action '+ strAction +' and Past time Uploaded'
			bSchedule = True

	for file in request.files.getlist("ephfile"):
		
		filename = secure_filename(file.filename)
		#destination = "/".join([SDB_VALID_DIR, filename])
		destination = os.path.join(SDB_VALID_DIR,filename)
		file.save(destination)
		if (OS_VER == 'WINDOWS') and (os.path.isfile(os.path.join(SDB_VALID_DIR,'ephemeris'))):
			os.remove(os.path.join(SDB_VALID_DIR,'ephemeris'))
			#windll.kernel32.MoveFileExW(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'ephemeris'), 0x1)
		#else:
		os.rename(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'ephemeris'))
		[Valid,Output] = EphemerisValidity(str.encode(SDB_VALID_DIR))
		if Valid == False:
			ephresult = Output
			ephresult = 'Ephemeris File Error: '+ephresult
			bEphemeris = False
		else:
			ephresult = 'Ephemeris File upload successful'
			bEphemeris = True
		
	for file in request.files.getlist("spcfile"):
		filename = secure_filename(file.filename)
		#destination = "/".join([SDB_VALID_DIR, filename])
		destination = os.path.join(SDB_VALID_DIR,filename)
		file.save(destination)
		windll.kernel32.MoveFileExW(os.path.join(SDB_VALID_DIR,filename),os.path.join(SDB_VALID_DIR,'spacecraft'), 0x1)
		#os.rename(SDB_VALID_DIR+'/'+filename,SDB_VALID_DIR+'/spacecraft')
		'''
		SDKFunctions.SpacecraftParams(str.encode(SDB_VALID_DIR), byref(Spacecraft))
		if (Spacecraft.ret == -1):
			spcresult = Spacecraft.strError
			spcresult = 'Spacecraft File Error: '+spcresult
			bSpacecraft = False
		else:
			spcresult = 'Spacecraft File upload successful'
			bSpacecraft = True
		'''

	sdbresult = [schresult,chnresult,ephresult,spcresult]
	
	return jsonify(result=sdbresult)

# validate software file
@app.route('/checkSW', methods=["GET","POST"])
def checkSW():
	swresult = 0 # Software File is not selected
	uploadedver = 0
	currentver = 0.1 #int(float(softacuver)*1000)

	for file in request.files.getlist("swfile"):
		filename = secure_filename(file.filename).encode()
		if filename.find('atams') is 0:
			swresult = 1
			'''
			uploadedver = filename.split('.')[0]
			uploadedverf = float(uploadedver.split('-')[1]+'.'+uploadedver.split('-')[2])
			uploadedver = int(uploadedverf * 1000)
			if uploadedver == currentver:
				swresult = 1
			elif uploadedver > currentver:
				swresult = 2
			if uploadedver < currentver:
				swresult = 3
			'''	
	return jsonify (swresult = swresult, ver = currentver)

# upload software
@app.route('/uploadSW', methods=["GET","POST"])
def uploadSW():
	global PACKAGE_DIR, CWD
	
	for file in request.files.getlist("swfile"):
		filename = secure_filename(file.filename).encode()
		if filename.find('atams') is 0:
			file.save(PACKAGE_DIR + filename)
			
	return jsonify()


	
if __name__ == "__main__":
	app.run()