#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Wed Aug 15 15:43:43 2012

import wx

# begin wxGlade: extracode
# end wxGlade


class WaterHammingUI(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: WaterHammingUI.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SpinLength = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100, style=wx.SP_ARROW_KEYS | wx.TE_AUTO_URL)
        self.ComboExtrap = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Linear", "AR Model"], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.SpinExtrap = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100, style=wx.SP_ARROW_KEYS | wx.TE_AUTO_URL)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_extrapolate_method, self.ComboExtrap)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: WaterHammingUI.__set_properties
        self.SpinLength.SetMinSize((60, -1))
        self.ComboExtrap.SetSelection(0)
        self.SpinExtrap.SetMinSize((60, -1))
        self.SpinExtrap.SetSize((40,-1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: WaterHammingUI.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        Length = wx.StaticText(self, wx.ID_ANY, "Hamming Filter Length:")
        sizer_3.Add(Length, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_3.Add(self.SpinLength, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_2.Add(sizer_3, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        LabelExtrap = wx.StaticText(self, wx.ID_ANY, "Extrapolation:")
        sizer_4.Add(LabelExtrap, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_4.Add(self.ComboExtrap, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        labelExtrap = wx.StaticText(self, wx.ID_ANY, "    Extrap Pts:")
        sizer_4.Add(labelExtrap, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_4.Add(self.SpinExtrap, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_2.Add(sizer_4, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        # end wxGlade

    def on_extrapolate_method(self, event):  # wxGlade: WaterHammingUI.<event_handler>
        print "Event handler `on_extrapolate_method' not implemented!"
        event.Skip()

# end of class WaterHammingUI

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.WaterHammingUI = WaterHammingUI(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.WaterHammingUI, 0, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
