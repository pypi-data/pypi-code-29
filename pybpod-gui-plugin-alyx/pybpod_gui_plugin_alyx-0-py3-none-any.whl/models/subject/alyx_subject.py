import os
import logging
import glob
import hashlib, pybpodgui_api
from AnyQt.QtGui import QIcon
from confapp import conf
from pybpodgui_api.utils.send2trash_wrapper import send2trash
from sca.formats import json
from pybpodgui_api.models.project.project_base import ProjectBase
from pybpodgui_api.exceptions.api_error import APIError

from pybpodgui_plugin.models.subject.subject_uibusy import SubjectUIBusy

from pybpod_alyx_module.alyx_details import AlyxDetails

class AlyxSubject(SubjectUIBusy):

    def __init__(self,project):
        super(AlyxSubject, self).__init__(project)

    def add_alyx_info(self,jsondata):
        print(json.dumps(jsondata))
        print(self.uuid4)
        self.name = jsondata['nickname']
        self.alyx_nickname = jsondata['nickname']
        self.alyx_id = jsondata['id']
        self.alyx_species = jsondata['species']
        self.alyx_genotype = jsondata['genotype']
        self.alyx_litter = jsondata['litter']
        self.alyx_alive = jsondata['alive']
        self.alyx_url = jsondata['url']
        self.alyx_line = jsondata['line']
        self.alyx_birth_date = jsondata['birth_date']
        self.alyx_responsible_user = jsondata['responsible_user']
        self.alyx_sex = jsondata['sex']
        self.alyx_death_date = jsondata['death_date']
        self.alyx_description = jsondata['description']
        self.alyx_strain = jsondata['strain']
        print(self.uuid4)
        

    def save(self):
        """
        Save subject data on filesystem.

        :ivar str project_path: Project path.  
        :return: Dictionary containing the setup info to save.  
        :rtype: dict
        """
        if not self.name:
            logger.warning("Skipping subject without name")
            return None
        else:  
            if not os.path.exists(self.path): os.makedirs(self.path)

            if self.data:
                data = self.data
            else:
                data = json.scadict(
                    uuid4_id=self.uuid4,
                    software='PyBpod GUI API v'+str(pybpodgui_api.__version__),
                    def_url ='http://pybpod.readthedocs.org',
                    def_text='This file contains information about a subject used on PyBpod GUI.',
                )
            data['nickname'] = self.alyx_nickname
            data['alyx_id'] = self.alyx_id
            data['species'] = self.alyx_species
            data['genotype'] = self.alyx_genotype
            data['litter'] = self.alyx_litter
            data['alive'] = self.alyx_alive
            data['url'] = self.alyx_url
            data['line'] = self.alyx_line
            data['birth_date'] = self.alyx_birth_date
            data['responsible_user'] = self.alyx_responsible_user
            data['sex'] = self.alyx_sex
            data['death_date'] = self.alyx_death_date
            data['description'] = self.alyx_description
            data['strain'] = self.alyx_strain

            config_path = os.path.join(self.path, self.name+'.json')
            with open(config_path, 'w') as fstream: json.dump(data, fstream)

    def toJSON(self):
        data = json.scadict(
                    uuid4_id=self.uuid4,
                    software='PyBpod GUI API v'+str(pybpodgui_api.__version__),
                    def_url ='http://pybpod.readthedocs.org',
                    def_text='This file contains information about a subject used on PyBpod GUI.',
                )
        data['name'] = self.name
        data['uuid4'] = self.uuid4
        data['nickname'] = self.alyx_nickname
        data['alyx_id'] = self.alyx_id
        data['species'] = self.alyx_species
        data['genotype'] = self.alyx_genotype
        data['litter'] = self.alyx_litter
        data['alive'] = self.alyx_alive
        data['url'] = self.alyx_url
        data['line'] = self.alyx_line
        data['birth_date'] = self.alyx_birth_date
        data['responsible_user'] = self.alyx_responsible_user
        data['sex'] = self.alyx_sex
        data['death_date'] = self.alyx_death_date
        data['description'] = self.alyx_description
        data['strain'] = self.alyx_strain

        return json.dumps(data)

    def load(self, path):
        """
        Load sebject data from filesystem

        :ivar str subject_path: Path of the subject
        :ivar dict data: data object that contains all subject info
        """
        print('LOADING SUBJECT ALYX')
        self.name  = os.path.basename(path)

        try:
            with open( os.path.join(self.path, self.name+'.json'), 'r' ) as stream:
                self.data = data = json.load(stream)
            
            self.alyx_nickname = data['nickname'] if 'nickname' in data.keys() else None
            self.uuid4 = data.uuid4 if data.uuid4 else self.uuid4
            self.alyx_id = data['alyx_id'] if 'alyx_id' in data.keys() else None
            self.alyx_species = data['species'] if 'species' in data.keys() else None
            self.alyx_genotype = data['genotype'] if 'genotype' in data.keys() else None
            self.alyx_litter = data['litter'] if 'litter' in data.keys() else None
            self.alyx_alive = data['alive'] if 'alive' in data.keys() else None
            self.alyx_url = data['url'] if 'url' in data.keys() else None
            self.alyx_line = data['line'] if 'line' in data.keys() else None
            self.alyx_birth_date = data['birth_date'] if 'birth_date' in data.keys() else None
            self.alyx_responsible_user = data['responsible_user'] if 'responsible_user' in data.keys() else None
            self.alyx_sex = data['sex'] if 'sex' in data.keys() else None
            self.alyx_death_date = data['death_date'] if 'death_date' in data.keys() else None
            self.alyx_description = data['description'] if 'description' in data.keys() else None
            self.alyx_strain = data['strain'] if 'strain' in data.keys() else None

        except:
            raise Exception('There was an error loading the configuration file for the subject [{0}]')

    def create_treenode(self, tree):
        """
        Creates node for this board under the parent "Boards" node.

        This methods is called when the board is first created.

        The following actions get assigned to node:
            * *Remove*: :meth:`BoardTreeNode.remove`.

        Sets key events:
            * :meth:`BoardTreeNode.node_key_pressed_event`


        :param tree: the project tree
        :type tree: pyforms.controls.ControlTree
        :return: new created node
        :return type: QTreeWidgetItem
        """
        self.node 						= tree.create_child(self.name, self.project.subjects_node, icon=QIcon(conf.SUBJECT_SMALL_ICON))
        self.node.key_pressed_event 	= self.node_key_pressed_event
        self.node.window 				= self
        self.node.setExpanded(True)

        tree.add_popup_menu_option('Remove', self.remove, item=self.node, icon=QIcon(conf.REMOVE_SMALL_ICON))
        tree.add_popup_menu_option('Alyx Details', self.showdetails, item = self.node)
        return self.node

    def showdetails(self):
        if not hasattr(self, 'detailswindow'):
            self.detailswindow = AlyxDetails(self)
        self.detailswindow.show()

'''
test_subject = {
    "nickname": "test_subject_posted",
    "responsible_user": "test_user",  # Required
    "birth_date": None,
    "death_date": None,
    "species": None,
    "sex": 'U',  # Required
    "litter": None,
    "strain": None,
    "line": None,
    "description": "Some description",
    "genotype": []  # Required?
}
'''

'''
{
    'species': 'mouse', 
    'genotype': [], 
    'litter': None, 
    'alive': True, 
    'url': 'http://alyx.champalimaud.pt:8000/subjects/4577', 
    'line': None, 
    'birth_date': '2017-04-11', 
    'responsible_user': 'ines', 
    'sex': 'F', 
    'death_date': None, 
    'description': '', 
    'nickname': '4577', 
    'strain': 'VGlut-2-ChR2-het', 
    'id': '27705345-f49a-4483-aec8-313fc01d2c1f'
} 


'''     