import configparser

def getKeys():
	"""Return keys to keep during parsing restriction from configuration file.
	For example, if JSON file contains the following keys : "description_fr", "name_fr" and "content"
	And keys are "description_fr" and "name_fr",
	Then the only values kept during the parsing are thoses associated with the keys "description_fr" and "name_fr" 
	Return :
	keys -- keys to keep (restriction keys)
	"""	
	config = configparser.ConfigParser()
	config.read('json.ini') # read configuration file
	keys = config['keys']
	restrict = keys['restrict'] # get keys from configuration file
	return restrict

def setKeys(keys):
	"""Set keys to keep during parsing restriction from configuration file.
	For example, if JSON file contains the following keys : "description_fr", "name_fr" and "content"
	And keys are "description_fr" and "name_fr",
	Then the only values kept during the parsing are thoses associated with the keys "description_fr" and "name_fr" 
	"""
	Config = configparser.ConfigParser()
	cfgfile = open("json.ini",'w')
	# add the settings to the structure of the file, and lets write it out...
	Config.add_section('keys')
	Config.set('keys','restrict',keys)
	Config.write(cfgfile)
	cfgfile.close()