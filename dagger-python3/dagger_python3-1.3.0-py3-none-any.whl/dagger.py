# Dagger is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Dagger is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Dagger.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2012 Remik Ziemlinski
# Copyright 2018 east301

import datetime
import hashlib
import os
from collections import deque

VERSION = "1.3.0"


###############################################################
class idict(object):
    """Stores append index and O(1) lookup of index using key."""

    def __init__(self):
        self.dict = {}
        self.list = []
        self.ctr = 0

    def append(self, item):
        """Add unique item, store its index and return index."""
        if item in self.dict:
            return self.dict[item]

        self.dict[item] = self.ctr
        self.list.append(item)
        self.ctr += 1
        return self.ctr

    def __contains__(self, v):
        return v in self.dict

    def index(self, item):
        """Return index for item. None if not in container."""
        return self.dict.get(item)

    def __iter__(self):
        return self.list.__iter__()

    def __len__(self):
        return len(self.list)


###############################################################
class ldict_node(object):
    """Node for ldict that wraps data and holds double-links."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class ldict(object):
    """
    Hybrid linked-list/dict container for O(1) removal of append-sorted data keys.
    Benchmark shows that it is much faster than plain list for large arrays
    (see bench/bench_ldict.py).
    """

    def __init__(self, lst=[]):
        """Create for existing list."""
        self.head = None
        self.tail = None
        self.dict = {}

        for item in lst:
            self.append(item)

    def append(self, item):
        if item in self.dict:
            return

        if not isinstance(item, ldict_node):
            item = ldict_node(item)

        if not self.head:
            self.head = item
            self.tail = item
        else:
            item.prev = self.tail
            self.tail.next = item
            self.tail = item

        self.dict[item.data] = item

    def get(self, data):
        """Returns ldict_node for data item."""
        return self.dict.get(data)

    def remove(self, item):
        if not isinstance(item, ldict_node):
            item = self.get(item)
        if not item:
            return

        if item.data in self.dict:
            self.dict.pop(item.data)
        if item.prev:
            item.prev.next = item.next
        if item.next:
            item.next.prev = item.prev
        if self.tail == item:
            self.tail = item.prev
        if self.head == item:
            self.head = item.next


###############################################################
class hashdb(object):
    """Loads, queries, computes and exports "file,hash" per line."""

    def __init__(self, fn=''):
        self.filename = fn
        self.db = {}

    def get(self, fn):
        """Get hash for given filename in db."""
        return self.db.get(fn)

    def export(self):
        """Write out db to text file with file names and hashes."""
        with open(self.filename, 'w') as f:
            for k in self.db:
                f.write(f'{k},{self.db[k]}\n')

    def load(self):
        """Loads db text file."""
        try:
            with open(self.filename) as f:
                self.db = dict([x.split(',') for x in f.read().split()])
        except FileNotFoundError:
            pass

    @staticmethod
    def md5(fn):
        """Return md5 checksum for file named 'fn' or None if error."""
        try:
            m = hashlib.md5()
            with open(fn, 'rb') as fh:
                for chunk in iter(lambda: fh.read(8192), b''):
                    m.update(chunk)

            return m.hexdigest()

        except FileNotFoundError:
            return None

    def set(self, fn, hash):
        """Put hash for file into table."""
        self.db[fn] = hash

    def update(self, fn):
        """Compute hash for file and update db entry."""
        hash = hashdb.md5(fn)
        self.set(fn, hash)


###############################################################
class hashdb_sqlite(hashdb):
    """Uses a sqlite database. Can be used inmemory after loading file."""

    def __init__(self, fn='', memory=False):
        self.filename = fn
        # Connection to file.
        self.db = None
        # Run db in memory?
        self.memory = memory

    def export(self):
        """Write out db to file with file names and hashes."""
        import binascii
        import shutil

        if self.memory:
            # Backup current file in case of write error.
            bak = f'{self.filename}.{binascii.b2a_hex(os.urandom(3))}.bak'
            try:
                shutil.copyfile(self.filename, bak)
                bakok = True
            except IOError:
                bakok = False

            def mem2file(outputfn):
                import sqlite3
                new_db = sqlite3.connect(outputfn)
                old_db = self.db
                sql = "".join(line for line in old_db.iterdump())
                new_db.executescript(sql)
                old_db.close()
                return new_db

            exportok = False
            try:
                self.db = mem2file(self.filename)
                exportok = True
            except:     # NOQA
                print(
                    f'Error: Converting in-memory hash db to file "{self.filename}" failed. '
                    f'Will try exporting to "hashdump.sqlite". '
                    f'Backup of original hash db was made to "{bak}".'
                )
                self.db = mem2file("hashdump.sqlite")

            if exportok and bakok:
                try:
                    os.remove(bak)
                except IOError:
                    pass

        if self.db:
            self.db.close()

    def get(self, fn):
        """Get hash for given filename in db."""
        if not self.db:
            return ''

        c = self.db.cursor()
        c.execute('SELECT hash FROM db WHERE file=?', (fn, ))
        h = c.fetchone()
        return h or None

    def load(self):
        """
        Loads sqlite db file if it exists and optionally into memory.
        If none exists, a new db is created.
        """
        import sqlite3

        # Create schema if file doesn't exist yet.
        exists = os.path.exists(self.filename)

        if self.memory:  # Load into memory.
            self.db = sqlite3.connect(':memory:')
            if exists:
                old_db = sqlite3.connect(self.filename)
                sql = "".join(line for line in old_db.iterdump())
                # Dump old database in the new one.
                self.db.executescript(sql)
                old_db.close()
        else:
            self.db = sqlite3.connect(self.filename)

        if not exists:
            c = self.db.cursor()
            c.execute(
                "CREATE TABLE db (file text, hash text, PRIMARY KEY (file))"
            )
            self.db.commit()

    def set(self, fn, hash):
        """Put hash for file into table."""
        if not self.db:
            return

        c = self.db.cursor()
        c.execute("INSERT OR REPLACE INTO db VALUES (?, ?)", (fn, hash))
        self.db.commit()


###############################################################
def time2strings(t):
    """Convert time (from os.path.getmtime) to date and time strings."""
    tstr = str(datetime.datetime.fromtimestamp(t))
    return tstr.split(' ')


###############################################################
class node(object):
    """
    File node for dependecy graph.
    """

    def __init__(self, name):
        self.hash = None
        self.name = name
        # Children. Deque allows O(1) popleft.
        self.nodes = deque()
        # None means no parent.
        # [] means was added as child by another.
        # dagger will populate lists of node references during tree evaluation.
        # Multiple paths from roots may exist. List of lists.
        self.paths = None
        # Lookup table for quick check if another node is in a path.
        self.paths_set = set()
        # If false, will get file attributes.
        self.phony = 0
        # None means TBD by graph walk.
        # Otherwise 0 is uptodate, 1 means needs refresh.
        # If file doesn't exist, then update() will set stale to true.
        self.stale = None
        # Missing files will always by older relative to real files.
        self.time = 0

    def add(self, *nodes):
        """Add one or more nodes as children."""
        self.nodes.extend(nodes)
        # Reset paths.
        for f in nodes:
            f.paths = []

    def build_paths_set(self):
        """Make set of nodes that are in paths lists to allow quick lookups."""
        if not self.paths:
            return

        self.paths_set = set()
        for path in self.paths:
            for no in path:
                self.paths_set.add(no)

    def dump(self):
        """Return string with basic node info."""
        return f'{self.name}: stale={self.stale}, time={self.tile}, hash={self.hash}'

    def format(self, pat=None):
        """
        @return formatted string.
        @param pat: Supported format specifiers:
        %a: absolute name
        %d: date
        %b: base name
        %r: root name (no directory prefix or extension suffix)
        %m: modified time
        None: as-is name
        """
        if pat:
            if '%a' in pat:
                a = os.path.abspath(self.name)
                pat = pat.replace('%a', a)

            if '%d' in pat or '%t' in pat:
                d, t = time2strings(self.time)
                pat = pat.replace('%d', d)
                pat = pat.replace('%t', t)

            if '%b' in pat:
                b = os.path.basename(self.name)
                pat = pat.replace('%b', b)

            if '%r' in pat:
                b = os.path.basename(self.name)
                idx = b.rfind('.')  # Allow dot files, eg. .bashrc
                r = b[:idx] if (idx > 0) else b
                pat = pat.replace('%r', r)

            return pat
        else:
            return self.name

    def reset(self):
        """Reset staleness, hash and time."""
        self.stale = None
        self.time = 0
        self.hash = None

    def update(self, time=True, hash=False):
        """Get modified time for file from system and optionally compute hash."""
        self.reset()

        if self.phony:
            return

        exists = os.path.exists(self.name)
        # Missing file is considered stale (we need to make it).
        if not exists:
            self.stale = 1

        if time and exists:
            self.time = os.path.getmtime(self.name)

        if hash:
            self.hash = hashdb.md5(self.name)


###########################################################
class iterator(object):
    """
    Iterate over dagger results and get groups of items mutually exclusive in dependency graph.
    Use for guiding serial or parallel processing.
    """

    def __init__(self, dag, items):
        self.dag = dag

        if type(items) == ldict:
            self.ldict = items
        else:
            self.ldict = ldict(items)

        # Setup quick path lookups.
        for no in self.ldict.dict:
            no.build_paths_set()

    def next(self, n=1):
        """Get next n independent item names. n=1 by default."""
        cur = self.ldict.head
        if not cur:
            return []

        result = [cur.data]
        cur = cur.next

        # Check if cur is not in path of any prev to allow parallel updates.
        while (len(result) < n) and cur:
            independent = all([cur.data not in no.paths_set for no in result])
            if independent:
                result.append(cur.data)

            cur = cur.next

        return [no.name for no in result]

    def remove(self, item):
        """Remove item from candidate list."""
        if isinstance(item, node):
            self.ldict.remove(item)
        else:
            self.ldict.remove(self.dag.nodes[item])

    def __len__(self):
        """
        Returns number of all items currently available in iterator
        ('remove' reduces this value).
        """
        return len(self.ldict.dict)


###########################################################
class dagger(object):
    """Evaluates file dependencies in pure python."""

    def __init__(self, hashfile='', sqlite=False, sqlite_memory=1):
        """
        Check if nodes are stale based on modified time or hash log (each line has file,hash).

        hashfile: filename for hash log file.
        """
        # Loaded hash db.
        self.db = None
        # Which files to force as stale or uptodate.
        self.forced = {}
        # Globally hash all files.
        self.hashall = False
        # Filename for db.
        self.hashfile = hashfile
        # Allow hashing per file. Default is no.
        self.useshash = {}
        # Store DAG eval order from bottom to top in node tree.
        self.order = []
        # Nodes are only unique by name.
        self.nodes = {}
        # Set of node names to consider phony.
        self.phonys = set()
        # Use SQLite database instead of text file.
        self.sqlite = sqlite
        self.sqlite_memory = sqlite_memory

    def add(self, target, sources=[]):
        """Make target depend on optional sources."""
        tnode = self.get(target)

        for s in sources:
            snode = self.get(s)
            tnode.add(snode)

    def dot(self, out=None, format=None, color=True):
        """
        Return dot graph as string and optionally write to file 'out'.
        Stale nodes will be colored red.

        You can set the file name 'format' for node labels.
        """
        red = '"#ff8888"'
        s = 'digraph dagger {\nbgcolor = white;\n'

        # Just create parent->child lines.
        for p in list(self.nodes.values()):
            pformat = p.format(format)
            atts = []
            if color and p.stale:
                atts.append("fillcolor = %s" % (red))
            else:
                atts.append("fillcolor = white")

            if atts:
                s += '%s [%s]\n' % (pformat, ','.join(atts))

            for c in p.nodes:
                cformat = c.format(format)
                atts = []
                if color and c.stale:
                    atts.append("fillcolor = %s" % (red))
                else:
                    atts.append("fillcolor = white")

                if atts:
                    s += '%s [%s]\n' % (cformat, ','.join(atts))

                s += '%s -> %s;\n' % (pformat, cformat)

        s += '}'

        if out:
            with open(out, 'w') as f:
                f.write(s)

        return s

    def dump(self):
        """Text dump of nodes."""
        return '\n'.join([n.dump() for n in self.nodes.values()])

    def exporthash(self):
        """Write hashdb for all nodes."""
        db = hashdb(self.hashfile)
        db.load()

        for k in self.nodes:
            f = self.nodes[k]
            if f.hash:
                db.set(k, f.hash)
            else:
                db.update(k)

        db.export()

    def get(self, name):
        """Get node by name."""
        if name not in self.nodes:
            self.nodes[name] = node(name)

        return self.nodes[name]

    def iter(self, names=[]):
        """
        Return iterator for all stale nodes listed by name (and their dependents).
        If [] is given, then all stale nodes (and their dependents) will be returned.
        """
        if names is None:
            return []

        if not names:   # User wants all stale.
            stalenames = [no.name for no in self.order.list if no.stale]
        else:
            stalenames = [name for name in names if self.nodes[name].stale]

        # Need to preserve dag run order to reduce path checking during iterator.next
        # to guarantee mutual independence, so sort queries by their dag search order indices.
        sort = [(self.order.index(self.nodes[k]), self.nodes[k])
                for k in stalenames]
        sort.sort()

        # Get just the node from the (index,node) sorted tuples.
        requests = [idx_no[1] for idx_no in sort]
        allrequests = ldict(requests)

        # Also add dependents (all nodes in path to a root node).
        # They are stale if a child node was stale.
        for no in requests:
            if not no.paths:
                continue

            for path in no.paths:
                for pno in path:
                    allrequests.append(pno)

        return iterator(self, allrequests)

    def ordernames(self):
        """Return names of files discovered during graph evaluation."""
        return ','.join([n.name for n in self.order])

    def pathnames(self, name):
        """Return list of lists where paths use names instead of object references."""
        no = self.nodes[name]
        if not no.paths:
            return no.paths

        return [[pno.name for pno in path] for path in no.paths]

    def phony(self, name):
        """
        Set node with name to be phony, so even when file with name is missing,
        it won't be considered stale, unless it has a stale child.
        """
        self.phonys.add(name)

    def resetnodes(self):
        """Reset all nodes."""
        for n in self.nodes.values():
            n.reset()

    def stale(self, name, force=1):
        """Force node with name to be stale (force=1) or uptodate (force=0)."""
        self.forced[name] = force

    def hash(self, name, enable=1):
        """Enable hashing for file node."""
        self.useshash[name] = enable

    def tree(self):
        """Return simple tree string of all nodes."""
        out = ''
        for f in self.nodes:
            thenode = self.nodes[f]
            if thenode.nodes:
                out += f + ': '
                for c in thenode.nodes:
                    out += c.name + ' '
                out += '\n'

        return out

    def run(self, allpaths=True):
        """
        Find stale nodes based on modtime or hash.

        allpaths: If true, also find all paths from roots to leaf nodes.
        """

        if (not self.db) and self.hashfile:
            if self.sqlite:
                self.db = hashdb_sqlite(self.hashfile, memory=self.sqlite_memory)
            else:
                self.db = hashdb(self.hashfile)

            self.db.load()

        # First pass get their latest info.
        for f in self.nodes:
            hash = self.hashall or self.useshash.get(f, 0)
            self.nodes[f].phony = f in self.phonys
            self.nodes[f].update(time=not hash, hash=hash)

        # Second pass, have each node check for a stale child,
        # check hash, and find all paths in graph.
        # Also store the search order.
        self.order = idict()

        # Quick check to prevent adding duplicates into self.order.
        ordered = set()

        # Get only roots.
        roots = [f for f in self.nodes.values() if f.paths is None]
        # Clear previous paths.
        for f in self.nodes.values():
            if f.paths:
                f.paths = []

        visit = {}  # Children lists are copied and popped to find all paths.
        for root in roots:
            # deque pops are faster than list, and we want paths ordered
            # left to right.
            q = deque([root])
            if allpaths or (root not in visit):
                visit[root] = deque(root.nodes)

            while q:
                top = q[0]
                if visit[top]:
                    child = visit[top].popleft()
                    q.appendleft(child)
                    if allpaths or child not in visit:
                        visit[child] = deque(child.nodes)
                else:
                    # Done visiting all children.
                    # Determine staleness only once.
                    # Redundant visits are only for building all paths.
                    if top.stale is None:
                        if top.name in self.forced:
                            top.stale = self.forced[top.name]
                        else:
                            usehash = self.hashall or self.useshash.get(top.name, 0)
                            if usehash and self.db:
                                dbhash = self.db.get(top.name)
                            else:
                                dbhash = None

                            # If db doesn't have hash for file because it wasn't hashed before,
                            # then its not stale yet.
                            if dbhash and (dbhash != top.hash):
                                top.stale = 1
                            else:
                                if (top.name in self.phonys) or usehash:
                                    top.stale = int(any(child.stale for child in top.nodes))
                                else:  # Also compare with children time.
                                    top.stale = int(any(child.stale or (top.time < child.time) for child in top.nodes))

                    q.popleft()
                    if top.paths is not None:   # If not root node.
                        # Store this depth-first-search path. One per parent.
                        path = list(q)  # Deep copy.
                        top.paths.append(path)

                    if top not in ordered:
                        # Build ordered node visit history.
                        self.order.append(top)
                        ordered.add(top)
