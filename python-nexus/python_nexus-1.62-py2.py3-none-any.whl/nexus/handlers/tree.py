import re
from nexus.handlers import GenericHandler
from nexus.exceptions import NexusFormatException


class TreeHandler(GenericHandler):
    """Handler for `trees` blocks"""
    is_tree = re.compile(r"""tree .*=.*;""", re.IGNORECASE)

    translate_regex = re.compile(r"""
        ([,(])              # boundary
        ([A-Z0-9_\-\.]+)    # taxa-id
        :?                  # optional colon
        (\[.+?\])?          # minimally match an optional comment chunk
        (\d+(\.\d+)?)?      # optional branchlengths
        (?=[),])?           # end boundary
    """, re.IGNORECASE + re.VERBOSE + re.DOTALL)

    def __init__(self):
        # does the treefile have a translate block?
        self.was_translated = False
        # has detranslate been called?
        self._been_detranslated = False
        self.translators = {}
        self.attributes = []
        self.trees = []
        super(TreeHandler, self).__init__()

    def __getitem__(self, index):
        return self.trees[index]

    @property
    def taxa(self):
        return self.translators.values()

    @property
    def ntrees(self):
        return len(self.trees)

    def parse(self, data):
        """
        Parses a `tree` nexus block from `data`.

        :param data: nexus block data
        :type data: string

        :return: None
        """
        super(TreeHandler, self).parse(data)

        translate_start = re.compile(r"""^translate$""", re.IGNORECASE)
        translation_pattern = re.compile(r"""(\d+)\s(['"\w\d\.\_\-]+)[,;]?""")

        lost_in_translation = False
        for line in data:
            # look for translation start, and turn on lost_in_translation
            if translate_start.match(line):
                lost_in_translation = True
                self.was_translated = True
            elif self.is_mesquite_attribute(line):
                self.attributes.append(line)

            # if we're in a translate block
            elif lost_in_translation:
                if translation_pattern.match(line):
                    taxon_id, taxon = translation_pattern.findall(line)[0]
                    taxon = taxon.strip("'")
                    if taxon_id in self.translators:
                        raise NexusFormatException(
                            "Duplicate Taxa ID %s in translate block" % taxon_id
                        )
                    if taxon in self.translators.values():
                        raise NexusFormatException(
                            "Duplicate Taxon %s in translate block" % taxon
                        )
                        
                    self.translators[taxon_id] = taxon
                if line.endswith(';'):
                    lost_in_translation = False

            elif self.is_tree.search(line):
                self.trees.append(line)

        # get taxa if not translated.
        if not self.translators:
            taxa = re.findall(r"""[(),](\w+)[:),]""", self.trees[0])
            for taxon_id, t in enumerate(taxa, 1):
                self.translators[taxon_id] = t

    def detranslate(self):
        """Detranslates all trees in the file"""
        if self._been_detranslated:
            return
        for idx, tree in enumerate(self.trees):
            self.trees[idx] = self._detranslate_tree(tree, self.translators)
        self._been_detranslated = True

    def _findall_chunks(self, tree):
        """Helper function to find groups used by detranslate."""
        matches = []
        index = 0
        while True:
            match = self.translate_regex.search(tree, index)
            if not match:
                break
            m = dict(zip(
                ['start', 'taxon', 'comment', 'branch'], match.groups()
            ))
            m['match'] = tree[match.start():match.end() + 1]
            m['end'] = tree[match.end()]
            matches.append(m)
            index = match.end()
        return matches

    def _detranslate_tree(self, tree, translatetable):
        """
        Takes a `tree` and expands the short format tree with translated
        taxa labels from `translatetable` into a full format tree.

        :param tree: String containing newick tree
        :type tree: String

        :param translatetable: Mapping of taxa id -> taxa names
        :type translatetable: Dict

        :return: String of detranslated tree
        """
        for found in self._findall_chunks(tree):
            if found['taxon'] in translatetable:
                taxon = translatetable[found['taxon']]
                if found['comment'] and found['branch']:
                    # comment and branch
                    sub = "%s:%s%s" % \
                        (taxon, found['comment'], found['branch'])
                elif found['comment']:
                    # comment only
                    sub = "%s%s" % (taxon, found['comment'])
                elif found['branch']:
                    # branch only
                    sub = "%s:%s" % (taxon, found['branch'])
                else:
                    # taxon only
                    sub = taxon
                sub = "%s%s%s" % (found['start'], sub, found['end'])
                tree = tree.replace(found['match'], sub)
        return tree

    def write(self):
        """
        Generates a string containing a trees block.

        :return: String
        """
        out = ['begin trees;']
        for attr in self.attributes:
            out.append("\t" + attr)
        if self.was_translated and not self._been_detranslated:
            out.append('\ttranslate')
            for index in sorted([int(k) for k in self.translators.keys()]):
                out.append("\t%d %s," % (index, self.translators[str(index)]))
            # handle last taxa label in translate block
            out[-1] = out[-1].replace(',', '')
            # work around bug https://github.com/CompEvol/beast2/issues/713
            out.append(';')
        for tree in self.trees:
            out.append("\t" + tree)
        out.append('end;\n')
        return "\n".join(out)

    def __repr__(self):
        return "<NexusTreeBlock: %d trees>" % self.ntrees
