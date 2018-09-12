#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Wed May 04 10:48:24 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class Panel_InterpolateRescale(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Panel_InterpolateRescale.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.label_ifsr = wx.StaticText(self, -1, "")
        self.CheckInterpolate = wx.CheckBox(self, -1, "Interpolate")
        self.LabelInterpolation = wx.StaticText(self, -1, "Interpol. Factor: ", style=wx.ALIGN_RIGHT)
        self.TextInterpolation = wx.TextCtrl(self, -1, "", style=wx.TE_CENTRE)
        self.LabelOldDwell = wx.StaticText(self, -1, "Current Dwell Time:")
        self.LabelCurrentDwellTime = wx.StaticText(self, -1, "xx.x", style=wx.ALIGN_CENTRE)
        self.LabelOldMs = wx.StaticText(self, -1, " microseconds")
        self.LabelDwell = wx.StaticText(self, -1, "New Dwell Time: ")
        self.TextDwellTime = wx.TextCtrl(self, -1, "", style=wx.TE_CENTRE)
        self.LabelNewMs = wx.StaticText(self, -1, " microseconds")
        self.sizer_3_staticbox = wx.StaticBox(self, -1, "Interpolate")
        self.CheckRescaling = wx.CheckBox(self, -1, "Rescaling")
        self.LabelAngle = wx.StaticText(self, -1, "On Resonance Tip: ")
        self.TextAngle = wx.TextCtrl(self, -1, "", style=wx.TE_CENTRE)
        self.sizer_5_staticbox = wx.StaticBox(self, -1, "Rescaling")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_CHECKBOX, self.on_checked_interpolate, self.CheckInterpolate)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_changed_interpolation_factor, self.TextInterpolation)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_changed_dwell_time, self.TextDwellTime)
        self.Bind(wx.EVT_CHECKBOX, self.on_checked_rescaling, self.CheckRescaling)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_changed_angle, self.TextAngle)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Panel_InterpolateRescale.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Panel_InterpolateRescale.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_5_staticbox.Lower()
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_6 = wx.GridSizer(1, 3, 0, 0)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_4 = wx.GridSizer(1, 3, 0, 0)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_7.Add(self.label_ifsr, 0, wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 2)
        sizer_2.Add(sizer_7, 0, wx.EXPAND, 0)
        grid_sizer_4.Add((20, 20), 0, 0, 0)
        grid_sizer_4.Add(self.CheckInterpolate, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 2)
        grid_sizer_4.Add((20, 20), 0, 0, 0)
        sizer_8.Add(grid_sizer_4, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.LabelInterpolation, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.TextInterpolation, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add((60, 8), 0, 0, 0)
        grid_sizer_2.Add(self.LabelOldDwell, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.LabelCurrentDwellTime, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.LabelOldMs, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.LabelDwell, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.TextDwellTime, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.LabelNewMs, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(grid_sizer_2, 1, wx.TOP|wx.EXPAND, 10)
        sizer_3.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 0, wx.BOTTOM|wx.EXPAND, 40)
        grid_sizer_6.Add((20, 20), 0, 0, 0)
        grid_sizer_6.Add(self.CheckRescaling, 0, 0, 0)
        grid_sizer_6.Add((20, 20), 0, 0, 0)
        sizer_13.Add(grid_sizer_6, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.LabelAngle, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.TextAngle, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add((60, 8), 0, 0, 0)
        sizer_13.Add(grid_sizer_1, 0, wx.TOP|wx.EXPAND, 10)
        sizer_5.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_5, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 3)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        # end wxGlade

    def on_checked_interpolate(self, event): # wxGlade: Panel_InterpolateRescale.<event_handler>
        print "Event handler `on_checked_interpolate' not implemented!"
        event.Skip()

    def on_text_changed_interpolation_factor(self, event): # wxGlade: Panel_InterpolateRescale.<event_handler>
        print "Event handler `on_text_changed_interpolation_factor' not implemented!"
        event.Skip()

    def on_text_changed_dwell_time(self, event): # wxGlade: Panel_InterpolateRescale.<event_handler>
        print "Event handler `on_text_changed_dwell_time' not implemented!"
        event.Skip()

    def on_checked_rescaling(self, event): # wxGlade: Panel_InterpolateRescale.<event_handler>
        print "Event handler `on_checked_rescaling' not implemented!"
        event.Skip()

    def on_text_changed_angle(self, event): # wxGlade: Panel_InterpolateRescale.<event_handler>
        print "Event handler `on_text_changed_angle' not implemented!"
        event.Skip()

# end of class Panel_InterpolateRescale


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_interpolate_rescale = Panel_InterpolateRescale(self, -1)

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
        sizer_1.Add(self.panel_interpolate_rescale, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
