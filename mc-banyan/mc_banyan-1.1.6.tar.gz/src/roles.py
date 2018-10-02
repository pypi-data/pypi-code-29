import os
import demjson
from .assert_util import not_none as assert_not_none
from .debug import simple as debug_simple
import logging
from .util import get_project_path, extract_project_path, get_config_path
from pathlib import Path
logger = logging.getLogger(__name__)
from fn import F

def load(config_path):
    '''
config_path: the path of the banyan configuration file
'''
    def get_cfg(dep_json):
        def load_cfg(cfg_path):
            return demjson.decode_file(cfg_path)

        return (F(get_config_path) >> F(load_cfg))(dep_json["project_name"], dep_json["config_name"] if "config_name" in dep_json else None)

    def get_roles(cfg_json, project_path):
        return [{"name": "%s_%s" % (debug_simple(os.path.split(project_path), "get_roles path")[1], role_name), \
                 "local": project_path,
                 "original_name": role_name} for role_name in cfg_json["roles_seq"]] if "roles_seq" in debug_simple(cfg_json, "get_roles cf_json") else []
    
    def handle(cfg_json, depended_roles, project_path):
        debug_simple(project_path, "handle_project_path")
        try:
            return [y for x in [handle(debug_simple(get_cfg(dep), "json in recursive"), depended_roles, get_project_path(dep["project_name"])) for dep in cfg_json["dependencies"]] for y in x] + get_roles(debug_simple(cfg_json, "get_roles_json_recursive"), debug_simple(project_path, "get_roles_path_recursive")) \
            if "dependencies" in cfg_json \
               else depended_roles + get_roles(debug_simple(cfg_json, "no dep json"), debug_simple(project_path, "no dep path"))
        except Exception:
            logger.debug("error happen in handle with project_path:%s\ncfg_json:%s", project_path, cfg_json)
            raise

    return handle(demjson.decode_file(config_path), [], debug_simple(extract_project_path(config_path)))


def build(roles, remote_name = None):
    from jinja2 import Template
    def get_host(): return 'hosts: localhost' if remote_name == None else 'hosts: ' + remote_name
    '''
build the roles into the entry yaml file
roles: a list for role. the sturcture of role can be reference in get_roles
'''
    return Template('''
---

- name: deploy
  {{ hosts }}
  become: true
  become_method: sudo
  roles:
{% for role in objs %}    - {{role}}
{% endfor %}
...
  
''').render(objs = [role["name"] for role in roles], hosts = get_host())


def link(roles, path):
    '''
link the roles
'''
    def get_src(role):
        return os.path.join(role["local"], "deploy", "roles", role["original_name"])

    def create_folder(name, parent_path):
        def create(path):
            if os.path.exists(path):
                return path
            os.makedirs(path)
            return path
        return create(os.path.join(parent_path, name))
    
    def get_dest(role):
        return os.path.join(create_folder("roles", os.path.abspath(path)) , role["name"])
    
    def link_role(role):
        if not os.path.exists(get_dest(role)):
            os.symlink(os.path.abspath(debug_simple(get_src(role), "src")), debug_simple(get_dest(role), "dest"))
        
    [link_role(role) for role in roles]


def link_src_to_deploy(rolesdata):
    ''' link src folder to deploy/roles/main/files/src for deployment '''
    
    def link(project_folder, src_name, link_folder):
        debug_simple(project_folder, 'project_folder')
        def put(target_path):
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            return target_path
        
        def link_path(source_path, target_link_path):
            if os.path.exists(source_path) and not Path(target_link_path).is_symlink():
                os.symlink(source_path, target_link_path)

        link_path(os.path.abspath(os.path.join(project_folder, src_name)),  os.path.join(\
                                                                                         put(os.path.abspath(os.path.join(project_folder, link_folder))),\
                                                                                         src_name)\
        )
        
    [link(project_folder, "src", "deploy/roles/main/files") for project_folder in list(set([p["local"] for p in rolesdata]))]
        
