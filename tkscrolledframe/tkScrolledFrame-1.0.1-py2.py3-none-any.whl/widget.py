#!/usr/bin/env python

"""Implementation of the scrollable frame widget."""

import os
import sys

try:
    # Python 3
    from tkinter import *
    from tkinter import Scrollbar as TkScrollbar
except (ImportError):
    # Python 2
    from Tkinter import *
    from Tkinter import Scrollbar as TkScrollbar

try:
    try:
        # Python 3
        from tkinter.ttk import Scrollbar as TtkScrollbar
    except (ImportError):
        # Python 2
        from ttk import Scrollbar as TtkScrollbar
    have_ttk = True
except (ImportError):
    have_ttk = False


__all__ = ["ScrolledFrame"]


class ScrolledFrame(Frame):
    """Scrollable Frame widget.

    Use display_widget() to set the interior widget. For example,
    to display a Label with the text "Hello, world!", you can say:

        sf = ScrolledFrame(self)
        sf.pack()
        sf.display_widget(Label, text="Hello, world!")

    The constructor accepts the usual Tkinter keyword arguments, plus
    a handful of its own:

      scrollbars (str; default: "both")
        Which scrollbars to provide.
        Must be one of "vertical", "horizontal," "both", or "neither".

      use_ttk (bool; default: False)
        Whether to use ttk widgets if available.
        The default is to use standard Tk widgets. This setting has
        no effect if ttk is not available on your system.
    """

    def __init__(self, master=None, **kw):
        """Return a new scrollable frame widget."""

        Frame.__init__(self, master)

        # Hold these names for the interior widget
        self._interior = None
        self._interior_id = None

        # Whether to fit the interior widget's width to the canvas
        self._fit_width = False

        # Which scrollbars to provide
        if "scrollbars" in kw:
            scrollbars = kw["scrollbars"]
            del kw["scrollbars"]

            if not scrollbars:
                scrollbars = self._default_scrollbars
            elif not scrollbars in self._valid_scrollbars:
                raise ValueError("scrollbars parameter must be one of "
                                 "'vertical', 'horizontal', 'both', or "
                                 "'neither'")
        else:
            scrollbars = self._default_scrollbars

        # Whether to use ttk widgets if available
        if have_ttk and "use_ttk" in kw and kw["use_ttk"]:
            Scrollbar = TtkScrollbar
            del kw["use_ttk"]
        else:
            Scrollbar = TkScrollbar

        # Default to a 1px sunken border
        if not "borderwidth" in kw:
            kw["borderwidth"] = 1
        if not "relief" in kw:
            kw["relief"] = "sunken"

        # Set up the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Canvas to hold the interior widget
        c = self._canvas = Canvas(self,
                                  borderwidth=0,
                                  takefocus=0)

        # Enable scrolling when the canvas has the focus
        self.bind_arrow_keys(c)
        self.bind_scroll_wheel(c)

        # Call _resize_interior() when the canvas widget is updated
        c.bind("<Configure>", self._resize_interior)

        # Scrollbars
        xs = self._x_scrollbar = Scrollbar(self,
                                           orient="horizontal",
                                           command=c.xview)
        ys = self._y_scrollbar = Scrollbar(self,
                                           orient="vertical",
                                           command=c.yview)
        c.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)

        # Lay out our widgets
        c.grid(row=0, column=0, sticky="nsew")
        if scrollbars == "vertical" or scrollbars == "both":
            ys.grid(row=0, column=1, sticky="ns")
        if scrollbars == "horizontal" or scrollbars == "both":
            xs.grid(row=1, column=0, sticky="we")

        # Forward these to the canvas widget
        self.bind = c.bind
        self.focus_set = c.focus_set
        self.unbind = c.unbind
        self.xview = c.xview
        self.xview_moveto = c.xview_moveto
        self.yview = c.yview
        self.yview_moveto = c.yview_moveto

        # Pass our remaining configuration options to Tk
        self.configure(**kw)

    def __setitem__(self, key, value):
        """Configure resources of a widget."""

        if key in self._canvas_keys:
            # Forward these to the canvas widget
            self._canvas.configure(**{key: value})

        else:
            # Handle everything else normally
            Frame.configure(self, **{key: value})

    # ------------------------------------------------------------------------

    def bind_arrow_keys(self, widget):
        """Bind the specified widget's arrow key events to the canvas."""

        widget.bind("<Up>",
                    lambda event: self._canvas.yview_scroll(-1, "units"))

        widget.bind("<Down>",
                    lambda event: self._canvas.yview_scroll(1, "units"))

        widget.bind("<Left>",
                    lambda event: self._canvas.xview_scroll(-1, "units"))

        widget.bind("<Right>",
                    lambda event: self._canvas.xview_scroll(1, "units"))

    def bind_scroll_wheel(self, widget):
        """Bind the specified widget's mouse scroll event to the canvas."""

        widget.bind("<MouseWheel>", self._scroll_canvas)
        widget.bind("<Button-4>", self._scroll_canvas)
        widget.bind("<Button-5>", self._scroll_canvas)

    def cget(self, key):
        """Return the resource value for a KEY given as string."""

        if key in self._canvas_keys:
            return self._canvas.cget(key)

        else:
            return Frame.cget(self, key)

    # Also override this alias for cget()
    __getitem__ = cget

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget."""

        # This is overridden so we can use our custom __setitem__()
        # to pass certain options directly to the canvas.
        if cnf:
            for key in cnf:
                self[key] = cnf[key]

        for key in kw:
            self[key] = kw[key]

    # Also override this alias for configure()
    config = configure

    def display_widget(self, widget_class, fit_width=False, **kw):
        """Create and display a new widget.

        If fit_width == True, the interior widget will be stretched as
        needed to fit the width of the frame.

        Keyword arguments are passed to the widget_class constructor.

        Returns the new widget.
        """

        # Blank the canvas
        self.erase()

        # Set width fitting
        self._fit_width = fit_width

        # Set the new interior widget
        self._interior = widget_class(self._canvas, **kw)

        # Add the interior widget to the canvas, and save its widget ID
        # for use in _resize_interior()
        self._interior_id = self._canvas.create_window(0, 0,
                                                       anchor="nw",
                                                       window=self._interior)

        # Call _update_scroll_region() when the interior widget is resized
        self._interior.bind("<Configure>", self._update_scroll_region)

        # Fit the interior widget to the canvas if requested
        # We don't need to check fit_width here since _resize_interior()
        # already does.
        self._resize_interior()

        # Scroll to the top-left corner of the canvas
        self.scroll_to_top()

        return self._interior

    def erase(self):
        """Erase the displayed widget."""

        # Clear the canvas
        self._canvas.delete("all")

        # Delete the interior widget
        del self._interior
        del self._interior_id

        # Save these names
        self._interior = None
        self._interior_id = None

        # Reset width fitting
        self._fit_width = False

    def scroll_to_top(self):
        """Scroll to the top-left corner of the canvas."""

        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)

    # ------------------------------------------------------------------------

    def _resize_interior(self, event=None):
        """Resize the interior widget to fit the canvas."""

        if self._fit_width and self._interior_id:
            # The current width of the canvas
            canvas_width = self._canvas.winfo_width()

            # The interior widget's requested width
            requested_width = self._interior.winfo_reqwidth()

            if requested_width != canvas_width:
                # Resize the interior widget
                new_width = max(canvas_width, requested_width)
                self._canvas.itemconfigure(self._interior_id, width=new_width)

    def _scroll_canvas(self, event):
        """Scroll the canvas."""

        c = self._canvas

        if sys.platform.startswith("darwin"):
            # macOS
            c.yview_scroll(-1 * event.delta, "units")

        elif event.num == 4:
            # Unix - scroll up
            c.yview_scroll(-1, "units")

        elif event.num == 5:
            # Unix - scroll down
            c.yview_scroll(1, "units")

        else:
            # Windows
            c.yview_scroll(-1 * (event.delta // 120), "units")

    def _update_scroll_region(self, event):
        """Update the scroll region when the interior widget is resized."""

        # The interior widget's requested width and height
        req_width = self._interior.winfo_reqwidth()
        req_height = self._interior.winfo_reqheight()

        # Set the scroll region to fit the interior widget
        self._canvas.configure(scrollregion=(0, 0, req_width, req_height))

    # ------------------------------------------------------------------------

    # Keys for configure() to forward to the canvas widget
    _canvas_keys = "width", "height", "takefocus"

    # Scrollbar-related configuration
    _default_scrollbars = "both"
    _valid_scrollbars = "vertical", "horizontal", "both", "neither"
