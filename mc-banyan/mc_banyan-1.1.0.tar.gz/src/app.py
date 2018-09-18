from .banyan_opt import get_options
import sys
import os
from .deploy import init_deploy, run_deploy, build_deploy_script, run_deploy_script
import logging
logging.basicConfig(stream = sys.stdout, level = 'DEBUG')

def run(options):
    
        
    def error_handler(msg):
        print(msg)

        
    if options.command == "deploy":
        init_deploy(os.getcwd(), options.projectname, options.cfg, \
                build_deploy_script, \
                run_deploy_script, \
                error_handler)
    elif options.command == "init":
        from .init_code_with_tag import init_tag_for_project
        init_tag_for_project(options.giturl, options.tag, options.cfg, os.getcwd())
    elif options.command == "clear":
        from .clear_deploy import clear_deploy
        clear_deploy(os.path.join(os.getcwd(), options.projectname), options.cfg)
    else:
        print('please set the valid command: deploy, init')
        
def main():
    run(get_options())
