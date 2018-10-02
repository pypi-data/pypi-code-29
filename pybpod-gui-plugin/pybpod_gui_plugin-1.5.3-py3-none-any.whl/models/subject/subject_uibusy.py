# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from confapp import conf

from AnyQt.QtGui import QIcon

from pybpodgui_api.models.setup import Setup
from pybpodgui_api.models.subject import Subject
from pybpodgui_api.models.project import Project
from pybpodgui_plugin.models.subject.subject_dockwindow import SubjectDockWindow

logger = logging.getLogger(__name__)

class SubjectUIBusy(SubjectDockWindow):
    """
	Extends subject with UI refreshment logic.

	"""

    def __init__(self, project):
        super(SubjectUIBusy, self).__init__(project)
        self.__running_icon = QIcon(conf.PLAY_SMALL_ICON)
    
    # This must switch between start and stop
    def update_ui(self, sessionrunning = False):
        if sessionrunning == True:
            #self._run.enabled = False
            self._run.checked = True
            self._run.label = 'Stop'
            for sess in self._sessions:
                if sess.running == True:
                    self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
        else:
            #self._run.enabled = True
            self._run.checked = False
            self._run.label = 'Run'
            self.node.setIcon(0, QIcon(conf.SUBJECT_SMALL_ICON))