from . import bridge

import pystache
import os

from ..util import memoize, shelve_it

from .components import CoreComponent
from .assets import BigJSPackage, JSComponent

import shlex
import subprocess

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def babel_compile(data, fname='???'):
    cmd = "%s --presets @babel/preset-react -f '%s'" % (BABEL_BIN, fname)

    p = subprocess.Popen(shlex.split(cmd), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout,stderr = p.communicate(data.encode())

    return stdout.decode()

def dukpy_compile(data, fname='???'):
    # try dukpy as a resort, too, but its slower
    import dukpy
    return dukpy.jsx_compile(data)

BABEL_BIN = os.path.expanduser("~/node_modules/.bin/babel")
JSX_COMPILE = babel_compile
if not os.path.exists(BABEL_BIN):
    print("*** COULDNT FIND BABEL BIN, REACT COMPONENTS WONT COMPILE")
    print("*** Try setting the babel bin with reactcomponent.set_bin('path/to/babel')")

    JSX_COMPILE = dukpy_compile


class ReactLoader(CoreComponent, JSComponent):
    WRAP_COMPONENT = False

class ReactComponent(bridge.ClientBridge):
    @classmethod
    def set_jsx_compiler(cls, fn):
        global JSX_COMPILE
        JSX_COMPILE = fn

    @classmethod
    def get_js(cls):
        with open(cls.get_file_for_ext("jsx")) as f:
            js = cls.js_transform(f.read())
            return js

    @classmethod
    @shelve_it("jsx.cache")
    def js_transform(cls, js):
        return JSX_COMPILE(js)

    @classmethod
    def find_file(cls, fname, basedir):
        cls_dir = cls.BASE_DIR

        for ext in ["js", "jsx"]:
            fname = fname.strip("'\"")
            if fname[0] == ".":
                jsp = "%s.%s" % (os.path.join(cls_dir, basedir, fname), ext)
            else:
                jsp = "%s.%s" % (os.path.join(cls_dir, fname), ext)

            if os.path.exists(jsp):
                return jsp

        return None

    def __json__(self):
        self.__marshal__()
        return { "_R" : self.__html_id__() }

    def set_ref(self, name):
        # TODO: validate there is only one of each named ref on the page
        self.__ref__ = name
        return self

    def __activate__(self):
        self.client.update(self.context)

        super(ReactComponent, self).__activate__()

        # we override the activation string with our react activation string
        t = """
            $C("ReactLoader", function(m) {
                m.exports.activate_react_component("{{__html_id__}}", "{{ __template_name__ }}", {{ &__context__ }}, {{ __display_immediately__ }}, "{{ __ref__ }}" )
            });
        """.strip()

        self.__activate_str__ = pystache.render(t, self)

from . import components
components.mark_virtual(ReactComponent, ReactLoader)
