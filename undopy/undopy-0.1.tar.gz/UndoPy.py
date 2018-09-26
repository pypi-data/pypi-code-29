def deepw(element, callbacks=[], undocallbacks=[], wrap=None, hoproot=False):
    """ Wrap nested list and dict. """
    if wrap:
        result = wrap(element)
        if result is not None:
            return result
    if type(element) == list:
        inner = [deepw(subelem, callbacks, undocallbacks, wrap)
                 for subelem in element]
        if hoproot:
            return inner
        return undo_list(inner, callbacks=callbacks, undocallbacks=undocallbacks)
    elif type(element) == dict:
        inner = dict((key, deepw(value, callbacks, undocallbacks, wrap))
                     for key, value in element.items())
        if hoproot:
            return inner
        return undo_dict(inner, callbacks=callbacks, undocallbacks=undocallbacks)
    else:
        return element

class UndoLog(object):
    def __init__(self):
        self.root = self.rootundo = watched_tree("undo root")
        self.observed = []
        self.index = -1

    def add(self, element):
        """ Add element to observe. """
        self.observed.append(element)
        element.undocallbacks.append(self.log)

    def log(self, element, undoelem, redoelem):
        if element.skiplog > 0:
            return
        self.void_redo()
        self.rootundo.append(watched_tree(name=(element, undoelem, redoelem)))

    def void_redo(self):
        if self.rootundo == self.root and self.index != -1:
            del self.root[self.index+1:]
            self.index = -1

    def start_group(self, label, brand_new=False):
        if brand_new and self.rootundo.name == label:
            return False
        self.void_redo()
        self.rootundo.append(watched_tree(label))
        self.index = -1
        self.rootundo = self.rootundo[-1]
        return True

    def end_group(self, label, skip_unused=False, delete_void=False):
        if label and self.rootundo.name != label:
            if skip_unused: return
            raise Exception("Ending group %s but the current group is %s!" % \
                            (label, self.rootundo.name))
        if not self.rootundo.parent:
            raise Exception("Attempting to end root group!")
        self.rootundo = self.rootundo.parent
        if delete_void and len(self.rootundo) == 0:
            self.rootundo.pop()
        self.index = -1

    def undo(self, vertex=None):
        if vertex is None:
            vertex = self.root[self.index]
            self.index -= 1
        if type(vertex.name) == str:
            for child in reversed(vertex):
                self.undo(child)
        else:
            self.unredo_event(vertex.name[0], vertex.name[1])

    def redo(self, vertex=None):
        if vertex is None:
            vertex = self.root[self.index + 1]
            self.index += 1
        if type(vertex.name) == str:
            for child in vertex:
                self.redo(child)
        else:
            self.unredo_event(vertex.name[0], vertex.name[2])

    def unredo_event(self, element, item):
        element.skiplog += 1
        getattr(element, item[0])(*item[1:])
        element.skiplog -= 1

    def pprint(self, vertex=None):
        for line in self.pprint_string(vertex):
            print(line)

    def pprint_string(self, vertex=None, indent=0):
        if vertex is None:
            vertex = self.root
        if type(vertex.name) != str:
            yield "%s%s" % (indent *" ", vertex.name[2][0])
            return
        name = vertex.name if vertex.name else ""
        yield "%s%s" % (indent*" ", name)
        for child in vertex:
            for line in self.pprint_string(child, indent + 2):
                yield line

