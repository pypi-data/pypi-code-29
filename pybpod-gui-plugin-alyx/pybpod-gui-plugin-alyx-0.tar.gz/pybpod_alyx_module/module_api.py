from pybpodapi.bpod_modules.bpod_module import BpodModule
from pybpod_alyx_module.alyxapi.alyxapi import AlyxAPI


class AlyxModule(object):
    
    def __init__(self):
        self.api = AlyxAPI()

    def _connect_to_alyx(self,username, password):
        return self.api.login(username,password)
    
    def get_alyx_subjects(self, username):
        return self.api.subjects.get.usersubjects(username)
    
    def get_alyx_address(self):
        return self.api.getaddr()
    
    def set_alyx_address(self,value):
        print('setting addr',value)
        self.api.setaddr(value)