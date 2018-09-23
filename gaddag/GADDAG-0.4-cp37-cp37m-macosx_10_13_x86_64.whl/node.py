import ctypes

from .cgaddag import cgaddag, MAX_CHARS

class Node():
    """
    A node in a GADDAG.
    """
    def __init__(self, gdg, node):
        self.node = node
        self.gdg = gdg

    def __str__(self):
        return "[{}] {}".format(", ".join(sorted([edge for edge in self])),
                                self.letter_set)

    def __len__(self):
        """
        Count of edges from this node.
        """
        return len(self.edges)

    def __iter__(self):
        """
        Iterate over the edge characters on this node.
        """
        for char in self.edges:
            yield char

    def __contains__(self, char):
        """
        Check if `char` is an edge character on this node.
        """
        char = char.lower()
        return char in self.edges

    def __getitem__(self, char):
        """
        Follow edge `char` from this node.
        """
        char = char.lower()
        next_node = cgaddag.gdg_follow_edge(self.gdg, self.node,
                                            char.encode("ascii"))

        if not next_node:
            raise KeyError(char)

        return Node(self.gdg, next_node)

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        if self.letter_set != other.letter_set or self.edges != other.edges:
            return False

        for child in self:
            if self[child] != other[child]:
                return False

        return True

    @property
    def edges(self):
        """
        Return the edge characters of this node.
        """
        edge_str = ctypes.create_string_buffer(MAX_CHARS)

        cgaddag.gdg_edges(self.gdg, self.node, edge_str)

        return [char for char in edge_str.value.decode("ascii")]

    @property
    def letter_set(self):
        """
        Return the letter set of this node.
        """
        end_str = ctypes.create_string_buffer(MAX_CHARS)

        cgaddag.gdg_letter_set(self.gdg, self.node, end_str)

        return [char for char in end_str.value.decode("ascii")]

    def is_end(self, char):
        """
        Return `True` if this `char` is part of this node's letter set,
        `False` otherwise.
        """
        char = char.lower()

        return bool(cgaddag.gdg_is_end(self.gdg, self.node, char.encode("ascii")))

    def follow(self, chars):
        """
        Traverse the GADDAG to the node at the end of the given characters.

        Args:
            chars: An string of characters to traverse in the GADDAG.

        Returns:
            The Node which is found by traversing the tree.
        """
        chars = chars.lower()

        node = self.node
        for char in chars:
            node = cgaddag.gdg_follow_edge(self.gdg, node, char.encode("ascii"))
            if not node:
                raise KeyError(char)

        return Node(self.gdg, node)

