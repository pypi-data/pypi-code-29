
from PySideX import QtCore
from opencmiss.zinc.sceneviewerinput import Sceneviewerinput

# Create a button map of Qt mouse buttons to Zinc input buttons
BUTTON_MAP = {QtCore.Qt.LeftButton: Sceneviewerinput.BUTTON_TYPE_LEFT,
              QtCore.Qt.MidButton: Sceneviewerinput.BUTTON_TYPE_MIDDLE,
              QtCore.Qt.RightButton: Sceneviewerinput.BUTTON_TYPE_RIGHT,
              QtCore.Qt.NoButton: None}


# Create a modifier map of Qt modifier keys to Zinc modifier keys
def modifier_map(qt_modifiers):
    """
    Return a Zinc scene viewer input modifiers object that is created from
    the Qt modifier flags passed in.
    """
    modifiers = Sceneviewerinput.MODIFIER_FLAG_NONE
    if qt_modifiers & QtCore.Qt.SHIFT:
        modifiers = modifiers | Sceneviewerinput.MODIFIER_FLAG_SHIFT

    return modifiers


class AbstractHandler(object):

    def __init__(self):
        self._scene_viewer = None
        self._zinc_sceneviewer = None
        self._ignore_mouse_events = False
        self._processing_mouse_events = False

    def get_mode(self):
        return self.__class__.__name__

    def set_ignore_mouse_events(self, value=True):
        self._ignore_mouse_events = value

    def set_scene_viewer(self, scene_viewer):
        self._scene_viewer = scene_viewer
        if self._scene_viewer.is_graphics_initialized():
            self._graphics_ready()
        else:
            self._scene_viewer.graphics_initialized.connect(self._graphics_ready)

    def enter(self):
        raise NotImplementedError()

    def leave(self):
        raise NotImplementedError()

    def mouse_press_event(self, event):
        self._processing_mouse_events = False
        if self._ignore_mouse_events:
            event.ignore()
            return

        if event.button() not in BUTTON_MAP:
            return

        event.accept()
        self._processing_mouse_events = True

    def mouse_move_event(self, event):
        if self._ignore_mouse_events:
            event.ignore()
            return

        event.accept()

    def mouse_release_event(self, event):
        if self._ignore_mouse_events:
            event.ignore()
            return

        if event.button() not in BUTTON_MAP:
            return

        event.accept()

    def mouse_enter_event(self, event):
        if self._ignore_mouse_events:
            event.ignore()
            return

        event.accept()

    def mouse_leave_event(self, event):
        if self._ignore_mouse_events:
            event.ignore()
            return

        event.accept()

    def key_press_event(self, event):
        event.ignore()

    def key_release_event(self, event):
        event.ignore()

    def _graphics_ready(self):
        self._zinc_sceneviewer = self._scene_viewer.get_zinc_sceneviewer()
