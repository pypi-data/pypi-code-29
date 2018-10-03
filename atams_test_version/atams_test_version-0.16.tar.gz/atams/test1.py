#!/usr/bin/env python

print os.getcwd()
prefixed = [filename for filename in os.listdir('C:\Python27\Lib\site-packages') if filename.startswith("atams")]
print prefixed,'prefixed'

f1='C:\\Python27\\Lib\\site-packages\\atams_test_version-0.10-py2.7.egg'
f2='C:\\Python27\\Lib\\site-packages\\atams_test_version-0.10-py2.7.egg\\atams'
d1='C:\\Users\\SIGPC4\\Desktop\\atamsPackage\\atams1'

if 'atams_test_version-0.10                                                                                                                                                                                                                                                                                                                     -py2.7.egg' in prefixed:
	print 'found...'
	os.chdir('f1')
	if os.path.isdir('f2'):
		print 'yes dir is there'
		copy_tree('f2', 'd1')
	#os.system("cd C:\Python27\Lib\site-packages\atams_test_version-0.5-py2.7.egg")
	print os.getcwd()
	
'''if os.path.isdir("C:\\Python27\\Lib\\site-packages\\atams_test_version-0.1-py2.7.egg"):
	print 'yes found 0.1..'


if os.path.isdir("C:\Python27\Lib\site-packages\atams_test_version-0.2-py2.7.egg"):
	print 'yes found'


print 'ksdjsdlkflsdjfldfgdf'''
