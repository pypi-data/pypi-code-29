#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Wed Oct 19 11:00:48 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.ListPulseSequences = wx.ListBox(self, -1, choices=[])
        self.ButtonCopy = wx.Button(self, -1, "Copy List to Clipboard")
        self.ButtonClose = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_copy, self.ButtonCopy)
        self.Bind(wx.EVT_BUTTON, self.on_close, id=wx.ID_CLOSE)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        self.SetSize((538, 462))
        self.ButtonClose.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.ListPulseSequences, 1, wx.ALL|wx.EXPAND, 10)
        sizer_2.Add(self.ButtonCopy, 0, 0, 0)
        sizer_2.Add((20, 20), 1, 0, 0)
        sizer_2.Add(self.ButtonClose, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL|wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_copy(self, event): # wxGlade: MyDialog.<event_handler>
        print "Event handler `on_copy' not implemented!"
        event.Skip()

    def on_close(self, event): # wxGlade: MyDialog.<event_handler>
        print "Event handler `on_close' not implemented!"
        event.Skip()

# end of class MyDialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = MyDialog(None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