class undo_list(list):
    """
    undo_list that calls functions from self.undocallbacks
    the undo,redo pair is used whenever an operation is applied to a list.
    ehile self.callbacks is called redo

    self.replace is not in python's list function itself, but is included due for convenient purposes
    """
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args)
        self.callbacks = kwargs.get("callbacks", [])
        self.undocallbacks = kwargs.get("undocallbacks", [])
        self.skiplog = 0

    def callback(self, undo, redo):
        for callback in self.callbacks:
            callback(self, *redo)
        for callback in self.undocallbacks:
            callback(self, undo, redo)

    def __deepcopy__(self, memo):
        return undo_list(self)

    def __setitem__(self, key, value):
        try:
            prevvalue = self.__getitem__(key)
        except KeyError:
            list.__setitem__(self, key, value)
            self.callback(("__delitem__", key), ("__setitem__", key, value))
        else:
            list.__setitem__(self, key, value)
            self.callback(("__setitem__", key, prevvalue),
                          ("__setitem__", key, value))

    def __delitem__(self, key):
        prevvalue = list.__getitem__(self, key)
        list.__delitem__(self, key)
        self.callback(("__setitem__", key, prevvalue), ("__delitem__", key))

    def __setslice__(self, i, j, seq):
        prevvalue = list.__getslice__(self, i, j)
        self.callback(("__setslice__", i, j, prevvalue),
                      ("__setslice__", i, j, seq))
        list.__setslice__(self, i, j, seq)

    def __delslice__(self, i, j):
        prevvalue = list.__getitem__(self, slice(i, j))
        list.__delslice__(self, i, j)
        self.callback(("__setslice__", i, i, prevvalue), ("__delslice__", i, j))

    def append(self, val):
        list.append(self, val)
        self.callback(("pop",), ("append", val))

    def pop(self, index=-1):
        prevvalue = list.pop(self, index)
        self.callback(("append", prevvalue), ("pop", index))
        return prevvalue

    def extend(self, newval):
        oldlen = len(self)
        list.extend(self, newval)
        self.callback(("__delslice__", oldlen, len(self)),
                      ("extend", self[oldlen:]))

    def insert(self, i, elem):
        list.insert(self, i, elem)
        self.callback(("pop", i), ("insert", i, elem))

    def remove(self, elem):
        if elem in self:
            oldindex = self.index(elem)
        list.remove(self, elem)
        self.callback(("insert", oldindex, elem), ("remove", elem))

    def reverse(self):
        list.reverse(self)
        self.callback(("reverse",), ("reverse",))

    def sort(self, *args, **kwargs):
        prevlist = self[:]
        list.sort(self, *args, **kwargs)
        self.callback(("replace", prevlist), ("replace", self[:]))

    def replace(self, nextlist):
        prevlist = self[:]
        self.skiplog += 1
        del self[:]
        try:
            self.extend(nextlist)
        except:
            self.replace(prevlist) # check for inf loops
            self.skiplog -= 1
            raise
        self.skiplog -= 1
        self.callback(("replace", prevlist), ("replace", nextlist))

class undo_dict(dict):
    def __init__(self, *args, **kwargs):
        self.callbacks = kwargs.pop("callbacks", [])
        self.undocallbacks = kwargs.pop("undocallbacks", [])
        dict.__init__(self, *args, **kwargs)
        self.skiplog = 0

    def callback(self, undo, redo):
        for callback in self.callbacks:
            callback(self, *redo)
        for callback in self.undocallbacks:
            callback(self, undo, redo)

    def __deepcopy__(self, memo):
        return undo_dict(self)

    def __setitem__(self, key, val):
        try:
            prevvalue = self.__getitem__(key)
        except KeyError:
            dict.__setitem__(self, key, val)
            self.callback(("__delitem__", key), ("__setitem__", key, val))
        else:
            dict.__setitem__(self, key, val)
            self.callback(("__setitem__", key, prevvalue),
                          ("__setitem__", key, val))

    def __delitem__(self, key):
        prevvalue = self[key]
        dict.__delitem__(self, key)
        self.callback(("__setitem__", key, prevvalue), ("__delitem__", key))

    def clear(self):
        prevvalue = self.copy()
        dict.clear(self)
        self.callback(("update", prevvalue), ("clear",))

    def update(self, update_dict):
        prevvalue = self.copy()
        dict.update(self, update_dict)
        self.callback(("replace", prevvalue), ("update", update_dict))

    def setdefault(self, key, val=None):
        if key not in self:
            dict.setdefault(self, key, val)
            self.callback(("__delitem__", key), ("setdefault", key, val))
            return val
        else:
            return self[key]

    def pop(self, key, default=None):
        if key in self:
            val = dict.pop(self, key, default)
            self.callback(("__setitem__", key, val), ("pop", key, default))
            return val
        else:
            return default

    def popitem(self):
        key, val = dict.popitem(self)
        self.callback(("__setitem__", key, val), ("popitem",))
        return key, val

    def replace(self, nextdict):
        prevvalue = self.copy()
        self.skiplog += 1
        self.clear()
        try:
            self.update(nextdict)
        except:
            self.replace(prevvalue)
            self.skiplog -= 1
            raise
        self.skiplog -= 1
        self.callback(("replace", nextdict), ("replace", prevvalue))

