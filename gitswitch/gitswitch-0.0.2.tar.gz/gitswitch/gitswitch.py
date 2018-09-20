import argparse
import os
import shutil


def handler():
  parser = argparse.ArgumentParser(prog='git-switch')
  parser.add_argument('--activate', help='activate ssh account', required=False)
  parser.add_argument('--list', help='List active accounts in $HOME/.git-switch/ folder', required=False, action='store_true')
  parser.add_argument('--create', help='Create a new ssh keypair to use in git', required=False, action='store_true')
  parser.add_argument('--backup', help='Backup current ssh keys at $HOME/.ssh', required=False, action='store_true')
  args = parser.parse_args()
  
  if args.list:
    list_environments()
  if args.activate:
    backup_ssh()
    activate_environment(args.activate)
  if args.create:
    create_environment()
  if args.backup:
    backup_ssh()

def create_switch_home():
  home_location = os.environ.get('HOME')
  switch_location = os.path.join(home_location,'.git-switch')
  os.makedirs(switch_location, 0755)


def get_switch_location():
  home_location = os.environ.get('HOME')
  return os.path.join(home_location,'.git-switch')
  
def list_environments():
  if os.path.exists(get_switch_location()):
    directories =  os.listdir(get_switch_location())
    if len(directories) == 0:
      print "You need to add some folders to $HOME/.git-switch"
      return
    print "Current environments found:"
    for directory in directories:
      current_directory_path = os.path.join(get_switch_location(), directory)
      if os.path.isdir(current_directory_path):
        print "* {}".format(directory)
  else:
    create_switch_home()
    print "This is the first time you are running git-switch, please add some folders to $HOME/.git-switch"

def activate_environment(environment):
  print "Activate environment"
  environment_folder = os.path.join(get_switch_location(),environment)
  print environment_folder
  ssh_folder = os.path.join(os.environ.get('HOME'),'.ssh/')
  if os.path.exists(ssh_folder):
    shutil.rmtree(ssh_folder)
  if os.path.exists(environment_folder):
    shutil.copytree(environment_folder, os.path.join(os.environ.get('HOME'),'.ssh'))
  else:
    print "The enviroment you are trying to activate does not exists"

def create_environment():
  print "Create environment"


def backup_ssh():
  
  if os.path.exists(os.path.join(os.environ.get('HOME'),'.ssh')):

    ssh_location = os.path.join('~','.ssh')
    print "Backing up ssh folder"
    
    archive_name = os.path.expanduser(os.path.join('~/.git-switch', 'ssh-bkp'))
    root_dir  = os.path.expanduser(os.path.join('~', '.ssh'))
    shutil.make_archive(archive_name, 'gztar', root_dir) 
  else:
    print "Current ssh folder has not been found"
