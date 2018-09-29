try: from kiwipiepy.coreWinx64 import *
except:
	try: from kiwipiepy.coreWinx86 import *
	except:
		try: from kiwipiepy.coreLinux64 import *
		except:
			raise Exception("Sorry. Currently, kiwipiepy can be run on Windows only.")