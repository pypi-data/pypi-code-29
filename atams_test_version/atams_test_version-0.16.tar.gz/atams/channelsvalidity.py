'''
---------------------------------------------------

	File name: channelsvalidity.py

---------------------------------------------------
	Description:   Validates channels file by verfying file format and 13 fields
				   If any field is not present returns that particular error

---------------------------------------------------	
	Package     : atams
	Version     : 0.1
	Language    : Python
	Authors		: 

Revision History:

Version		Created 			Modification
-----------------------------------------------------------------
'''

from structures import *
import time
import os
import xml.etree.ElementTree as ET

def ChannelsValidity(ChannelsFilepath):
	count = 0
	Output = ''
	strChannelID = ''
	strBeamID = ''
	dwEffectivity = ''
	Valid = False
	bLocalSiteLatitude = bLocalSiteLongitude = bLocalSiteAltitude = bPeerSiteLatitude = bPeerSiteLongitude = bPeerSiteAltitude = bBeam = bUplinkModemFreq = bUplinkRfFreq = bUplinkRate = bDownlinkModemFreq = bDownlinkRfFreq = bDownlinkRate = False
	ChannelsFilepath = os.path.join(ChannelsFilepath, 'channels')
	try:
		tree = ET.parse(ChannelsFilepath)
	except:
		Output = 'Invalid Channel File'
		Valid = False
		return [Valid,Output,dwEffectivity,strChannelID,strBeamID]
	root = tree.getroot()
	if root.tag == 'ChannelPlan':
		effectivity_time = root.attrib.get('Effectivity')
		pattern = '%m/%d/%Y %H:%M:%S'
		dwEffectivity = int(time.mktime(time.strptime(effectivity_time, pattern)))
		for node in  tree.iter('LocalSite'):
			if node.find('SiteType') is not None:
				strSiteType = node.find('SiteType').text
			if node.find('SiteId') is not None:
				strSite = node.find('SiteId').text
			if node.find('Lat') is not None:
				dLatitude = float(node.find('Lat').text)             #	Local Site Latitude
				bLocalSiteLatitude = True
				count = count+1
			if node.find('Lon') is not None:
				dLongitude = float(node.find('Lon').text)            #	Local Site Longitude
				bLocalSiteLongitude = True
				count = count+1
			if node.find('Alt') is not None:
				dAltitude = float(node.find('Alt').text)             #	Local Site Altitude
				bLocalSiteAltitude = True
				count = count+1
		
					
		for node1 in root.findall('Channel'):
			if root.find('Channel') is not None:
				strChannelID = node1.attrib.get('Id')
				for node2 in node1.iter('PeerSite'):
					if node2.find('SiteType') is not None:
						strSiteType = node2.find('SiteType').text
					if node2.find('SiteId') is not None:
						strSite = node2.find('SiteId').text
					if node2.find('Lat') is not None:
						dLatitude = float(node2.find('Lat').text)   #	Peer Site Latitude
						bPeerSiteLatitude = True
						count = count+1
					if node2.find('Lon') is not None: 
						dLongitude = float(node2.find('Lon').text)  #	Peer Site Longitude
						bPeerSiteLongitude = True
						count = count+1
					if node2.find('Alt') is not None:
						dAltitude = float(node2.find('Alt').text)    #	Peer Site Altitude
						bPeerSiteAltitude = True
						count = count+1
				if node1.find('Region') is not None:     # Region Tag
					strRegion = node1.find('Region').text
				else:
					Output = '<Region> tag not found'
					Valid = False
					return [Valid,Output,dwEffectivity,strChannelID,strBeamID]
					
				for node3 in node1.iter('Satellite'):
					strID = node3.attrib.get('Id')
					if node3.iter('Beam'):
						if node3.find('Beam') is not None:
							strBeamID = node3.find('Beam').text		# Beam ID
							bBeam = True
							count = count+1
					for node4 in node3.iter('Uplink'):
						if node4.find('ModemFreq') is not None:
							UPlink_dModemFrequency = float(node4.find('ModemFreq').text)   #	Modem Frequency
							bUplinkModemFreq = True
							count = count+1
						if node4.find('RfFreq') is not None:
							UPlink_dRfFrequency = float(node4.find('RfFreq').text)         #	RF Frequency
							bUplinkRfFreq = True
							count = count+1
						if node4.find('SatLo') is not None:
							UPlink_dSatLo = float(node4.find('SatLo').text)
						if node4.find('Rate').text:
							Uplink_dRate = float(node4.find('Rate').text)  #	Uplink Rate
							bUplinkRate = True
							count = count+1
						if node4.find('Pol') is not None:
							Uplink_strPol= node4.find('Pol').text
						if node4.find('Power') is not None:
							Uplink_dPower = float(node4.find('Power').text)
					for node5 in node3.iter('Downlink'):
						if node5.find('ModemFreq') is not None:
							Downlink_dModemFrequency = float(node5.find('ModemFreq').text)     #	Downlink 
							bDownlinkModemFreq = True
							count = count+1
						if node5.find('RfFreq') is not None:
							Downlink_dRfFrequency = float(node5.find('RfFreq').text)           #	Downlink RF Frquency
							bDownlinkRfFreq = True
							count = count+1
						if node5.find('SatLo') is not None:
							Downlink_dSatLo = float(node5.find('SatLo').text)
						if node5.find('Rate') is not None:
							Downlink_dRate = float(node5.find('Rate').text)                    #	Downlink Rate
							bDownlinkRate = True
							count = count+1
						if node5.find('Pol') is not None:
							Downlink_strPol= node5.find('Pol').text
			else:
				Output = 'channel ID tag not found'
				Valid = False
				return [Valid,Output,dwEffectivity,strChannelID,strBeamID]				
	else:
		Output = 'channel plan tag is not found'
		Valid = False
		return [Valid,Output,dwEffectivity,strChannelID,strBeamID]
	if (count == 13):    #if required parameters found in channels file, return zero error in channelplan structure
		Valid = True
		Output = True
		return [Valid,Output,dwEffectivity,strChannelID,strBeamID]
	elif (count == 3):    #if required parameters found in channels file, return zero error in channelplan structure
		Valid = False
		Output = 'Channel ID tag not found'
		return [Valid,Output,dwEffectivity,strChannelID,strBeamID]
	elif count > 13:
		Valid = False
		Output = 'More than one channel ID found in channels file'
		return [Valid,Output,dwEffectivity,strChannelID,strBeamID]		
	else:
		Valid = False
		if not bLocalSiteLatitude:
			Output = '<LocalSite><Lat> tag not found'
		elif not bLocalSiteLongitude:
			Output = '<LocalSite><Lon> tag not found'
		elif not bLocalSiteAltitude:
			Output = '<LocalSite><Alt> tag not found'
		elif not bBeam:
			Output = '<Beam> tag not found'
		elif not bPeerSiteLatitude:
			Output = '<PeerSite><Lat> tag not found'
		elif not bPeerSiteLongitude:
			Output = '<PeerSite><Lon> tag not found'
		elif not bPeerSiteAltitude:
			Output = '<PeerSite><Alt> tag not found'
		elif not bUplinkModemFreq:
			Output = '<Uplink><ModemFreq> tag not found' 
		elif not bUplinkRfFreq:
			Output = '<Uplink><RfFreq> tag not found'
		elif not bUplinkRate:
			Output = '<Uplink><Rate> tag not found'
		elif not bDownlinkModemFreq:
			Output = '<Downlink><ModemFreq> tag not found'
		elif not bDownlinkRfFreq:
			Output = '<Downlink><RfFreq> tag not found'
		elif not bDownlinkRate:
			Output = '<Downlink><Rate> tag not found'
		return [Valid,Output,dwEffectivity,strChannelID,strBeamID]
