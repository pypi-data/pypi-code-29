#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Feb 23 17:18:43 2011 from "/home/me/duke/src/vespa/common/wxglade/exception_report.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.sizer_5_staticbox = wx.StaticBox(self, -1, "Details")
        self.LabelMessage = wx.StaticText(self, -1, "Message text goes here")
        self.CopyDetails = wx.Button(self, -1, "Copy Details to Clipboard")
        self.CheckboxOpenEmail = wx.CheckBox(self, -1, "Open a new email on copy")
        self.TextDetails = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        self.ButtonDone = wx.Button(self, wx.ID_CANCEL, "Done")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_copy, self.CopyDetails)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.LabelMessage, 0, wx.ALL|wx.EXPAND, 10)
        sizer_4.Add(self.CopyDetails, 0, wx.BOTTOM, 10)
        sizer_4.Add(self.CheckboxOpenEmail, 0, wx.LEFT, 10)
        sizer_5.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.TextDetails, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_5, 1, wx.ALL|wx.EXPAND, 10)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_6.Add(self.ButtonDone, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_6, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def on_copy(self, event): # wxGlade: MyDialog.<event_handler>
        print "Event handler `on_copy' not implemented!"
        event.Skip()

# end of class MyDialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = MyDialog(None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
