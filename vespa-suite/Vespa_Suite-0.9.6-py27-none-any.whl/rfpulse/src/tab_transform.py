# Python modules
from __future__ import division
import math
import os


# 3rd party modules
import wx
import matplotlib as mpl
import numpy as np

# Our modules
import prefs
import util_menu
import util_rfpulse_config
import plot_panel_transform
import run_transform_controller as rtc
import auto_gui.panel_tab_transform as panel_tab_transform
import auto_gui.panel_kernel_globals as panel_kernel_globals
import vespa.common.wx_gravy.common_dialogs as common_dialogs
import vespa.common.constants as constants
import vespa.common.util.misc as util_misc
import vespa.common.pulse_funcs.pulse_func_exception as pulse_func_exception
import vespa.common.pulse_funcs.util as pulse_funcs_util
        
        
PLOT_PANEL_X_BUMP = 0.02   
PLOT_PANEL_Y_BUMP = 0.1
       
# This is the row of lines that goes in the console to separate the messages
# of one run from another.
SEPARATOR = "-" * 60
 

class TabTransform(panel_tab_transform.PanelTabTransform):

    def __init__(self, inner_notebook, left_neighbor, 
                                       pulse_project,
                                       transform, 
                                       parent=None, 
                                       in_editor=False):

        if parent is None:
            parent = inner_notebook

        panel_tab_transform.PanelTabTransform.__init__(self, parent)

        # This tab needs to know who its left neighbor is during init. 
        # Ordinarily we get the left neighbor by asking the notebook 
        # "who is to the left of me?" But during init, the notebook doesn't 
        # know about "me" yet, so the notebook can't find this tab in the 
        # list of tabs and therefore can't determine who is to the left.
        # We resolve this annoyance by having the caller pass in the left 
        # neighbor as a param and stashing it in this attribute. Once init is
        # complete we clear the attribute and ignore it thereafter.
        self._left_neighbor = left_neighbor

        self._inner_notebook = inner_notebook
        self._pulse_project  = pulse_project
        
        self.parent = parent
        self.transform = transform
        self.in_editor = in_editor
        self._last_run = { }
        self._last_save = { }
        self._current_focus_id = None
        
        self._prefs = prefs.PrefsMain()

        # user_parameter_controls is a list of lists. The inner lists contain
        # one row each of parameter controls.
        self.user_parameter_controls = []

        # local storage for possible profile plot data
        self.profile = None
        self.profile_ext = None
        self.profile_grad_refocus = None

        self.initialize_kernel_controls()
        self.initialize_display_controls()
        
        # plot_init creates placeholder line2D objects in each of 
        # the 9 axes that were created to display results
        self.plot_init()
        
        # we default to not showing any axes on initialization
        self.view.display_naxes([False,False,False,False,False,False,False,False,False])
        
        # we call plot here in case this is an existing pulse_project
        # being loaded into memory that already has results to plot.
        self.plot(relim_flag=True)
        
        # Setting the sash position won't work if the containing window 
        # hasn't sized itself yet, and that's the case under GTK and Windows.
        # So we use the CallAfter hack to allow the window to settle down 
        # before the call to SetSashPosition(). Under OSX, the call to 
        # SetSashPosition() works regardless of whether we call it directly
        # here or via wx.CallAfter().
        wx.CallAfter(self.window_splitter.SetSashPosition, 440, True)
        
        self.Layout()   
        self.Fit()

        self.Bind(wx.EVT_WINDOW_DESTROY, self.on_destroy, self)
        self.Bind(wx.EVT_CHILD_FOCUS, self.on_child_focus)


    @property
    def is_saved(self):
        """True if the current input is the same as it was when the tab
        was last saved.
        """
        return self._last_save == self.get_raw_gui_data()


    @property
    def is_synced(self):
        """True if the current input is in sync with the results."""
        if self.transform.result and (self.get_raw_gui_data() == self._last_run):
            # I'm only in sync if my left neighbor is is sync. If not, then
            # the results that were passed to me as input are no longer valid.
            if self.left_neighbor:
                return self.left_neighbor.is_synced
            else:
                return True
        else:
            # Definitely not in sync
            return False


    @property
    def left_neighbor(self):
        """
        Returns the tab that is the left neighbor of this one, or
        None if there is no left neighbor.
        
        """
        # We use self._left_neighbor while it's populated (during init), but
        # not thereafter.
        if self._left_neighbor:
            return self._left_neighbor
        else:
            return self._inner_notebook.get_left_neighbor(self)


    ##### Event Handlers ######################################################

    def on_activation(self):
        # This is a faux event handler. wx doesn't call it directly. It's 
        # a notification from my parent (the experiment notebook) to let
        # me know that this tab has become the current one.
        
        # Force the View menu to match the current plot options.
        util_menu.bar.set_menu_from_state(self._prefs.menu_state)

               
    def on_child_focus(self, event):
        # When the focus changes we take the opportunity to note if the 
        # user has made any changes and, if so, we update the sync status
        # indicator. The project notebook actually does that work; this 
        # is just a trigger.
        
        # The wx doc for wxChildFocusEvent says --
        # "Notice that child window is the direct child of the window 
        # receiving event. Use FindFocus to retreive [sic] the window which  
        # is actually getting focus."
        recipient = wx.Window.FindFocus()

        # I'm not sure why, but we seem to get a surplus of these messages.
        # Here we ensure that the focus really is somewhere else.
        if self._current_focus_id != recipient.Id:
            # Focus changed
            self._current_focus_id = recipient.Id            
            self._inner_notebook.update_sync_status(self)
                
                
    def on_destroy(self, event):
        self._prefs.save()


    def on_browse_file1(self, event):
        dialog = wx.FileDialog(self)
        if wx.ID_OK == dialog.ShowModal():
            file_path = dialog.GetPath()
            self.panel_kernel_globals.TextFile1.SetValue(file_path)
