"""Utils to parse .info or .par files to XML.

example
-------
tree   = fyrgo.utils.XmlTree('config.info')
config = tree.get_cElementTree()
"""
import sys
from xml.etree import cElementTree


class XmlTree:
    '''A class to convert .info configuration file to XML format.'''

    class XmlAttribute:
        '''micro class only useful internally'''
        def __init__(self, txtstr):
            '''txtstr must be formated as "key value"'''
            self.key, self.val = txtstr.split()
            self.key = self.key.lower()
        def __repr__(self):
            return f"{self.key}='{self.val}'"


    def __init__(
            self,
            source  : str,
            level   : int = 0,
            strmode : bool = False
    ):
        '''
        source can either be a filename or a string, that
        must be formated as
        --------------------------
        "highestlevel {
        level0 {
        key1 value1
        key2 value2
        level1 {
        key11 value11
        level2 {
        }
        }
        }
        level0 {
        key1 value1
        key2 value2
        level1 {
        key11 value11
        level2 {
        }
        }
        }
        }"
        --------------------------
        '''
        #this is a pythonic way to have several constructors for a class
        if strmode:
            txtstr = source
        else:
            txtstr = XmlTree.str_from_info(source)
        lines = txtstr.split('\n')
        self.level = level
        self._construct_tree(lines)
        self.hasSubtrees = (self.subtrees != [])
        self.hasAttribs  = (self.attribs  != [])
        if int(sys.version[0]) < 3:
            from string import capitalize
            self.rootname = capitalize(lines[0].split()[0])
        else:
            self.rootname = lines[0].split()[0].capitalize()

    def _construct_tree(self, lines: list) -> None:
        '''makes the constructor recursive, add
            * subtrees (XmlTree classobjects)
            * attributes (XmlAttribute class objects)
        '''
        self.attribs = []
        self.subtrees = []
        n_lines = len(lines)
        i = 1
        subtree_args = {'level': self.level+1, 'strmode': True}

        while i < n_lines:
            line = lines[i]
            if lines[i].endswith('{'):
                start,end = XmlTree.find_subtree(lines,i)
                self.subtrees.append(XmlTree('\n'.join(lines[start:end]), **subtree_args))
                i = end
            elif line.endswith('}'):
                i+=1
            else:
                self.attribs.append(self.__class__.XmlAttribute(lines[i]))
                i+=1

    @staticmethod
    def find_subtree(lines: list, init: int) -> tuple:
        '''Find limits of a self-consistent subtree to be used by _construct_tree().'''
        n_lines = len(lines)
        start = init
        end = init+1
        open_brackets = 1
        while open_brackets > 0 and end < n_lines:
            if lines[end].endswith('{'):
                open_brackets += 1
            elif lines[end].endswith('}'):
                open_brackets -= 1
            end += 1
        return start, end

    def __repr__(self) -> str:
        '''Yield a XML string, parsable with xml.etree.cElementTree'''
        indent = '  '*self.level
        openintag  = indent+'<%s'  % (self.rootname)
        closeintag = '>\n'
        outtag = indent+'</%s>\n' % (self.rootname)
        attribstr = ''
        substr = ''
        if self.hasAttribs:
            attribstr = ' '+' '.join([repr(at) for at in self.attribs])
        if self.hasSubtrees:
            substr = ''.join([repr(tree) for tree in self.subtrees])
        intag = openintag+attribstr+closeintag
        return f'{intag}{substr}{outtag}'

    @staticmethod
    def str_from_info(filename: str) -> str:
        '''Convert a .info file to a str parsable by the class constructor.'''
        #devnote: add submethod to ensure attributes are placed first
        #and subtrees second
        ext = filename.split('.')[-1]
        with open(filename,'r') as fi:
            lines = fi.readlines()
        for commentsign in [';','%','#']:#remove comments
            lines = [line.split(commentsign)[0].strip() for line in lines]
        if ext == 'par':
            # .par files use '#' for comments, and that is the only
            # way we can decorate the file. Hence, there's no mean to
            # indicate a node, so we won't parse them here.
            # Instead we put everything in a 'Found' node that isn't root so
            # that the attributes can still be fetched by Scan.search()
            lines = ['Found {'] + lines + ['}']
        lines = list(filter(lambda l: l != '', lines))#remove empty lines
        lines = ['Config {'] + lines + ['}']
        return '\n'.join(lines)

    def get_cElementTree(self):
        'Convert to xml.etree.cElementTree'
        return cElementTree.fromstring(repr(self))


# ===========================================================
def parse_conf(configfile: str) -> XmlTree:
    '''Return the xml parsed tree representing the configuration file.'''
    configtree = XmlTree(configfile).get_cElementTree()
    return configtree
