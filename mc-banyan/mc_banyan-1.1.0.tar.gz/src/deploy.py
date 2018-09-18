import os
from .defaults import write as write_defaults, override_values, all as all_defaults
from .roles import build as roles_build, link as roles_link, load as roles_load, link_src_to_deploy
from .debug import simple as debug_simple
import yaml
from .tools.file import get_file_name, get_file_only_name, put_file
from .tools.folder import put_folder
import demjson



def init_deploy(root_folder, project_name, config_name, build_handler, run_handler, error_handler):
    '''
build_handler: (configuration_folder, banayan_configuration_name)，if the configuration_folder has not already created, build_handler will be called.
run_handler: (configuration_folder), if the configuration_folder has already been created, it will call this handler
error_handler: (msg), raise error message friendly.
'''
    def banyan_config_path():
        return os.path.join(root_folder, project_name, "deploy", "banyan.cfg" if config_name == None else config_name + ".cfg")

    def config_path():
        return os.path.join(root_folder, project_name, "deploy", ".banyan" if config_name == None else "." + config_name)
    
    def check_structure():
        def check(path):
            return "%s is not existing" % path if not os.path.exists(path) else None
        return check(banyan_config_path())









    if check_structure():
        error_handler(check_structure())

    if os.path.exists(config_path()):
        run_handler(config_path())

    if not os.path.exists(config_path()):
        build_handler(config_path(), banyan_config_path())


def run_deploy(configuration_path):
    '''configuration_path: it is the folder path which contains the main.sh to launch the deploy script'''
    import subprocess
    
    def run(current_path):
        try:
            os.chdir(configuration_path)
            p = subprocess.Popen("bash main.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            while p.poll() is None:
                line = p.stdout.readline()
                if line:
                    print(line.strip())
        finally:
            os.chdir(current_path)

    run(os.getcwd())


def build_deploy_script(target_folder, cfg_file_path): #yml_file_path#
    yml_file_folder = lambda: put_folder(os.path.abspath(target_folder))
    yml_file_path = lambda: os.path.join(yml_file_folder(), "main.yml")
    host_file = lambda: os.path.join( \
        yml_file_folder(), \
        debug_simple(get_file_only_name(yml_file_path()), "host file name") + ".host")
    bash_file = lambda: os.path.join( \
                                      yml_file_folder(),
                                      get_file_only_name(yml_file_path()) + ".sh")


    def build(file, roles_data):
        # write data to file
        file.write(roles_build(roles_data))
        # build link for role folders
        roles_link(roles_data, \
                   debug_simple(yml_file_folder(), "link_root") \
        )
        # link src folder to deploy/roles/main/files/src for deployment
        link_src_to_deploy(roles_data)
        # build inventory files on roles
        write_defaults(host_file(), \
                       override_values( \
                                                 demjson.decode_file(cfg_file_path), \
                                                 all_defaults(yml_file_folder(), \
                                                              [role["name"] for role in roles_data] \
                                                              ) \
                                                 ) \
                       )
        # build the bash file
        open(bash_file(), "w") \
            .write("sudo ansible-playbook ./{yml_file} -i ./{host_file}" \
                   .format(yml_file = get_file_name(put_file(yml_file_path())), \
                           host_file = get_file_name(host_file()) \
                   ) \
            )


    build(open(put_file(yml_file_path()), 'w'), \
          roles_load(cfg_file_path) \
    )

    run_deploy(target_folder)

def run_deploy_script(configuration_path):
    run_deploy(configuration_path)
