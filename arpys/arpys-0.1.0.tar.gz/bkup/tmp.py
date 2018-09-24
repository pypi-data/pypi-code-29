#!/usr/bin/python
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib import rcParams
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename

from dataloaders import *

# +------------+ #
# | Parameters | # =============================================================
# +------------+ #

# Backgroundcolor of plot
BGCOLOR = "black"

# Length of sliders
SLIDER_LENGTH = 200

# Number of entries allowed in colormap sliders (starts from 0)
CM_SLIDER_RESOLUTION = 99

# Data loader objects
DATA_LOADERS = { 'PSI' : Dataloader_PSI() }

# Size of the plot in inches (includes labels and title etc)
SIZE =  6.5
FIGSIZE = (SIZE, SIZE)

# Set the font size for plot labels, titles, etc.
FONTSIZE = 10
rcParams.update({'font.size': FONTSIZE})

# The status of the GUI when nothing else is going on
DEFAULT_STATUS = 'Idle'

# Initialize some default data
STARTUP_DATA = np.array([[[k*(i+j) +(1-k)*(i-j) for k in range(2)] for j in 
                          range(100)] for i in range(90)])


# +------------+ #
# | GUI Object | # =============================================================
# +------------+ #

class Gui :
    """
    A tkinter GUI to quickly visualize 2D and 3D data. Should be built in a 
    modular fashion such that any data reader can be 'plugged in'.
    """
    data = STARTUP_DATA
    data_loaders = DATA_LOADERS

    def __init__(self, master, filename=None) :
        """ Define all visible elements and link their to their logic. """
        # Create the main container/window
        frame = tk.Frame(master)

        # Define some elements
        self._set_up_load_button(master)
        self._set_up_plots(master)
        self._set_up_colormap_sliders(master)
        self._set_up_z_slider(master)
        self._set_up_status_label(master)

        # Align all elements
        self._align()

        # Load the given file
        if filename :
            self.filepath.set(filename)
            self.load_data()

    def _align(self) :
        """ Use the grid() layout manager to align the elements of the GUI. """
        # The plot takes up the space of N_PLOT widgets
        N_PLOT = 8
        N_PATH_FIELD = int(N_PLOT/2)

        # 'Load file' elements
        LOADROW = 0
        self.browse_button.grid(row=LOADROW, column=0, sticky='ew')
        self.load_button.grid(row=LOADROW, column=1, sticky='ew')
        self.path_field.grid(row=LOADROW+1, column=0, columnspan=N_PATH_FIELD, 
                             sticky='ew') 
        # Plot & colormap sliders
        PLOTROW = LOADROW + 2
        PLOTCOLUMN = 1
        self.canvas.get_tk_widget().grid(row=PLOTROW, column=PLOTCOLUMN, 
                                         columnspan=N_PLOT)
        self.cm_min_slider.grid(row=PLOTROW, column=N_PLOT + PLOTCOLUMN + 1)
        self.cm_max_slider.grid(row=PLOTROW, column=N_PLOT + PLOTCOLUMN + 2)

        # z slider
        self.z_slider.grid(row=PLOTROW, column=0)

        # Put the status label at the very bottom left
        STATUSROW = PLOTROW + 1
        self.status_label.grid(row=STATUSROW, column=0, sticky='ew')

    def _set_up_load_button(self, master) :
        """ Add a button which opens a filebrowser to choose the file to load
        and a textbox (Entry widget) where the filepath can be changed.
        """
        # Define the Browse button
        self.browse_button = tk.Button(master, text='Browse',
                                     command=self.browse)

        # and the Load button
        self.load_button = tk.Button(master, text='Load',
                                     command=self.load_data)
        
        # and the entry field which holds the path to the current file
        self.filepath = tk.StringVar()
        self.path_field = tk.Entry(master, textvariable=self.filepath)

        # Finally, also add inc and decrement buttons
        self.increment_button = tk.Button(master, text='>',
                                          command=lambda : self.increment('+')) 
        self.decrement_button = tk.Button(master, text='<',
                                          command=lambda : self.increment('-')) 

    def _set_up_plots(self, master) :
        """ Take car of all the matplotlib stuff for the plot. """
        fig = Figure(figsize=FIGSIZE)
        fig.patch.set_alpha(0)
        ax_cut1 = fig.add_subplot(221)
        ax_cut2 = fig.add_subplot(224)
        ax_map = fig.add_subplot(223)
        ax_energy = fig.add_subplot(222)
        self.axes = {'cut1': ax_cut1,
                     'cut2': ax_cut2,
                     'map': ax_map,
                     'energy': ax_energy}
        for ax in self.axes.values() :
            ax.set_facecolor(BGCOLOR)
        self.canvas = FigureCanvasTkAgg(fig, master=master)
        self.canvas.show()

    def _set_up_colormap_sliders(self, master) :
        """ Add the colormap adjust slider, set its starting position and add 
        its binding such that it only triggers upon release.
        Also, couple them to the variables vmin/max_index.
        """
        self.vmin_index = tk.IntVar()
        self.vmax_index = tk.IntVar()
        cm_slider_kwargs = { 'showvalue' : 0,
                             'to' : CM_SLIDER_RESOLUTION, 
                             'length':SLIDER_LENGTH }
        self.cm_min_slider = tk.Scale(master, variable=self.vmin_index,
                                      label='Min', **cm_slider_kwargs)
        self.cm_min_slider.set(CM_SLIDER_RESOLUTION)
        self.cm_min_slider.bind('<ButtonRelease-1>', self.plot_data)

        self.cm_max_slider = tk.Scale(master, variable=self.vmax_index,
                                      label='Max', **cm_slider_kwargs)
        self.cm_max_slider.set(0)
        self.cm_max_slider.bind('<ButtonRelease-1>', self.plot_data)

    def _set_up_z_slider(self, master) :
        """ Create a Slider which allows to select the z value of the data.
        This value is stored in the DoubleVar self.z """
        self.z = tk.IntVar()
        self.z.set(0)
        self.zmax = tk.IntVar()
        self.zmax.set(1)
        self.z_slider = tk.Scale(master, variable=self.z, label='z', 
                                 to=self.zmax.get(), showvalue=1, 
                                 length=SLIDER_LENGTH) 
        self.z_slider.bind('<ButtonRelease-1>', self.plot_data)

    def _set_up_status_label(self, master) :
        """ Create a label which can hold informative text about the current
        state of the GUI or success/failure of certain operations. This text 
        is held in the StringVar self.status.
        """
        self.status = tk.StringVar()
        # Initialize the variable with the default status
        self.update_status()
        self.status_label = tk.Label(textvariable=self.status, justify=tk.LEFT,
                                    anchor='w')

    def increment(plusminus) :
        pass

    def update_status(self, status=DEFAULT_STATUS) :
        """ Update the status StringVar with the current time and the given
        status argument. """
        now = datetime.now().strftime('%H:%M:%S')
        new_status = '[{}] {}'.format(now, status)
        self.status.set(new_status)

    def browse(self) :
        """ Open a filebrowser dialog and put the selected file into  
        self.path_field. """
        # If the file entry field already contains a path to a file use it
        # as the default file for the browser
        old_filepath = self.filepath.get() 
        if old_filepath :
            default_file = old_filepath
        else :
            default_file = None

        # Open a browser dialog
        new_filepath = askopenfilename(initialfile=default_file)
        self.filepath.set(new_filepath)

    def load_data(self) :
        """ Load data from the file currently selected by self.filepath. """
        # At the moment, there is only one data loader
        data_loader = 'PSI'

        # Show the user that something is happening
        self.update_status('Loading {} data...'.format(data_loader))

        # Try to load the data with the given dataloader
        try :
            self.data, self.xlabel, self.ylabel, self.zlabel = \
            self.data_loaders[data_loader].load_data(self.filepath.get())
            self.update_status('Loaded {} data.'.format(data_loader))
        except Exception as e :
            print(e)
            self.update_status('Failed to load {} data.'.format(data_loader))
            # Leave the function
            return 1

        # Update the max z value
        self.zmax.set( len(self.data[0,0]) - 1)
        self.z_slider.config(to=self.zmax.get())

        self.plot_data()

    def plot_data(self, event=None) :
        """ Update the colormap range and (re)plot the data. """
        # Note: vmin_index goes from 100 to 0 and vice versa for vmax_index.
        # This is to turn the sliders upside down.
        # Crude method to avoid unreasonable colormap settings
        if self.vmin_index.get() < self.vmax_index.get() :
            self.vmin_index.set(CM_SLIDER_RESOLUTION)

        # Split the data value range into equal parts
        drange = np.linspace(self.data.min(), self.data.max(), 
                             CM_SLIDER_RESOLUTION + 1)

        # Get the appropriate vmin and vmax values from the data
        vmin = drange[CM_SLIDER_RESOLUTION - self.vmin_index.get()]
        vmax = drange[CM_SLIDER_RESOLUTION - self.vmax_index.get()]

        # (Re)plot the heatmap 
        for ax in self.axes.values() :
            ax.clear()
        self.axes['map'].pcolormesh(self.data[:,:,self.z.get()], vmin=vmin, 
                                     vmax=vmax)
        self.canvas.draw()

def start_gui(filename=None) :
    """ Initialize the Tk object, give it a title, attach the Gui (App) to it 
    and start the mainloop. 
    """
    root = tk.Tk()
    root.title('Data visualizer')
    gui = Gui(root, filename=filename)
    gui.plot_data()
    root.mainloop()


# +------+ #
# | Main | # ===================================================================
# +------+ #

if __name__ == '__main__' :
    start_gui()
