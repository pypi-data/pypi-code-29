from PyObjCTools.TestSupport import *

import MASShortcut

class TestMASShortcutMonitor (TestCase):
    def test_classes(self):
        MASShortcut.MASShortcutMonitor

    def test_methods(self):
        self.assertResultIsBOOL(MASShortcut.MASShortcutMonitor.registerShortcut_withAction_)
        self.assertResultIsBOOL(MASShortcut.MASShortcutMonitor.isShortcutRegistered_)

if __name__ == "__main__":
    main()
