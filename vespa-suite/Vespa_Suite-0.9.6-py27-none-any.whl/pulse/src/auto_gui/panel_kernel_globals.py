#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Fri Jul 24 11:26:52 2015

import wx

# begin wxGlade: extracode
# end wxGlade


class PanelKernelGlobals(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelKernelGlobals.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.LabelTransformName = wx.StaticText(self, -1, "Transform Name")
        self.PanelFile1 = wx.Panel(self, -1)
        self.LabelFile1 = wx.StaticText(self.PanelFile1, -1, "Label File1")
        self.ButtonBrowseFile1 = wx.Button(self.PanelFile1, -1, "Browse")
        self.TextFile1 = wx.TextCtrl(self.PanelFile1, -1, "", style=wx.TE_READONLY)
        self.sizer_2_staticbox = wx.StaticBox(self.PanelFile1, -1, "File1 Selection")
        self.PanelFile2 = wx.Panel(self, -1)
        self.LabelFile2 = wx.StaticText(self.PanelFile2, -1, "Label File2")
        self.ButtonBrowseFile2 = wx.Button(self.PanelFile2, -1, "Browse")
        self.TextFile2 = wx.TextCtrl(self.PanelFile2, -1, "", style=wx.TE_READONLY)
        self.sizer_3_staticbox = wx.StaticBox(self.PanelFile2, -1, "File2 Selection")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelKernelGlobals.__set_properties
        self.TextFile1.SetMinSize((175, -1))
        self.TextFile2.SetMinSize((175, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelKernelGlobals.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.VERTICAL)
        grid_sizer_7 = wx.FlexGridSizer(1, 4, 4, 4)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        grid_sizer_6 = wx.FlexGridSizer(1, 4, 4, 4)
        sizer_4_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_4_copy.Add(self.LabelTransformName, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_4_copy, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_2.Add(self.LabelFile1, 0, wx.TOP | wx.BOTTOM | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_6.Add(self.ButtonBrowseFile1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6.Add(self.TextFile1, 0, wx.EXPAND, 0)
        grid_sizer_6.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        self.PanelFile1.SetSizer(sizer_2)
        sizer_4.Add(self.PanelFile1, 0, wx.ALL | wx.EXPAND, 4)
        sizer_3.Add(self.LabelFile2, 0, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_7.Add(self.ButtonBrowseFile2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_7.Add(self.TextFile2, 0, wx.EXPAND, 0)
        grid_sizer_7.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        self.PanelFile2.SetSizer(sizer_3)
        sizer_4.Add(self.PanelFile2, 0, wx.ALL | wx.EXPAND, 4)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        # end wxGlade

# end of class PanelKernelGlobals

class FrameKernelGlobals(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FrameKernelGlobals.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.PanelKernelGlobals = PanelKernelGlobals(self, -1)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FrameKernelGlobals.__set_properties
        self.SetTitle("frame_transform_core")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FrameKernelGlobals.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.PanelKernelGlobals, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class FrameKernelGlobals
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    FrameKernelGlobals = FrameKernelGlobals(None, -1, "")
    app.SetTopWindow(FrameKernelGlobals)
    FrameKernelGlobals.Show()
    app.MainLoop()
