#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Wed Apr 20 11:36:12 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.TextName = wx.TextCtrl(self, -1, "")
        self.TextComment = wx.TextCtrl(self, -1, "")
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "Pulse Description")
        self.TextAmpIntegral = wx.TextCtrl(self, -1, "")
        self.TextCalcAmpIntegral = wx.TextCtrl(self, -1, "")
        self.TextCalcAbsIntegral = wx.TextCtrl(self, -1, "")
        self.TextCalcPowerIntegral = wx.TextCtrl(self, -1, "")
        self.TextMinSliceThickness = wx.TextCtrl(self, -1, "")
        self.TextMaxSliceThickness = wx.TextCtrl(self, -1, "")
        self.TextReferenceGradient = wx.TextCtrl(self, -1, "")
        self.sizer_3_staticbox = wx.StaticBox(self, -1, "Pulse Characteristics")
        self.ButtonResetIntegral = wx.Button(self, -1, "Reset Integral")
        self.LabelOkCancelPlaceholder = wx.StaticText(self, -1, "Placeholder for OK/Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Export to Siemens")
        self.TextCalcAmpIntegral.Enable(False)
        self.TextCalcAbsIntegral.Enable(False)
        self.TextCalcPowerIntegral.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(7, 2, 2, 2)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 2, 2)
        label_1 = wx.StaticText(self, -1, "Name:")
        grid_sizer_1.Add(label_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_1.Add(self.TextName, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, -1, "Comment:")
        grid_sizer_1.Add(label_2, 0, wx.ALL, 4)
        grid_sizer_1.Add(self.TextComment, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, -1, "Amplitude Integral [opt]:")
        grid_sizer_2.Add(label_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextAmpIntegral, 0, wx.EXPAND, 0)
        label_4 = wx.StaticText(self, -1, "Calcul. Amplitude Integral [opt]:")
        grid_sizer_2.Add(label_4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextCalcAmpIntegral, 0, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, -1, "Calcul. Absolute Integral [opt]:")
        grid_sizer_2.Add(label_5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextCalcAbsIntegral, 0, wx.EXPAND, 0)
        label_6 = wx.StaticText(self, -1, "Cacul. Power Integral [opt]:")
        grid_sizer_2.Add(label_6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextCalcPowerIntegral, 0, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, -1, "MinSlice Thickness [mm]:")
        grid_sizer_2.Add(label_7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextMinSliceThickness, 0, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, -1, "MaxSlice Thickness [mm]:")
        grid_sizer_2.Add(label_8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextMaxSliceThickness, 0, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, -1, "Reference Gradient [mT/min]:")
        grid_sizer_2.Add(label_9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_2.Add(self.TextReferenceGradient, 0, wx.EXPAND, 0)
        grid_sizer_2.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 4)
        sizer_4.Add(self.ButtonResetIntegral, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 12)
        sizer_4_copy.Add(self.LabelOkCancelPlaceholder, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(sizer_4_copy, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_4, 0, wx.ALL|wx.EXPAND, 4)
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
