import logging

logger = logging.getLogger(__name__)

from pybpodgui_plugin.models.user.user_treenode import UserTreeNode

class UserDockWindow(UserTreeNode):

    def show(self):
        self.mainWindow.details.value = self
        super(UserDockWindow, self).show()

    def focus_name(self):
        self._namebox.form.lineEdit.setFocus()

    def close(self):
        self.mainWindow.details.value = None
        super(UserDockWindow, self).close(silent)

    @property
    def mainWindow(self):
        return self.project.mainwindow