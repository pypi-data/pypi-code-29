'''
---------------------------------------------------

	File name: structures.py

---------------------------------------------------
	Description:   

---------------------------------------------------	
	Package     : 
	Version     : 
	Language    : Python
	Authors		: 

Revision History:

Version		Created 			Modification
-----------------------------------------------------------------
'''

#! python

from ctypes import *

''' Sub-strucutre UPLINK '''
class UPLINK(Structure):
	_fields_ = [("strPol", c_char * 16), ("dModemFrequency", c_double), ("dRfFrequency", c_double), ("dSatLo", c_double), ("dRate", c_double), ("dPower", c_double)] 

''' Sub-strucutre DOWNLINK '''
class DOWNLINK(Structure):
	_fields_ = [("strPol", c_char * 16), ("dModemFrequency", c_double), ("dRfFrequency", c_double), ("dSatLo", c_double), ("dRate", c_double)]

''' Sub-structure SATELLITE '''
class SATELLITE(Structure):
	_fields_ = [("Uplink", UPLINK), ("Downlink", DOWNLINK), ("strID", c_char * 16), ("strBeamID", c_char * 8), ("iBeam", c_int)]

''' Sub-structure CHANNELSITE '''
class CHANNELSITE(Structure):
	_fields_ = [("strSiteType", c_char * 16), ("strSite", c_char * 16), ("dLatitude", c_double), ("dLongitude", c_double), ("dAltitude", c_double)]

''' Sub-structure CHANNEL '''
class CHANNEL(Structure):
	_fields_ = [("Satellite", SATELLITE), ("PeerSite", CHANNELSITE), ("strID", c_char * 16), ("strRegion", c_char * 16)]

''' Structure CHANNELPLAN '''
class CHANNELPLAN(Structure):
	_fields_ = [("strError", c_char * 128), ("Channel", CHANNEL), ("LocalSite", CHANNELSITE), ("dwEffectivity", c_ulong), ("ret", c_int)]

''' Sub-strucutre HANDOVER '''
class HANDOVER(Structure):
	_fields_ = [("strTime", c_char * 20), ("strRegion", c_char * 16), ("strBeam", c_char * 8), ("dwTime", c_ulong), ("dwRealTime", c_ulong)]

''' Sub-structure Track '''
class TRACK(Structure):
	_fields_ = [("Handover", HANDOVER), ("strPrePassTime", c_char * 20), ("strStartTime", c_char * 20), ("strEndTime", c_char * 20), ("strSatelliteID", c_char * 16), ("dwPrePassTime", c_ulong), 
				 ("dwRealPrePassTime", c_ulong), ("dwStartTime", c_ulong), ("dwEndTime", c_ulong)]

''' Strucutre SCHEDULE '''
class SCHEDULE(Structure):
	_fields_ = [("Track", TRACK * 32), ("strError", c_char * 128), ("strPeriod", c_char * 16), ("strAction", c_char * 8), ("iPeriod", c_uint), ("iTrackIndex", c_int), ("iSatelliteCount", c_int), 
				("ret", c_int)]

''' Sub-structure EphemerisArray '''
class EPHEMERISARRAY(Structure):
	_fields_ = [("strLine1", c_char * 128), ("strLine2", c_char * 128), ("strSatelliteID", c_char * 16)]

''' Structure EPHEMERIS '''
class EPHEMERIS(Structure):
	_fields_ = [("EphemerisArray", EPHEMERISARRAY * 32), ("strError", c_char * 128), ("iSatelliteCount", c_int), ("ret", c_int)]

''' Sub-strucutre SPACECRAFTARRAY '''
class SPACECRAFTARRAY(Structure):
	_fields_ = [("strSatelliteID", c_char * 16), ("strBeaconFreqPri", c_char * 16), ("strBeaconFreqSec", c_char * 16), ("strBeaconPolPri", c_char * 16), ("strBeaconPolSec", c_char * 16), 
				("dBeaconFreqPri", c_double), ("dBeaconFreqSec", c_double)]

''' Structure SPACECRAFT '''
class SPACECRAFT(Structure):
	_fields_ = [("SpacecraftArray", SPACECRAFTARRAY * 32), ("strError", c_char * 128), ("iSatelliteCount", c_int), ("ret", c_int)]

''' Structure STRUCTSATELLITE '''
class STRUCTSATELLITE(Structure):
	_fields_ = [("ro", c_double * 3), ("vo", c_double * 3), ("dLatitude", c_double), ("dLongitude", c_double), ("dAltitude", c_double), ("gsrt", c_double)]

MP_TABLE = """ CREATE TABLE IF NOT EXISTS MonitorParams (
					id integer PRIMARY KEY,
					strUTCTime string NOT NULL,
					strATAMSver string NOT NULL,
					strATAMSStatus string NOT NULL,
					dLatitude float NOT NULL,
					dLongitude float NOT NULL,
					strTrackingMethod string NOT NULL,
					strCurrentSatID string NOT NULL,
					strNextSatID string NOT NULL,
					strHandoverTime string NOT NULL,
					iHandoverCounter int NOT NULL,
					dFrequency float NOT NULL,
					dBandwidth float NOT NULL,
					strPol string NOT NULL,
					strRxStatus string NOT NULL,
					bModManStatus bool NOT NULL,
					bAntennaStatus bool NOT NULL
				); """
				
MP_INSERT = ''' INSERT INTO MonitorParams (strUTCTime, strATAMSver, strATAMSStatus, dLatitude, dLongitude, 
											strTrackingMethod, strCurrentSatID, strNextSatID, strHandoverTime, iHandoverCounter,
												dFrequency, dBandwidth, strPol, strRxStatus, bModManStatus, bAntennaStatus)
						VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
						
MP_DEFAULT_SET = ('00:00:00','0.1',0,248,'Running','MEO','O3B M001','O3B M002','00:30:00',0,1270,35,'LHCP','UnLocked',False,False)

CONFIG_TABLE = """ CREATE TABLE IF NOT EXISTS ConfigParams (
					id integer PRIMARY KEY,
					iAPImsgfreq int NOT NULL,
					iAMIPmsgfreq int NOT NULL,
					bATAMSRestart bool NOT NULL,
					bATAMSGUIRestart bool NOT NULL,
					bModManAPIRestart bool NOT NULL,
					bModManAMIPRestart bool NOT NULL,
					bAntennaAMIPRestart bool NOT NULL
				); """
CONFIG_INSERT = ''' INSERT INTO ConfigParams (iAPImsgfreq, iAMIPmsgfreq, bATAMSRestart, bATAMSGUIRestart, bModManAPIRestart,
												bModManAMIPRestart, bAntennaAMIPRestart)
						VALUES(?,?,?,?,?,?,?) '''
						
CONFIG_DEFAULT_SET = (10,1,False,False,False,False,False)

IP_TABLE = """ CREATE TABLE IF NOT EXISTS IPSettings (
					id integer PRIMARY KEY,
					NTPIP string NOT NULL,
					ModManIP string NOT NULL,
					AntennaIP string NOT NULL,
					ModManAMIPPort string NOT NULL,
					AntennaAMIPPort string NOT NULL,
					ModManAPIPort string NOT NULL
				); """
IP_INSERT = ''' INSERT INTO IPSettings (NTPIP, ModManIP, AntennaIP, ModManAMIPPort, AntennaAMIPPort, ModManAPIPort)
						VALUES(?,?,?,?,?,?) '''
						
IP_DEFAULT_SET = ('pool.ntp.org','192.168.1.70','192.168.1.80',6200,6200,6300)

