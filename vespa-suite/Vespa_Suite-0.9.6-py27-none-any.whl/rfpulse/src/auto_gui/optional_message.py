#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Fri Jun 17 12:48:58 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.LabelMessage = wx.StaticText(self, -1, "Message goes here...")
        self.CheckDontShowAgain = wx.CheckBox(self, -1, "Don't show this message again")
        self.LabelOkCancelPlaceholder = wx.StaticText(self, -1, "OK and Cancel go here at runtime")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.LabelMessage, 0, wx.EXPAND, 0)
        sizer_2.Add(self.CheckDontShowAgain, 0, wx.TOP|wx.BOTTOM, 10)
        sizer_2.Add(self.LabelOkCancelPlaceholder, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.ALL|wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = MyDialog(None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
