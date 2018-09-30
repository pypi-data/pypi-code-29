import os
from codegenhelper import debug
import subprocess
import re

def get_project_name_from_url(giturl):
    return os.path.basename(giturl)

def get_tag(giturl, tag, location = os.getcwd()):
    def get_tag_func(project_name):
        debug("start to get {tag} of {project_name}".format(tag=tag, project_name=project_name))
        #
        def load(temp_folder):
            subprocess.call('mkdir {temp}'.format(temp=temp_folder), \
                            shell=True, \
                            cwd=location)
            subprocess.call(debug('wget {giturl}/archive/{tag}.tar.gz && tar vzxf {tag}.tar.gz -C {temp} && rm {tag}.tar.gz'.format(giturl=giturl, tag=tag, project_name=project_name, temp=temp_folder)), \
                            shell=True, \
                            cwd=location)
            subprocess.call('ls |xargs -I {{}} mv {{}} {project_name}'.format(project_name=project_name), \
                            shell=True, cwd=os.path.join(location, '.temp'))
            subprocess.call('mv {temp}/{project_name} ./ && rm {temp} -rf'.format(project_name=project_name, temp=temp_folder),\
                            shell=True, cwd=location)
        load('.temp')

    get_tag_func(get_project_name_from_url(giturl))
    
def get_code(giturl, ssh_key = None, location = os.getcwd()):
    debug("start to clone code of %s" % giturl)

    def is_ssh():
        return giturl.startswith('git')
    
    subprocess.call(debug('ssh -i {key_file} git clone {giturl}'.format(key_file=ssh_key, giturl=giturl),'command'), \
                    shell=True, \
                    cwd=location) if is_ssh() else \
                    subprocess.call(debug('git clone {giturl}'.format(giturl=giturl), 'command'), \
                                    shell=True, \
                                    cwd=location)
    
    
