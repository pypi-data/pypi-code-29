from anytree import NodeMixin


class Node(NodeMixin):
    location = ''
    data = ''
    traveledPath = []

    def __init__(self, location, data, path, parent=None):
        super(Node, self).__init__()
        self.location = location
        self.data = data
        self.traveledPath = path
        self.parent = parent
