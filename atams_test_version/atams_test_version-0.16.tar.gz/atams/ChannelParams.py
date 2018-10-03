from structures import *
import os, time
import xml.etree.ElementTree as ET

def ChannelsParams(ChannelsFilepath, ChannelID, ChannelPlan):
	#print(ChannelsFilepath, ChannelID, ChannelPlan)
	count = 0
	bLocalSiteLatitude = bLocalSiteLongitude = bLocalSiteAltitude = bPeerSiteLatitude = bPeerSiteLongitude = bPeerSiteAltitude = bBeam = bUplinkModemFreq = bUplinkRfFreq = bUplinkRate = bDownlinkModemFreq = bDownlinkRfFreq = bDownlinkRate = False
	#print(ChannelsFilepath, ChannelID, ChannelPlan)
	ChannelsFilepath = os.path.join(ChannelsFilepath, 'channels')
	try:                                                  #spacecraft file Parsing
		tree = ET.parse(ChannelsFilepath)
	except:
		ChannelPlan.strError = 'Invalid Channel File'
		ChannelPlan.ret = -1
		return
	root = tree.getroot()
	if root.tag == 'ChannelPlan':
		effectivity_time = root.attrib.get('Effectivity')
		pattern = '%m/%d/%Y %H:%M:%S'
		ChannelPlan.dwEffectivity = int(time.mktime(time.strptime(effectivity_time, pattern)))
		
		for node in  tree.iter('LocalSite'):
			if node.find('SiteType') is not None:
				ChannelPlan.LocalSite.strSiteType = node.find('SiteType').text
			if node.find('SiteId') is not None:
				ChannelPlan.LocalSite.strSite = node.find('SiteId').text
			if node.find('Lat') is not None:
				ChannelPlan.LocalSite.dLatitude = float(node.find('Lat').text)             #
				bLocalSiteLatitude = True
				count = count+1
			if node.find('Lon') is not None:
				ChannelPlan.LocalSite.dLongitude = float(node.find('Lon').text)            #
				bLocalSiteLongitude = True
				count = count+1
			if node.find('Alt') is not None:
				ChannelPlan.LocalSite.dAltitude = float(node.find('Alt').text)             #
				bLocalSiteAltitude = True
				count = count+1
		
					
		for node1 in root.findall('Channel'):
			ChannelPlan.Channel.strID = node1.attrib.get('Id')
			#print(ChannelPlan.Channel.strID)
			if ChannelID == ChannelPlan.Channel.strID:
				for node2 in node1.iter('PeerSite'):
					if node2.find('SiteType') is not None:
						ChannelPlan.Channel.PeerSite.strSiteType = node2.find('SiteType').text
					if node2.find('SiteId') is not None:
						ChannelPlan.Channel.PeerSite.strSite = node2.find('SiteId').text
					if node2.find('Lat') is not None:
						ChannelPlan.Channel.PeerSite.dLatitude = float(node2.find('Lat').text)   #
						bPeerSiteLatitude = True
						count = count+1
					if node2.find('Lon') is not None: 
						ChannelPlan.Channel.PeerSite.dLongitude = float(node2.find('Lon').text)  #
						bPeerSiteLongitude = True
						count = count+1
					if node2.find('Alt') is not None:
						ChannelPlan.Channel.PeerSite.dAltitude = float(node2.find('Alt').text)    #
						bPeerSiteAltitude = True
						count = count+1
				if node1.iter('Region'):
					ChannelPlan.Channel.strRegion = node1.find('Region').text
				for node3 in node1.iter('Satellite'):
					ChannelPlan.Channel.Satellite.strID = node3.attrib.get('Id')
					#print(ChannelPlan.Channel.Satellite.strID)
					if node3.iter('Beam'):
						if node3.find('Beam') is not None:
							#var = node3.find('Beam').text
							'''
							if var.isdigit() == True:
								#print('int')
								ChannelPlan.Channel.Satellite.strBeamID = node3.find('Beam').text
								ChannelPlan.Channel.Satellite.iBeam = int(ChannelPlan.Channel.Satellite.strBeamID)   #
							else:
								#print('str')
								ChannelPlan.Channel.Satellite.strBeamID = node3.find('Beam').text
							'''
							ChannelPlan.Channel.Satellite.strBeamID = node3.find('Beam').text
							bBeam = True
							count = count+1
					for node4 in node3.iter('Uplink'):
						if node4.find('ModemFreq') is not None:
							ChannelPlan.Channel.Satellite.Uplink.dModemFrequency = float(node4.find('ModemFreq').text)   #
							bUplinkModemFreq = True
							count = count+1
						if node4.find('RfFreq') is not None:
							ChannelPlan.Channel.Satellite.Uplink.dRfFrequency = float(node4.find('RfFreq').text)         #
							bUplinkRfFreq = True
							count = count+1
						if node4.find('SatLo') is not None:
							ChannelPlan.Channel.Satellite.Uplink.dSatLo = float(node4.find('SatLo').text)
						if node4.find('Rate').text:
							ChannelPlan.Channel.Satellite.Uplink.dRate = float(node4.find('Rate').text)  #
							bUplinkRate = True
							count = count+1
						if node4.find('Pol') is not None:
							ChannelPlan.Channel.Satellite.Uplink.strPol= node4.find('Pol').text
						if node4.find('Power') is not None:
							ChannelPlan.Channel.Satellite.Uplink.dPower = float(node4.find('Power').text)
					for node5 in node3.iter('Downlink'):
						if node5.find('ModemFreq') is not None:
							ChannelPlan.Channel.Satellite.Downlink.dModemFrequency = float(node5.find('ModemFreq').text)     #
							bDownlinkModemFreq = True
							count = count+1
						if node5.find('RfFreq') is not None:
							ChannelPlan.Channel.Satellite.Downlink.dRfFrequency = float(node5.find('RfFreq').text)           #
							bDownlinkRfFreq = True
							count = count+1
						if node5.find('SatLo') is not None:
							ChannelPlan.Channel.Satellite.Downlink.dSatLo = float(node5.find('SatLo').text)
						if node5.find('Rate') is not None:
							ChannelPlan.Channel.Satellite.Downlink.dRate = float(node5.find('Rate').text)                    #
							bDownlinkRate = True
							count = count+1
							#print(count)
						if node5.find('Pol') is not None:
							ChannelPlan.Channel.Satellite.Downlink.strPol= node5.find('Pol').text
	else:
		ChannelPlan.strError = 'channel plan tag is not found'
		ChannelPlan.ret = -1
	if (count == 13):    #if required parameters found in channels file, return zero error in channelplan structure
		ChannelPlan.ret = 0;
	elif(count == 3):
		ChannelPlan.strError = 'Given Channel Id not found'
		ChannelPlan.ret = -1
	else:
		ChannelPlan.ret = -1
		if not bLocalSiteLatitude:
			ChannelPlan.strError = '<LocalSite><Lat> tag not found'
		if not bLocalSiteLongitude:
			ChannelPlan.strError = '<LocalSite><Lon> tag not found'
		if not bLocalSiteAltitude:
			ChannelPlan.strError = '<LocalSite><Alt> tag not found'
		if not bBeam:
			ChannelPlan.strError = '<Beam> tag not found'
		if not bPeerSiteLatitude:
			ChannelPlan.strError = '<PeerSite><Lat> tag not found'
		if not bPeerSiteLongitude:
			ChannelPlan.strError = '<PeerSite><Lon> tag not found'
		if not bPeerSiteAltitude:
			ChannelPlan.strError = '<PeerSite><Alt> tag not found'
		if not bUplinkModemFreq:
			ChannelPlan.strError = '<Uplink><ModemFreq> tag not found' 
		if not bUplinkRfFreq:
			ChannelPlan.strError = '<Uplink><RfFreq> tag not found'
		if not bUplinkRate:
			ChannelPlan.strError = '<Uplink><Rate> tag not found'
		if not bDownlinkModemFreq:
			ChannelPlan.strError = '<Downlink><ModemFreq> tag not found'
		if not bDownlinkRfFreq:
			ChannelPlan.strError = '<Downlink><RfFreq> tag not found'
		if not bDownlinkRate:
			ChannelPlan.strError = '<Downlink><Rate> tag not found'
