import pyforms
from confapp import conf
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText, ControlButton, ControlLabel
from pybpod_alyx_module.module_api import AlyxModule
from AnyQt.QtWidgets import QLineEdit

from pybpodgui_api.models.project import Project
from pybpod_alyx_module.models.subject.alyx_subject import AlyxSubject
from pybpodgui_api.models.subject import Subject

class AlyxModuleGUI(AlyxModule, BaseWidget):

    TITLE = 'Alyx connection'

    def __init__(self, _project : Project):
        BaseWidget.__init__(self, self.TITLE)
        AlyxModule.__init__(self)

        self.project = _project
        
        self._addressbox = ControlText('Address')
        self._username = ControlText('User:')
        self._password = ControlText('Password:')
        #self._username = ControlText('User:',default = 'test_user')
        #self._password = ControlText('Password:', default = 'test')
        self._connect_btn = ControlButton('Connect',default = self._connect)
        self._status_lbl = ControlLabel('Status: Not Connected')
        self._getsubjects_btn = ControlButton('Get Subjects', default = self._get_subjects)

        self.set_margin(10)

        self._addressbox.value = conf.ALYX_ADDR
        self._addressbox.changed_event = self.setaddr

        if self.project.loggeduser is not None:
            self._username.value = self.project.loggeduser.name
        
        self._password.form.lineEdit.setEchoMode(QLineEdit.Password)

        self.formset = [
            '_addressbox',
            '_username',
            '_password',
            '_connect_btn',
            '_status_lbl',
            '_getsubjects_btn'
        ]

    def setaddr(self):
        self.api.setaddr(self._addressbox.value)

    def _connect(self):
        if self._connect_to_alyx(self._username.value,self._password.value):
            usersearch = self.project.find_user(self._username.value)
            if usersearch is None: # create this user on the project
                newuser = self.project.create_user()
                newuser.name = self._username.value
                newuser.node_double_clicked_event()
            else:
                usersearch.node_double_clicked_event()
            self.project.loggeduser.connection = 'ALYX'
            self._status_lbl.value = 'Status: CONNECTED'
            self.project.loggeduser = self.project.loggeduser

    def _get_subjects(self):
        result = self.get_alyx_subjects(self._username.value)
        for subj in result:
            subjname = subj['nickname']
            existing = False
            for s in self.project.subjects:
                if s.name == subjname:
                    existing = True
                    reply = self.question('Subject ' + s.name + ' Already exists locally. Replace local details?', 'Update Subject')
                    if reply == 'yes':
                        s.add_alyx_info(subj)
            if existing == False:
                newsubject = AlyxSubject(self.project)
                newsubject.add_alyx_info(subj)
                self.project += newsubject
            

            