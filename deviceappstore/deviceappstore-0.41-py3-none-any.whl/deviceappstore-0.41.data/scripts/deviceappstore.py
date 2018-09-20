#!python
import json
import ssl
import tempfile
import sys
import os
import subprocess
import platform
import hashlib
import gzip
import zipfile
#import commands
import argparse
import glob
import serial
import pkg_resources
import time
from subprocess import call
from subprocess import Popen, PIPE

try:
    from urllib.request import Request, urlopen  # Python 3
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import Request, urlopen, HTTPError  # Python 2

'''
TODO: List
      Better error printing
      Shows issue request info: http://github.com/deviceappstore/deviceappstore-installer/issues
'''

#import imp
from distutils.spawn import find_executable as which

def serial_ports():
  if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
  elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    ports = glob.glob('/dev/tty[A-Za-z]*')
  elif sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/cu.*') + glob.glob('/dev/tty.*')
  else:
    raise EnvironmentError('Unsupported platform')

  result = []
  for port in ports:
    try:
      s = serial.Serial(port)
      s.close()
      result.append(port)
    except (OSError, serial.SerialException):
      pass
  
  return result

def serial_port(port):
  ports = serial_ports()
  if len(ports) > 1 and port == -1:
    print(str(len(ports)) + " port detected. Plese choose which port is getting used:\n")
    for i, port in enumerate(ports):
      print("[" + str(i + 1) + "]: " + port)
    print('')
    port = int(raw_input('Number: '))
  elif len(ports) == 1:
    port = 1
  else:
    print("No port found")
    exit(1)

  return ports[port - 1]

# Print error msg
def eprint(txt):
  sys.stderr.write('\x1b[1;31m' + txt.strip() + '\x1b[0m\n')

# Print success msg
def sprint(txt):
  sys.stdout.write('\x1b[1;32m' + txt.strip() + '\x1b[0m\n')

# Print info/warning msg
def wprint(txt):
  sys.stdout.write('\x1b[1;32m' + txt.strip() + '\x1b[0m\n')

# ceate checkum of donwloaded file
def checksum(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
       hash_md5.update(chunk)
  return hash_md5.hexdigest()

def whichExec(program):
  import os
  def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

  fpath, fname = os.path.split(program)
  if fpath:
    if is_exe(program):
      return program
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      exe_file = os.path.join(path, program)
      if is_exe(exe_file):
        return exe_file

  return None

# Download from URL
def download(info, retry=True):
  # Download the file first
  new_file, filename = tempfile.mkstemp()
  url = info['url']
  u = urlopen(url)
  #request = urllib2.Request(url, headers={'Accept-Encoding': 'gzip'})
  #request = urllib2.Request(url)
  #u = urllib2.urlopen(request)
  meta = u.info()
  file_name = url.split('/')[-1]
  #u = urllib2.urlopen(url)
  #f = open(file_name, 'wb')
  print('getheader' in dir(u))
  if 'getheader' in dir(u):
    file_size = int(u.getheader("Content-Length"))
  else:
    file_size = int(meta.getheaders("Content-Length")[0])
  print(file_size)

  # TODO: Check if it's zip, for now we just accept zip
  # contentType = meta.getheaders("Content-Type")[0]
  print("Downloading: %s Bytes: %s" % (file_name, file_size))
 
  file_size_dl = 0
  block_sz = 8192
  while True:
    buffer = u.read(block_sz)
    if not buffer:
      break

    file_size_dl += len(buffer)
    os.write(new_file, buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print(status),

  os.close(new_file)

  '''md5 = checksum(new_file)
  if md5 != info.checksum:
    print('Downloaded file is corrupted try to download the file again')
    if retry:
      # We just retry one time
      return download(info, False)'''
  #_, raw = tempfile.mkstemp()
  #with gzip.open(filename, 'rb') as f_in, open(raw, 'wb') as f_out:
  #  f_out.write(f_in.read())
  
  zip_ref = zipfile.ZipFile(filename, 'r')
  zip_ref.extractall(filename + '_files')
  zip_ref.close()

  return os.path.join(filename + '_files', 'rom.bin')

def versionCall(args):
  # Not work with python3
  #print(pkg_resources.require("deviceappstore")[0].version)
  print("0.41")

def sendCall(args):
  port = serial_port(args.port)

  print("Try to sent to " + port + " ...")

  ser = serial.Serial(
    port=port,
    baudrate=115200
  )

  ser.isOpen()

  # Important: Write string cause wrong encoding
  ser.write(args.command.encode())

  out = ''
  time.sleep(2)
  while ser.inWaiting() > 0:
    out += ser.read(1)
  print(">>" + out)

  exit()

def installCall(args):
  try:
    #opener = urllib2.build_opener()
    #opener.addheaders = [('User-agent', 'deviceappstore-installer/0.1'), ('Accept-Encoding', 'xz')]
    q = Request('https://deviceappstore.com/api/app/' + args.app)
    q.add_header('User-agent', 'deviceappstore-installer/0.41')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    info = json.load(urlopen(q, context=ctx))
  except (HTTPError) as e:
    if e.code == 404:
      eprint("The application did not find: '" + args.app + "'. Please check the app ID/Name and try again.")
    else:
      print(e.code)
      print(e.msg)
      print(e.headers)
      print(e.fp.read())
    exit()
  except e:
    print(e)
    print('Error to connect to the server, check the internet connection or update the app')
    exit()

  # TODO: Download setup instruction http://deviceappstore.com/setup/eprism_s04
   
  if which('esptool.py') is None:
    eprint('You need to setup esptool.py to be able to setup this application:')
    print('\n    (sudo) pip install esptool\n')
    exit(1)

  # Esp setup mode
  if args.device in ['eprism_s04', 'eprism_t04']:
    version = info['versions'][0]

    # Download the ROM
    rom_info = version['rom']
    rom = download(rom_info)
    port = serial_port(args.port)

    print('Please do not unplug your device until the operation finishs. Any intruption may damage your device.')

    p = Popen([which('esptool.py'), "--port", port, "chip_id"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    if rc == 0 and str(output).find("ESP8266EX") > -1:
      call([which('esptool.py'), "--port", port, "write_flash", "0", rom])
    else:
      print('Could not detect the device!')
      exit(1)
  elif args.device in ['eprism2_s04', 'eprism2_t04']:
    version = info['versions'][0]

    # Download the ROM
    rom_info = version['rom']
    rom = download(rom_info)
    port = serial_port(args.port)

    print('Please do not unplug your device until the operation finishs. Any intruption may damage your device.')

    p = Popen([which('esptool.py'), "--port", port, "chip_id"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    if rc == 0 and "ESP32D0WDQ6" in output:
      call([which('esptool.py'), "--port", port, "write_flash", "0", rom])
    else:
      print('Could not detect the device!')
      exit(1)

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

install = subparser.add_parser('install')
install.add_argument('device', help='Type of device you connected to your sysytem')
install.add_argument('app', help='The ID or Complete name of the application you want to setup')
install.add_argument('-p', '--port', help='Port index', default=-1, type=int)
install.set_defaults(func=installCall)

send = subparser.add_parser('send')
send.add_argument('command', help='Command to send to the device')
send.add_argument('-p', '--port', help='Port index', default=-1, type=int)
send.set_defaults(func=sendCall)

version = subparser.add_parser('version')
version.set_defaults(func=versionCall)

cmd = parser.parse_args()
cmd.func(cmd)
