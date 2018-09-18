#!/usr/bin/env python
import unittest
from tipico.gui.basic_qt import SimpleGui
from test.test_helper import TestHelper
from Qt.QtWidgets import QApplication



class SimpleGuiTest(unittest.TestCase):


    def setUp(self):
        try:
            self.qtApp= QApplication([])
        except RuntimeError:
            self.qtApp=QApplication.instance()
        self.gui= SimpleGui()
        QApplication.processEvents()

    def tearDown(self):
        del self.qtApp


    def testName(self):
        self.assertEqual('Simple', self.gui.windowTitle())


    def testButton(self):
        self.gui.pushButton.setText("42")
        self.assertEqual('42', self.gui.pushButton.text())


    def testLabel(self):
        self.gui.label.setText("foo")
        self.assertEqual('foo', self.gui.label.text())


if __name__ == "__main__":
    TestHelper.executeQtGUITestsWithXvfb(SimpleGuiTest,
                                         [],
                                         "./xvfb.log")