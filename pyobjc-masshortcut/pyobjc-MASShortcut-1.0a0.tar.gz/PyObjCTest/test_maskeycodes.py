from PyObjCTools.TestSupport import *

import MASShortcut

class TestMASKeyCodes (TestCase):
    def test_constants(self):
        self.assertEqual(MASShortcut.kMASShortcutGlyphEject, 0x23CF)
        self.assertEqual(MASShortcut.kMASShortcutGlyphClear, 0x2715)
        self.assertEqual(MASShortcut.kMASShortcutGlyphDeleteLeft, 0x232B)
        self.assertEqual(MASShortcut.kMASShortcutGlyphDeleteRight, 0x2326)
        self.assertEqual(MASShortcut.kMASShortcutGlyphLeftArrow, 0x2190)
        self.assertEqual(MASShortcut.kMASShortcutGlyphRightArrow, 0x2192)
        self.assertEqual(MASShortcut.kMASShortcutGlyphUpArrow, 0x2191)
        self.assertEqual(MASShortcut.kMASShortcutGlyphDownArrow, 0x2193)
        self.assertEqual(MASShortcut.kMASShortcutGlyphEscape, 0x238B)
        self.assertEqual(MASShortcut.kMASShortcutGlyphHelp, 0x003F)
        self.assertEqual(MASShortcut.kMASShortcutGlyphPageDown, 0x21DF)
        self.assertEqual(MASShortcut.kMASShortcutGlyphPageUp, 0x21DE)
        self.assertEqual(MASShortcut.kMASShortcutGlyphTabRight, 0x21E5)
        self.assertEqual(MASShortcut.kMASShortcutGlyphReturn, 0x2305)
        self.assertEqual(MASShortcut.kMASShortcutGlyphReturnR2L, 0x21A9)
        self.assertEqual(MASShortcut.kMASShortcutGlyphPadClear, 0x2327)
        self.assertEqual(MASShortcut.kMASShortcutGlyphNorthwestArrow, 0x2196)
        self.assertEqual(MASShortcut.kMASShortcutGlyphSoutheastArrow, 0x2198)

    def test_functions(self):
        MASShortcut.NSStringFromMASKeyCode
        MASShortcut.MASPickCocoaModifiers
        MASShortcut.MASCarbonModifiersFromCocoaModifiers

if __name__ == "__main__":
    main()
