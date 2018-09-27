# -*- coding: utf-8 -*-
################################################################################
# This file is part of bookman.
#
# Copyright 2018 Richard Paul Baeck <richard.baeck@free-your-pc.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 
################################################################################

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from . import CONFIG_SINGLETON

class TagsDialog:
    def __init__(self, app):
        # Dialog
        self.dialog = None

        builder = Gtk.Builder()
        builder.set_translation_domain(app.appName)
        builder.add_from_file(CONFIG_SINGLETON.get_absolute_path(CONFIG_SINGLETON.get_config()["Builder"]["Files"]["TagsDialog"]))
        builder.connect_signals(self)
        
        self.init_dialog(builder)


    def init_dialog(self, builder : Gtk.Builder):
        self.dialog = builder.get_object('tags_dialog')

        cancel_button = builder.get_object('close_button')
        cancel_button.connect("clicked", self.on_close_clicked)


    def on_close_clicked(self):
        pass


    def run(self):
        response = self.dialog.run()
        self.dialog.destroy()