class watched_tree(list):
    """Ordered list of children with parent pointers for consistency checking
    Should contain one element

    Could be used for modelling an xml or JSON document"""
    def __init__(self, name=None, val=[], parent=None,
                 callbacks=None, undocallbacks=None):
        list.__init__(self, val)
        self.parent = parent
        self.name = name
        self.callbacks = callbacks if callbacks else []
        self.undocallbacks = undocallbacks if undocallbacks else []
        self.skiplog = 0

    def callback(self, undo, redo, source=None):
        # pass self here
        if source is None:
            source = self
        for callback in self.callbacks:
            callback(source, *redo)
        for callback in self.undocallbacks:
            callback(source, undo, redo)
        if self.parent:
            self.parent.callback(undo, redo, source)

    def _reparent(self, nextparent, remove=False):
        if remove and self.parent:
            self.parent.remove(self, reparent=False)
        self.parent = nextparent

    def __setitem__(self, key, val):
        try:
            prevvalue = self.__getitem__(key)
        except KeyError:
            val._reparent(self, True)
            list.__setitem__(self, key, val)
            # check reparent undo
            self.callback(("__delitem__", key), ("__setitem__", key, val))
        else:
            prevvalue._reparent(None)
            val._reparent(self, True)
            list.__setitem__(self, key, val)
            self.callback(("__setitem__", key, prevvalue),
                          ("__setitem__", key, val))

    def __delitem__(self, key):
        prevvalue = list.__getitem__(self, key)
        list.__delitem__(self, key)
        prevvalue._reparent(None)
        # undo on the reparent needs checked here
        # __setitem__ actually handles it for now
        self.callback(("__setitem__", key, prevvalue), ("__delitem__", key))

    def __setslice__(self, i, j, seq):
        prevvalue = list.__getslice__(self, i, j)
        self.callback(("__setslice__", i, j, prevvalue),
                      ("__setslice__", i, j, seq))
        for child in prevvalue:
            child._reparent(None, True)
        for child in seq:
            child._reparent(self, True)
        list.__setslice__(self, i, j, seq)

    def __delslice__(self, i, j):
        prevvalue = list.__getitem__(self, slice(i, j))
        for child in prevvalue:
            child._reparent(None, True)
        list.__delslice__(self, i, j)
        self.callback(("__setslice__", i, i, prevvalue), ("__delslice__", i, j))

    def __eq__(self, other):
        return self is other

    def append(self, val):
        list.append(self, val)
        val._reparent(self, True)
        self.callback(("pop",), ("append", val))

    def pop(self, index=-1):
        prevvalue = list.pop(self, index)
        prevvalue._reparent(None)
        self.callback(("append", prevvalue), ("pop", index))
        return prevvalue

    def extend(self, nextvalue):
        prevlen = len(self)
        list.extend(self, nextvalue)
        for value in nextvalue:
            value._reparent(self, True)
        self.callback(("__delslice__", prevlen, len(self)),
                      ("extend", self[prevlen:]))

    def insert(self, i, elem):
        elem._reparent(self, True)
        list.insert(self, i, elem)
        self.callback(("pop", i), ("insert", i, elem))

    def remove(self, elem, reparent=True):
        if elem in self:
            previndex = self.index(elem)
        list.remove(self, elem)
        if reparent:
            elem._reparent(None)
        self.callback(("insert", previndex, elem), ("remove", elem))

    def reverse(self):
        list.reverse(self)
        self.callback(("reverse",), ("reverse",))

    def sort(self, *args, **kwargs):
        prevlist = self[:]
        list.sort(self, *args, **kwargs)
        self.callback(("replace", prevlist), ("replace", self[:]))

    def replace(self, nextlist):
        prevlist = self[:]
        self.skiplog += 1
        del self[:]
        try:
            self.extend(nextlist)
        except:
            self.replace(prevlist) # check for inf loops
            self.skiplog -= 1
            raise
        self.skiplog -= 1
        self.callback(("replace", prevlist), ("replace", nextlist))

 #Helper func
    def maximal(self, condition):
        """ Return maximal non chain among desc that satisfy conditions"""
        for child in self:
            if condition(child):
                yield child
            else:
                for gc in child.maximal(condition):
                    yield gc

    @property
    def children(self):
        for child in self:
            for gc in child.children:
                yield gc
            yield child

# debugging for callbacks
def printargs(*args):
    print(args)

if __name__ == '__main__':
    # test cases
    t = UndoLog()
    d = undo_dict({1: "VU", 2: "UvA"})
    l = undo_list([3, 3, 3])
    t.add(d)
    t.add(l)
    l.append(1)
    print(l)
    t.undo()
    print(l)
    t.redo()
    print(l)
    d[3] = "CWI"
    print(d)
    t.undo()
    print(d)
    t.redo()
    print(d)
    t.start_group("foo")
    d[53] = "person"
    del d[1]
    t.end_group("foo")
    t.start_group("foo")
    d["bar"] = "baz"
    t.end_group("foo")
    deep = {"cdf": "abc", "alist": [4, 5, 6]}
    obs_deep = deepw(deep, undocallbacks=[t.log])
    t.observed.append(obs_deep)
    obs_deep["test"] = "1"
    obs_deep["alist"].append(4)
