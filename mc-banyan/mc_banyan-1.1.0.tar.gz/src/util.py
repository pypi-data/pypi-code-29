import os
import shutil
from .assert_util import not_none as assert_not_none

root_folder = lambda:"./.tests"

def init_folder():
    if os.path.exists(root_folder()):
        remove_folder()
        
    os.makedirs(root_folder())

def remove_folder():
    shutil.rmtree(root_folder())
    
def create_folder(folder_name, parent_folder = None):
    def create(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    return create(os.path.join(parent_folder or root_folder(), folder_name))
                
def create_file(file_name, parent_folder, content):
    with open(os.path.join(parent_folder, file_name), 'w') as fileobj:
        fileobj.write(content)

def do_nothing():
    pass

def get_project_path(config_path):
    import re
    def match(pattern):
        return re.match(pattern, config_path)[0] if re.match(pattern, config_path) else None
    return os.path.relpath(assert_not_none(match('''.*(?=/deploy/\w+\.cfg)'''), "cfg path is invalid. Please make sure the it is under project folder"))
    
