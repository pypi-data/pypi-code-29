#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Mon Jan 24 17:37:17 2011

import wx

# begin wxGlade: extracode
# end wxGlade




class PulseDesignBrowser(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PulseDesignBrowser.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.ListPulseDesigns = wx.ListBox(self, -1, choices=[])
        self.sizer_7_staticbox = wx.StaticBox(self, -1, "Pulse Designs")
        self.LabelHtml = wx.StaticText(self, -1, "At runtime this label is replaced by an HTML control")
        self.LabelOpenCancelPlaceholder = wx.StaticText(self, -1, "The Open and Cancel buttons are \nadded in the dialog init, not here.")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_list_double_click, self.ListPulseDesigns)
        self.Bind(wx.EVT_LISTBOX, self.on_list_click, self.ListPulseDesigns)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PulseDesignBrowser.__set_properties
        self.SetTitle("Pulse Project Browser")
        self.SetSize((652, 414))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PulseDesignBrowser.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_7_staticbox.Lower()
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 10, 5)
        sizer_7.Add(self.ListPulseDesigns, 5, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableCol(1)
        sizer_7.Add(grid_sizer_1, 1, wx.TOP | wx.BOTTOM | wx.EXPAND, 10)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_13.Add(self.LabelHtml, 0, 0, 0)
        sizer_10.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_11.Add(self.LabelOpenCancelPlaceholder, 0, 0, 0)
        sizer_10.Add(sizer_11, 0, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 0)
        sizer_5.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_list_double_click(self, event):  # wxGlade: PulseDesignBrowser.<event_handler>
        print "Event handler `on_list_double_click' not implemented!"
        event.Skip()

    def on_list_click(self, event):  # wxGlade: PulseDesignBrowser.<event_handler>
        print "Event handler `on_list_click' not implemented!"
        event.Skip()

# end of class PulseDesignBrowser
class PulseProjectBrowser(wx.Dialog):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

    def on_list_double_click(self, event): # wxGlade: PulseProjectBrowser.<event_handler>
        print "Event handler `on_list_double_click' not implemented!"
        event.Skip()

    def on_list_click(self, event): # wxGlade: PulseProjectBrowser.<event_handler>
        print "Event handler `on_list_click' not implemented!"
        event.Skip()

# end of class PulseProjectBrowser


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = PulseProjectBrowser(None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