#            self.transform.parameters['file1'][0] = file_path
            self._inner_notebook.update_sync_status()


    def on_browse_file2(self, event):
        dialog = wx.FileDialog(self)
        if wx.ID_OK == dialog.ShowModal():
            file_path = dialog.GetPath()
            self.panel_kernel_globals.TextFile2.SetValue(file_path)
#            self.transform.parameters['file2'][0] = file_path
            self._inner_notebook.update_sync_status()
                
                
    def on_run(self, event):
        """ 
        See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        """
        self._inner_notebook.run(self)


    def on_usage(self, event):
        
        use_type = self.ComboUsageType.GetStringSelection()

# bjs-start - temporary comment out to do a release without Grad_Refocus

        use_type = constants.UsageType.get_type_for_value(use_type, 'display')
        
        if use_type == constants.UsageType.EXCITE:
            self.PanelGradRefocus.Show()
        else:
            self.PanelGradRefocus.Hide()
            self.CheckGradRefocus.SetValue(False)
        self.PanelLeftSide.Layout()
        self.PanelLeftSide.Refresh()        
        
        self.plot(update_profiles=True, relim_flag=True)
# bjs-end - temporary comment out to do a release without Grad_Refocus


    def on_check(self, event):
        self.plot()


    def on_check_grad_refocus(self, event):
        result = self.transform.result
        if result:
            self.plot(update_profiles=True)
        
        
    def on_float_grad_refocus(self, event):
        result = self.transform.result
        if result: 
            self.plot(update_profiles=True, update_refocus=True)


    def on_menu_view_option(self, event):
        event_id = event.GetId()

        if self._prefs.handle_event(event_id):
            if event_id == util_menu.ViewIds.ZERO_LINE_SHOW:
                for i, axes in enumerate(self.view.all_axes):
                    axes.lines[2].set_visible(self._prefs.zero_line_show)
                self.view.canvas.draw()      
        
            elif event_id == util_menu.ViewIds.XAXIS_SHOW:
                for i, axes in enumerate(self.view.all_axes):
                    axes.xaxis.set_visible(self._prefs.xaxis_show)
                self.view.canvas.draw()
        
            elif event_id in (util_menu.ViewIds.DATA_TYPE_REAL,
                              util_menu.ViewIds.DATA_TYPE_REAL_IMAGINARY,
                             ):
                if self.transform and self.transform.result:
                    for i, axes in enumerate(self.view.all_axes):
                        if self._prefs.data_type_real:
                            axes.lines[1].set_visible(False)
                        if self._prefs.data_type_real_imaginary:
                            if i in [0,2,4,8]:
                                axes.lines[1].set_visible(True)
                    self.view.canvas.draw()
                

    def on_menu_view_output(self, event):
        event_id = event.GetId()

        formats = { util_menu.ViewIds.VIEW_TO_PNG : "PNG",
                    util_menu.ViewIds.VIEW_TO_SVG : "SVG", 
                    util_menu.ViewIds.VIEW_TO_EPS : "EPS", 
                    util_menu.ViewIds.VIEW_TO_PDF : "PDF", 
                  }

        if event_id in formats:
            format = formats[event_id]
            lformat = format.lower()
            filter_ = "%s files (*.%s)|*.%s" % (format, lformat, lformat)
            figure = self.view.figure

            filename = common_dialogs.save_as("", filter_)

            if filename:
                msg = ""
                try:
                    figure.savefig( filename,
                                    dpi=300, 
                                    facecolor='w', 
                                    edgecolor='w',
                                    orientation='portrait', 
                                    papertype='letter', 
                                    format=None,
                                    transparent=False)
                except IOError:
                    msg = """I can't write the file "%s".""" % filename
                
                if msg:
                    common_dialogs.message(msg, style=common_dialogs.E_OK)


    ##### Internal helper functions  ##########################################

    def clear_result(self):
        """Destroys this tab's result and forces the plot to redraw."""
        self.transform.result = None
        self.plot()

        
    def complete_init(self, is_new):
        if not is_new:
            self._last_run.update(self.get_raw_gui_data())
            self._last_save.update(self.get_raw_gui_data())

        # We use _left_neighbor during init but not thereafter.
        self._left_neighbor = None


    def accept_gui_data(self):
        """ See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        """
        d = self.get_cooked_gui_data()
        self.transform.parameters = d
        

    def get_raw_gui_data(self):
        """ 
        See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        """

        kernel = self.transform.transform_kernel
        
        d = {}
        if not kernel.hide_file1:
            value = self.panel_kernel_globals.TextFile1.GetValue().strip()
            d['file1'] = [value, '(File)']

        if not kernel.hide_file2:
            value = self.panel_kernel_globals.TextFile2.GetValue().strip()
            d['file2'] = [value, '(File)']

        # pulse sequence static user parameters
        for control in self.user_parameter_controls:

            key   = control[3]
            type_ = control[2].GetLabel().strip()
            if type_ == '(Choice)':
                value = control[1].GetSelection()
            else:
                value = control[1].GetValue().strip()
    
            d[key] = [value, type_]

        return d
            

    def get_cooked_gui_data(self):
        """ 
        See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        """
        d = self.get_raw_gui_data()
       
        for key in d.keys():
           
            type_ = d[key][1]
            value = d[key][0]
            
            if type_ == "(Double)":
                d[key] = float(value)
            elif type_ == "(Long)":
                d[key] = int(value)

            # Note. types File and String are already in their final forms.

        return d


    def validate_gui(self):
        """ 
        See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        """
        msg = ""

        d = self.get_raw_gui_data()
       
        for key in d.keys():
           
            type_ = d[key][1]
            value = d[key][0]
            
            if type_ == "(Double)":
                if not util_misc.is_floatable(value):
                    msg = """I don't understand the %s parameter value "%s".""" % (key,value)
            elif type_ == "(Long)":
                if not util_misc.is_intable(value):
                    msg = """I don't understand the %s parameter value "%s".""" % (key,value)
            elif type_ == "(String)":
                if value == '':
                    msg = """Please enter a value for the "%s" parameter".""" % key
            elif type_ == "(Choice)":
                if not util_misc.is_intable(value):
                    msg = """I don't understand the choice %s parameter value "%s".""" % (key,value)
            elif type_ == "(File)":
                if value == '':
                    msg = """Please enter a file name for the "%s" parameter".""" % key
                
            if msg:
                # No point in going through the other controls.
                break
                 
        if not msg:
            # At this point we know all of the fields can be cooked. The rest
            # of the validation we have to do is on the cooked data, so we
            # grab it here.
            d = self.get_cooked_gui_data()


        if not msg:
            duration = pulse_funcs_util.check_and_suggest_duration(
                        d["time_steps"], d["duration"],
                        self._pulse_project.machine_settings.min_dwell_time,
                        self._pulse_project.machine_settings.dwell_time_increment,
                        )
                                                        
            if duration != d["duration"]:
                msg = "The duration should be %s to accommodate your "      \
                      "time steps and machine settings (minimum dwell "     \
                      "time and dwell time increment). Would you like "     \
                      "to change the duration to %s?"
                s = ("%f" % duration).strip("0")
                msg = msg % (s, s)
                 
                if wx.YES == common_dialogs.message(msg, None, common_dialogs.Q_YES_NO):
                    msg = ""

                    kernel = self.transform.transform_kernel
                    for control in self.user_parameter_controls:
                        key = control[3]
                        if key == "duration":
                            value = control[1]
                            value.SetValue(str(duration))
                            # I force the window to update right away so that it 
                            # changes before the GUI freezes while running. 
                            value.Update()
                            break
                else:
                    msg = "Please change the duration or number of time steps."
 
        if not msg:
            # Warn if time_steps are greater than 1/4 of calc_resolution.
            calc_resolution = self._inner_notebook.get_current_calc_resolution()
             
            if util_misc.is_intable(calc_resolution):
                calc_resolution = int(calc_resolution)
 
                if calc_resolution < (d["time_steps"] * 4):
                    msg = "For best results, the calculation resolution "   \
                          "(currently %d) should be at least four times "   \
                          "wider than the number of time steps.\n\n"        \
                          "Do you want to continue with the current values?"
                           
                    msg = msg % calc_resolution
                           
                    if wx.NO == common_dialogs.message(msg, None, common_dialogs.Q_YES_NO):
                        msg = "Please adjust the calculation resolution or " \
                              "the number of time steps."
                    else:
                        msg = ""

        if msg:
            self._inner_notebook.activate_tab(self)
            common_dialogs.message(msg)

        return not bool(msg)        
        

    def initialize_kernel_controls(self):

        # sizers that hold the global and user parameter controls
        self.sizer_global_parameters = self.LabelPlaceholder2.GetContainingSizer()
        self.sizer_user_parameters   = self.LabelPlaceholder3.GetContainingSizer()

        self.LabelPlaceholder2.Destroy()
        self.LabelPlaceholder3.Destroy()
        
        # insert global controls panel onto transform tab
        self.panel_kernel_globals = panel_kernel_globals.PanelKernelGlobals(self.PanelTransformKernel)
        self.sizer_global_parameters.Insert(0, self.panel_kernel_globals, flag=wx.EXPAND)

        # add/modify any dynamic user controls to transform tab        
        self.set_kernel_controls(self.transform.transform_kernel)
        
        self.PanelTransformKernel.Layout()
        
        self.Bind(wx.EVT_BUTTON, self.on_browse_file1, self.panel_kernel_globals.ButtonBrowseFile1)
        self.Bind(wx.EVT_BUTTON, self.on_browse_file2, self.panel_kernel_globals.ButtonBrowseFile2)
        
    
    
    def update_kernel_controls(self, kernel):
        """
        This method updates and existing panel of user defined controls in a 
        TabTransform. This typically happens over and over in the TransformKernel 
        editor.
        
        The old set of user defined transform kernel controls are deleted and
        the new set created in the existing TabTransform. The old parameter 
        values stored in the Transform object are also deleted. The new set of
        controls are initialized to default values from the TranformKernel
        user_parameters objects
        
        """
        self.transform.transform_kernel = kernel
        self.transform.parameters = {}
        
        #------------------------------------------------------------
        # Modify any Global parameters

        globals = self.panel_kernel_globals
        
        globals.LabelTransformName.SetLabel("Transform Name : "+kernel.name)
        
        globals.PanelFile1.Hide() if kernel.hide_file1 else globals.PanelFile1.Show()
        globals.PanelFile2.Hide() if kernel.hide_file2 else globals.PanelFile2.Show()
        
        globals.LabelFile1.SetLabel(kernel.file1_label)
        globals.LabelFile2.SetLabel(kernel.file2_label)
        globals.TextFile1.ChangeValue(str(kernel.file1))
        globals.TextFile2.ChangeValue(str(kernel.file2))

        #------------------------------------------------------------
        # Remove current user defined parameter controls

        # grid sizer that holds the user's input controls
        sizer = self.sizer_user_parameters 
        for control_group in self.user_parameter_controls:
            for control in control_group:
                # last 'control' is just a string, skip destroying that
                if not isinstance(control, basestring):
                    control.Destroy()
        self.user_parameter_controls = []

        #------------------------------------------------------------
        # Insert new user defined parameter controls

        parameters = kernel.user_parameters
 
        # There are three columns, one for the descriptive label, one for the
        # textbox that holds the default value, and one for another label that 
        # describes the type (string, double, etc.)
        sizer.SetCols(3)
        sizer.SetRows(len(parameters))

        # Create one row of new controls for each param
        for parameter in parameters:
            name = parameter.name
            if not name.endswith(":"):
                name += ":"
            name_label = wx.StaticText(self.PanelTransformKernel, wx.ID_ANY, name)
            sizer.Add(name_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5)
     
            if parameter.type != 'Choice':
                textbox = wx.TextCtrl(self.PanelTransformKernel)
                textbox.ChangeValue(parameter.default)
                sizer.Add(textbox, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
            else:
                entries = parameter.default.split(",")
                textbox = wx.Choice(self.PanelTransformKernel, -1, choices=entries)
                textbox.SetSelection(0)
                sizer.Add(textbox, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
                
            type_label = wx.StaticText(self.PanelTransformKernel, wx.ID_ANY, "(%s)" % parameter.type)
            sizer.Add(type_label, 0, wx.ALIGN_CENTER_VERTICAL)
            variable = parameter.variable
 
            self.user_parameter_controls.append( (name_label, textbox, type_label, variable) )

        self.PanelTransformKernel.Layout()

#         # wx sets tab order according to control creation order. Since I 
#         # just created controls, they'll be *after* the Run button in the
#         # tab order which is wrong. Here I correct the tab order.
#         if self.user_parameter_controls:
#             last_control = self.user_parameter_controls[-1][-1]
#         else:
#             last_control = self.TextBandwidth


    def set_kernel_controls(self, kernel):
        """
        This method sets up the user defined transform kernel controls with
        parameter values stored in the Transform object. NOT the default 
        values from the transform kernel.  It assumes that the 'parameters'
        dict is appropriately formed.
        
        """
        self.transform.transform_kernel = kernel
        values = self.transform.parameters

        #------------------------------------------------------------
        # Modify any Global parameters

        globals = self.panel_kernel_globals
        
        globals.LabelTransformName.SetLabel("Transform Name : "+kernel.name)
        
        if kernel.hide_file1: 
            globals.PanelFile1.Hide() 
            globals.TextFile1.ChangeValue('')
        else: 
            globals.PanelFile1.Show()
            globals.TextFile1.ChangeValue(str(values['file1'][0]))
            
        if kernel.hide_file2:
            globals.PanelFile2.Hide()
            globals.TextFile2.ChangeValue('')  
        else: 
            globals.PanelFile2.Show()
            globals.TextFile2.ChangeValue(str(values['file2'][0]))
        
        globals.LabelFile1.SetLabel(kernel.file1_label)
        globals.LabelFile2.SetLabel(kernel.file2_label)
        
        #------------------------------------------------------------
        # Add any User Defined parameters

        parameters = kernel.user_parameters

        # grid sizer that holds the user's input controls
        sizer = self.sizer_user_parameters 
        
        # Get rid of any existing user defined controls
        for control_group in self.user_parameter_controls:
            for control in control_group:
                # last 'control' is just a string, skip destroying that
                if not isinstance(control, basestring):
                    control.Destroy()
        self.user_parameter_controls = []
 
        # There are three columns, one for the descriptive label, one for the
        # textbox that holds the default value, and one for another label that 
        # describes the type (string, double, etc.)
        sizer.SetCols(3)
        sizer.SetRows(len(parameters))

        # Create one row of new controls for each param
        for parameter in parameters:
            key  = parameter.variable
            name = parameter.name
            if not name.endswith(":"):
                name += ":"
            name_label = wx.StaticText(self.PanelTransformKernel, wx.ID_ANY, name)
            sizer.Add(name_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5)
     
            if parameter.type != 'Choice':
                textbox = wx.TextCtrl(self.PanelTransformKernel)
                textbox.ChangeValue(str(values[key][0]))
                sizer.Add(textbox, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
            else:
                entries = parameter.default.split(",")
                textbox = wx.Choice(self.PanelTransformKernel, -1, choices=entries)
                textbox.SetSelection(0)
                sizer.Add(textbox, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
                
            type_label = wx.StaticText(self.PanelTransformKernel, wx.ID_ANY, "(%s)" % parameter.type)
            sizer.Add(type_label, 0, wx.ALIGN_CENTER_VERTICAL)
            variable = parameter.variable
 
            self.user_parameter_controls.append( (name_label, textbox, type_label, variable) )
                
        self.PanelTransformKernel.Layout()

#         # wx sets tab order according to control creation order. Since I 
#         # just created controls, they'll be *after* the Run button in the
#         # tab order which is wrong. Here I correct the tab order.
#         if self.user_parameter_controls:
#             last_control = self.user_parameter_controls[-1][-1]
#         else:
#             last_control = self.TextBandwidth
        
        
    def initialize_display_controls(self):
        
        self.ComboUsageType.Clear()        
        self.ComboUsageType.AppendItems( \
                            [constants.UsageType.EXCITE['display'], \
                             constants.UsageType.INVERSION['display'], \
                             constants.UsageType.SATURATION['display'], \
                             constants.UsageType.SPIN_ECHO['display']])

        # Small hack for OS X problem -- this combobox believes it is sized
        # correctly but paints itself only about 15 pixels wide. Slightly
        # altering the size gives OS X the nudge it needs to render it 
        # correctly. I'm sure there's a more elegant solution but I had 
        # trouble finding one.
        x, y = self.ComboUsageType.GetSizeTuple()
        self.ComboUsageType.SetMinSize( (x - 1, y) )
       
        # Add a plot_panel to right splitter window
        self.view = plot_panel_transform.PlotPanelTransform(self.PanelRhs,
                                                naxes=9,
                                                reversex=False,
                                                zoom='box', 
                                                reference=True,
                                                unlink=True,
                                                do_zoom_select_event=False,
                                                do_zoom_motion_event=True,
                                                do_refs_select_event=False,
                                                do_refs_motion_event=True,
                                                xscale_bump = PLOT_PANEL_X_BUMP,
                                                yscale_bump = PLOT_PANEL_Y_BUMP,
                                                props_zoom=dict(alpha=0.2, facecolor='yellow'),
                                                props_cursor=dict(alpha=0.1, facecolor='gray'))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.view, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.PanelRhs.SetSizer(sizer)
        self.view.Fit()    

        self.view.figure.set_facecolor('white')
        for axes in self.view.axes:
            axes.set_axis_bgcolor(self._prefs.bgcolor)
            mpl.artist.setp(axes.axes.xaxis, visible=True)
            self.view.figure.subplots_adjust(left=0.12,right=0.98,
                                               bottom=0.05,top=0.95,
                                               wspace=0.0,hspace=0.3)
        
        # default plot settings on startup for all transforms
        self.CheckWaveform.SetValue(True)        
        self.ComboUsageType.SetStringSelection(constants.UsageType.EXCITE['display'])

        if not self.transform.result:
            grad_refocus_fraction = 0.0
        else:
            grad_refocus_fraction = self.transform.result.grad_refocus_fraction

        result = self.transform.result
        if result:
            if grad_refocus_fraction == 0.0:
                result.gradient_refocusing()
                grad_refocus_fraction = result.grad_refocus_fraction
            else:
                result.gradient_refocusing(grad_refocus_fraction)
            self.profile_grad_refocus = result.refocused_profile

        self.FloatGradRefocus.SetMinSize((75, -1))
        self.FloatGradRefocus.SetSize((75, -1))
        self.FloatGradRefocus.SetDigits(5)
        self.FloatGradRefocus.SetIncrement(0.0005)
        self.FloatGradRefocus.SetRange(0.0, 1.0)
        self.FloatGradRefocus.SetValue(grad_refocus_fraction)      

        self.PanelGradRefocus.Hide()

# bjs-start - temporary comment out to do release without Grad_Refocus

        use_type = self.ComboUsageType.GetStringSelection()
        use_type = constants.UsageType.get_type_for_value(use_type, 'display')
        if use_type == constants.UsageType.EXCITE:
            self.PanelGradRefocus.Show()
        else:
            self.PanelGradRefocus.Hide()

# bjs-end - temporary comment out to do a release without Grad_Refocus

    def on_save(self):
        self._last_save = self.get_raw_gui_data()


    def update_sync_status(self):
        """ See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        """
        # Subclasses may override this
        pass


    def run(self):
        """ 
        See documentation here:
        http://scion.duhs.duke.edu/vespa/rfpulse/wiki/CommonTabFeatures
        
        """
        # All is well, time to Run Algorithm and Bloch simulation ---------
        #
        # this section copies values from widgets into the RFPulse project
        # object for a number of input parameters

        if self.in_editor:
            self._inner_notebook.say("\nStarting Pulse test ...\n")
        
        results, failed = rtc.run_transform(self.transform)
                
        if failed:
            successful = False
            msg = rtc.exception_to_message(failed[0])
            if self.in_editor:
                # write message to Console widget in editor
                self._inner_notebook.say(msg + "\n")
                self._inner_notebook.say("Test run finished with errors.\n")
            else:
                common_dialogs.message(msg, "Error Generating Pulse", wx.ICON_ERROR | wx.OK)
        else:
            successful = True
            msg = ""
            if self.in_editor:
                # write message to Console widget in editor
                self._inner_notebook.say("Test run finished successfully.\n")
                self._inner_notebook.say("Results plotting to display canvas.\n")
                self._inner_notebook.say(SEPARATOR) 
            
            # Since we only asked for one transform, we get only one result
            results = results[0]
            self.transform.result.rf_waveform = results['rf_waveform']
            self.transform.result.rf_xaxis    = results['rf_xaxis']
            self.transform.result.gradient    = results['gradient']
            self.transform.result.grad_xaxis  = results['grad_xaxis']

        if successful:
            self._last_run.update(self.get_raw_gui_data())   
            # Generate new frequency profiles here, using the Bloch equations.
            master_parameters = self._inner_notebook.pulse_project.master_parameters
            self.transform.result.update_profiles(master_parameters.calc_resolution)
       
            self.plot(update_profiles=True)
        
        return successful
    
    

    def plot(self, update_profiles=False, relim_flag=False, update_refocus=False):            
        '''
        Here we either update the data in each axes in the plot_panel or just
        select which ones to display in the figure. If "update_profiles" is
        True then we go through each axes, calculate the profile and extended
        profile based on the usage_type and then plot the real, imag and zero
        line into lines[0], [1] and [2] respectively. We then go through and
        make lines visible or not and xaxis on/off depending on prefs.
        '''
        if not self.transform or not self.transform.result:
            # Clear the plot.
            for axes in self.view.all_axes:
                for line in axes.lines:
                    line.set_visible(False)
                axes.xaxis.set_visible(False)
    
            self.view.canvas.draw()
            return
        
        checks = []
        checks.append(self.CheckProfile.IsChecked())
        checks.append(self.CheckAbsolute.IsChecked())
        checks.append(self.CheckProfileExtended.IsChecked())
        checks.append(self.CheckAbsoluteExtended.IsChecked())
        checks.append(self.CheckGradient.IsChecked())
        checks.append(self.CheckWaveform.IsChecked())
        checks.append(self.CheckWaveformMagn.IsChecked())
        checks.append(self.CheckWaveformPhase.IsChecked())
#        checks.append(self.CheckContour.IsChecked())
        checks.append(self.CheckGradRefocus.IsChecked())
        # tell the view which plot axes to include in the figure
        self.view.display_naxes(checks)
        naxes = len(self.view.figure.axes) 
        
        if naxes == 0: return
        
        fsize = ['medium','medium','small','small','x-small','x-small','x-small','x-small','x-small']
        fsize = fsize[naxes-1]
        use_type = self.ComboUsageType.GetStringSelection()
        use_type = constants.UsageType.get_type_for_value(use_type, 'display')

        if update_profiles != False or self.profile == None or self.profile_ext == None:
            result = self.transform.result
            self.profile     = result.get_profile(use_type, False, False)
            self.profile_ext = result.get_profile(use_type, True, False)
            if self.CheckGradRefocus.GetValue():
                grad_value = self.FloatGradRefocus.GetValue()
                if grad_value == 0.0:
                    result.gradient_refocusing()
                    self.FloatGradRefocus.SetValue(result.grad_refocus_fraction)
                else:
                    result.gradient_refocusing(grad_value)
                self.profile_grad_refocus = result.refocused_profile
            if self.profile_grad_refocus is None:
                 self.profile_grad_refocus = self.profile[0] * 0.0
            
            # :FIXME: For the next 4 plots .. Will these 
            # always be in Frequency or will we allow it 
            # in spatial coordinates (e.g. millimeters).

            # Frequency Profile  
            fy, fx = self.profile
            fx0 = np.array(fx)
            fx1 = np.array(fx)
            fy0 = np.array([i.real for i in fy])            
            fy1 = np.array([i.imag for i in fy])
            axes = self.view.all_axes[0]
            axes.lines[0].set_xdata(fx0)
            axes.lines[0].set_ydata(fy0)
            axes.lines[1].set_xdata(fx1)
            axes.lines[1].set_ydata(fy1)

            # Absolute Frequency Profile
            fy, fx = self.profile 
            fy = abs(fy)
            axes = self.view.all_axes[1]
            axes.lines[0].set_xdata(np.array(fx))
            axes.lines[0].set_ydata(np.array([i.real for i in fy]))
            axes.lines[1].set_visible(False)

            # Extended Frequency Profile  
            fy, fx = self.profile_ext
            axes = self.view.all_axes[2]
            axes.lines[0].set_xdata(np.array(fx))
            axes.lines[0].set_ydata(np.array([i.real for i in fy]))
            axes.lines[1].set_xdata(np.array(fx))
            axes.lines[1].set_ydata(np.array([i.imag for i in fy]))

            # Extended Absolute Frequency Profile  
            fy, fx = self.profile_ext
            fy = abs(fy)
            axes = self.view.all_axes[3]
            axes.lines[0].set_xdata(np.array(fx))
            axes.lines[0].set_ydata(np.array([i.real for i in fy]))
            axes.lines[1].set_visible(False)

            # Gradient Waveform
            fy, fx = result.get_gradient()
            fx0 = np.array([t*1000 for t in fx])
            axes = self.view.all_axes[4]
            axes.lines[0].set_xdata(np.array(fx0))
            axes.lines[0].set_ydata(np.array(fy))
            axes.lines[1].set_visible(False)

            # Time Waveform
            fx  = result.rf_xaxis
            fy  = result.rf_waveform
            fx0 = np.array([t*1000 for t in fx])
            fx1 = np.array([t*1000 for t in fx])
            
            # Multiply by 1000 to convert to microtesla.
            fy0 = np.array([i.real*1000 for i in fy])            
            fy1 = np.array([i.imag*1000 for i in fy])
            
            # Next 4 lines added so that plot of results spans
            # the total time desired: Each point represents a value 
            # for a time period equal to the dwell time.
            # Note this is similar to what J.M. does in Matpulse.
            # see MATPULSE/CPLANE/MCLB1FIG.M
            # e.g.
            # % To make stairs look 'right'
            # k = length(b1) ;    
            # c1 = 1000*real(b1) ;
            # c1(k+1) = c1(k) ;
            # d1 = 1000*imag(b1) ;
            # d1(k+1) = d1(k) ;
            fx0 = np.append(fx0, fx0[-1] + result.dwell_time/1000)
            fx1 = np.append(fx1, fx1[-1] + result.dwell_time/1000)
            fy0 = np.append(fy0, fy0[-1])
            fy1 = np.append(fy1, fy1[-1])
            
            axes = self.view.all_axes[5]  
            axes.lines[0].set_xdata(fx0)
            axes.lines[0].set_ydata(fy0)
            axes.lines[1].set_xdata(fx1)
            axes.lines[1].set_ydata(fy1)

            # Time Waveform (Magnitude)
            fx  = result.rf_xaxis
            fy  = result.rf_waveform
            fx0 = np.array([t*1000 for t in fx])
            fy0 = np.array([np.abs(i)*1000.0 for i in fy])  # Multiply by 1000 to convert to microtesla.

            axes = self.view.all_axes[6]
            axes.lines[0].set_xdata(fx0)
            axes.lines[0].set_ydata(fy0)
            axes.lines[1].set_visible(False)

            # Time Waveform (Phase Degrees)
            fx = result.rf_xaxis
            fy = result.rf_waveform
            fx0 = np.array([t*1000 for t in fx])
            fy0 = np.array([np.angle(i, deg=True) for i in fy])

            axes = self.view.all_axes[7]
            axes.lines[0].set_xdata(fx0)
            axes.lines[0].set_ydata(fy0)
            axes.lines[1].set_visible(False)
            
#             # B1 Contour Profile Plot 
#             fy, fx = self.profile
#             axes = self.view.all_axes[8]
#             axes.lines[0].set_xdata(np.array(fx))
#             axes.lines[0].set_ydata(np.array([i.real for i in fy]))
#             axes.lines[1].set_xdata(np.array(fx))
#             axes.lines[1].set_ydata(np.array([i.imag for i in fy]))

            # Grad Refocused Profile  
            fy = self.profile_grad_refocus
            _, fx = self.profile
            axes = self.view.all_axes[8]
            axes.lines[0].set_xdata(np.array(fx))
            axes.lines[0].set_ydata(np.array([i.real for i in fy]))
            axes.lines[1].set_xdata(np.array(fx))
            axes.lines[1].set_ydata(np.array([i.imag for i in fy]))

        for i in range(9):
            self.format_plot(self.view.all_axes[i], i, use_type,  fsize)
            
        for i, axes in enumerate(self.view.all_axes):
            if self._prefs.data_type_real:
                axes.lines[0].set_visible(True)
                axes.lines[1].set_visible(False)
            if self._prefs.data_type_real_imaginary:
                axes.lines[0].set_visible(True)
                if i in [0,2,5,8]:
                    axes.lines[1].set_visible(True)
            axes.lines[2].set_visible(self._prefs.zero_line_show)
            axes.xaxis.set_visible(self._prefs.xaxis_show)

        for i, axes in enumerate(self.view.figure.axes):
            axes.change_geometry(naxes,1,i+1)

        if relim_flag or update_profiles and not update_refocus:
            # here we bump out the viewing window a bit on the
            # overall plot so we can get a zoom box around the
            # all sides of the plotted data
            for axes in self.view.all_axes:
                # first calculate the tight bounds for data
                x  = axes.lines[0].get_xdata()
                y0 = axes.lines[0].get_ydata()
                y1 = axes.lines[1].get_ydata()
                xmin = min(x)
                xmax = max(x)
                ymin = min([min(y0),min(y1)])
                ymax = max([max(y0),max(y1)])
                if xmin == xmax:
                    # Workaround for ticket #24:
                    # http://scion.duhs.duke.edu/vespa/project/ticket/24
                    xmax += np.finfo(type(xmax)).eps
                axes.set_xlim([xmin,xmax])
                if ymin == ymax:
                    # Workaround for ticket #24:
                    # http://scion.duhs.duke.edu/vespa/project/ticket/24
                    ymax += np.finfo(type(ymax)).eps
                axes.set_ylim([ymin,ymax])
                axes.ignore_existing_data_limits = True
                axes.update_datalim([[xmin,ymin],[xmax,ymax]])
                # now loosen the bounds a bit for display purposes
                x0, y0, x1, y1 = axes.dataLim.bounds  
                xdel = PLOT_PANEL_X_BUMP*np.abs(x1-x0)
                ydel = PLOT_PANEL_Y_BUMP*np.abs(y1-y0)
                axes.set_xlim(x0-xdel,x0+x1+xdel)
                axes.set_ylim(y0-ydel,y0+y1+ydel)
                
                      
        self.view.canvas.draw()       


    def plot_init(self):
        '''
        This method plots place holder data into all axes so that
        from here on out all we have to do is set_xdata() and set_ydata()
        rather than recreating new plots in each axis. This way we keep
        the same xlim and ylim values as plots are turned off/on 
        '''
        for i,axes in enumerate(self.view.all_axes):
            axes.cla()
            x = np.arange(255)*10/255.0
            y = np.zeros(255)
            
            width = self._prefs.line_width
            color_real = self._prefs.line_color_real
            color_imag = self._prefs.line_color_imaginary
            color_magn = self._prefs.line_color_magnitude
            color_phas = self._prefs.line_color_phase_degrees
            
            if i == 0 or i == 2:    # waveform and extended waveform
                axes.plot(x, y, color=color_real, linewidth=width)
                axes.plot(x, y, color=color_imag, linewidth=width)
            elif i == 1 or i == 3:  # absolute and absolute extended waveforms
                axes.plot(x, y, color=color_magn, linewidth=width)
                axes.plot(x, y, color=color_imag, linewidth=width)
            elif i == 4:    # time waveform
                axes.step(x, y, where='post', color=color_real, linewidth=width)
                axes.step(x, y, where='post', color=color_imag, linewidth=width)
            elif i == 5:    # time waveform magnitude
                axes.step(x, y, where='post', color=color_magn, linewidth=width)
                axes.step(x, y, where='post', color=color_imag, linewidth=width)
            elif i == 6:    # time waveform phase-degrees
                axes.step(x, y, where='post', color=color_phas, linewidth=width)
                axes.step(x, y, where='post', color=color_imag, linewidth=width)
            elif i == 7:    # contour plot FIXME bjs figure out a real contour plot please
                axes.plot(x, y, color=color_real, linewidth=width)
                axes.plot(x, y, color=color_imag, linewidth=width)
            elif i == 8:    # grad_refocus
                axes.plot(x, y, color=color_real, linewidth=width)
                axes.plot(x, y, color=color_imag, linewidth=width)
                
            axes.axhline(0, color=self._prefs.zero_line_color, 
                            linestyle=self._prefs.zero_line_style, 
                            linewidth=width)  
                
        

    def format_plot(self, axes, plot, use_type, fsize):
        
        xlabel, ylabel, title = self.get_labels(plot, use_type)
        
        axes.set_xlabel(xlabel, size=fsize)
        axes.set_ylabel(ylabel, size=fsize)
        axes.set_title( title,  size=fsize)  
        self.set_ticklabel_size(axes, fsize)
        axes.grid(True)

        
    def set_ticklabel_size(self, axes, size):
        xlabels = axes.get_xticklabels()
        ylabels = axes.get_yticklabels()
        for xtext, ytext in zip(xlabels, ylabels):
            xtext.set_size(size)
            ytext.set_size(size)



    def get_labels(self, plot, use_type):
        labels = ['','','']
        if plot < 4 or plot == 8:
            labels = ['frequency [kHz]']
            if use_type == constants.UsageType.EXCITE:
                if self._prefs.data_type_real:
                    labels.append('Mx [normal]')
                elif self._prefs.data_type_real_imaginary:
                    labels.append('Mx/My [normal]')
            elif use_type == constants.UsageType.INVERSION:
                labels.append('Mz [normal]')
            elif use_type == constants.UsageType.SATURATION:
                labels.append('Mz [normal]')
            elif use_type == constants.UsageType.SPIN_ECHO:
                if self._prefs.data_type_real:
                    labels.append('+Mx [normal]')
                elif self._prefs.data_type_real_imaginary:
                    labels.append('+Mx/-My [normal]')
        
            if plot == 0:
                labels.append('Frequency Profile')
            elif plot == 1:
                labels.append('Absolute Frequency Profile')
            elif plot == 2:
                labels.append('Extended Profile')
            elif plot == 3:
                labels.append('Extended Absolute Profile')
            elif plot == 8:
                labels.append('Grad Refocused Profile')
 
        if plot == 4:
            labels = ['time [ms]','microTesla','Gradient Waveform']
        if plot == 5:
            labels = ['time [ms]','Magnitude [uT]','RF Pulse Waveform']
        if plot == 6:
            labels = ['time [ms]','Phase [degrees]','RF Pulse Waveform']

        return labels
 



    


