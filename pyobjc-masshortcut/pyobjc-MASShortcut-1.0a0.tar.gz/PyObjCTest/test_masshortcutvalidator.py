from PyObjCTools.TestSupport import *

import MASShortcut

class TestMASShortcutValidator (TestCase):
    def test_classes(self):
        MASShortcut.MASShortcutValidator

    def test_methods(self):
        self.assertResultIsBOOL(MASShortcut.MASShortcutValidator.allowAnyShortcutWithOptionModifier)
        self.assertArgIsBOOL(MASShortcut.MASShortcutValidator.setAllowAnyShortcutWithOptionModifier_, 0)

        self.assertResultIsBOOL(MASShortcut.MASShortcutValidator.isShortcutValid_)
        self.assertResultIsBOOL(MASShortcut.MASShortcutValidator.isShortcut_alreadyTakenInMenu_explanation_)
        self.assertArgIsOut(MASShortcut.MASShortcutValidator.isShortcut_alreadyTakenInMenu_explanation_, 2)
        self.assertResultIsBOOL(MASShortcut.MASShortcutValidator.isShortcutAlreadyTakenBySystem_explanation_)
        self.assertArgIsOut(MASShortcut.MASShortcutValidator.isShortcutAlreadyTakenBySystem_explanation_, 1)

if __name__ == "__main__":
    main()
