from PyObjCTools.TestSupport import *

import MASShortcut

class TestMASShortcutView (TestCase):
    def test_constants(self):
        self.assertIsInstance(MASShortcut.MASShortcutBinding, unicode)

        self.assertEqual(MASShortcut.MASShortcutViewStyleDefault, 0)
        self.assertEqual(MASShortcut.MASShortcutViewStyleTexturedRect, 1)
        self.assertEqual(MASShortcut.MASShortcutViewStyleRounded, 2)
        self.assertEqual(MASShortcut.MASShortcutViewStyleFlat, 3)

    def test_classes(self):
        MASShortcut.MASShortcutView

    def test_methods(self):
        self.assertResultIsBOOL(MASShortcut.MASShortcutView.isRecording)
        self.assertArgIsBOOL(MASShortcut.MASShortcutView.setRecording_, 0)

        self.assertResultIsBOOL(MASShortcut.MASShortcutView.isEnabled)
        self.assertArgIsBOOL(MASShortcut.MASShortcutView.setEnabled_, 0)

        self.assertResultIsBlock(MASShortcut.MASShortcutView.shortcutValueChange, b'v@')
        self.assertArgIsBlock(MASShortcut.MASShortcutView.setShortcutValueChange_, 0, b'v@')

        self.assertArgIsBOOL(MASShortcut.MASShortcutView.setAcceptsFirstResponder_, 0)

if __name__ == "__main__":
    main()
