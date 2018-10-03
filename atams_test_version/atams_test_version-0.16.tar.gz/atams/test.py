from ctypes import *
import os, time
from structures import *
from ChannelParams import ChannelsParams

# Create instance of all structure objects from structures.py file
ChannelPlan 	= CHANNELPLAN()					# create instance of CHANNELPLAN object
Schedule 		= SCHEDULE()					# create instance of SCHEDULE object
Ephemeris 		= EPHEMERIS()					# create instance of EPHEMERIS object
Spacecraft 		= SPACECRAFT()					# create instance of SPACECRAFT object
StructSatellite = STRUCTSATELLITE()				# create instance of STRUCTSATELLITE object


SDKLIB_PATH = os.path.join('c:','\ATAMS','atams')
SDB_FILES_DIR = os.path.join('c:','\ATAMS','atams','SDBFiles')

ChannelPlan.strError = 'Error'
print ChannelPlan.strError

ChannelsParams(str.encode(SDB_FILES_DIR), 'USA_APX_001_01', ChannelPlan)


print SDB_FILES_DIR
print SDKLIB_PATH + '\libsdkwindows.so'
SDKFunctions = cdll.LoadLibrary(SDKLIB_PATH + '\libsdkwindows.so')

SDKFunctions.EphemerisTLEs(str.encode(SDB_FILES_DIR), byref(Ephemeris))
print Ephemeris.EphemerisArray[0].strSatelliteID
if (Ephemeris.ret == -1):
	print Ephemeris.strError


while True:
	iEpochTime = int(time.time())
	SDKFunctions.SatelliteParams(byref(Ephemeris),'O3B M006',str(iEpochTime),byref(StructSatellite))
	dLat = StructSatellite.dLatitude
	dLong = StructSatellite.dLongitude

	print iEpochTime, dLat, dLong
	
	time.sleep(0.1)
