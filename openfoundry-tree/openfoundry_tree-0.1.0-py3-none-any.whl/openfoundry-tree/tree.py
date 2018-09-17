from anytree import AnyNode, RenderTree, NodeMixin
import uuid
from enum import Enum
from anytree.exporter import DictExporter
from anytree import NodeMixin, RenderTree
from anytree.exporter import JsonExporter
from anytree import search

class EnumString(Enum):
    def __str__(self):
        return str(self.value)

class FoundryBase(object):
    def __init__(self, id=None, name=None):
        self.name = name
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id

class FoundryNode(FoundryBase, NodeMixin):
    def __init__(self, id=None, name=None, parent=None):
        super(FoundryNode,self).__init__(id=id,name=name)
        self.parent = parent
    
    def render(self):
        for pre, _, node in RenderTree(self):
            treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8), node.id)
    
    def search_tree(self, attr, value, render=False):
        search_result = search.find_by_attr(self, name=attr, value=value)
        if render == True:
            search_result.render()
        return search_result

    def get_id(self, name, render=False):
        """A function to get the id of a node given the name"""
        return self.search_tree("name", name, render=render).id
    
    def view_node(self, uuid, render=False):
        """Returns node of uuid"""
        return self.search_tree('id', uuid, render=render)

    # TODO get JSON export functionality. Write UUIDs and Enums as Strings
    # TODO get import functionality from JSON file
    def json_export(self):
        exporter = JsonExporter()
        return exporter.export(self)

    # TODO move function
    
    # TODO edit function
    
    # TODO remove function
    
    # TODO remove_one function
    
    # TODO add function




class WellNode(FoundryNode):
    def __init__(self, id=None, name=None, parent=None, state=None, well_type=None, address=None, volume=None):
        super(WellNode,self).__init__(id=id, name=name, parent=parent)
        self.well_type = well_type
        self.address = address
        self.volume = volume

class PlateNode(FoundryNode):
    def __init__(self, id=None, name=None, parent=None, plate_type=None, storage_conditions=None, plate_number=None):
        super(PlateNode,self).__init__(id=id, name=name, parent=parent)
        self.plate_type = plate_type
        self.storage_conditions = storage_conditions
        self.plate_number = plate_number

class DnaNode(FoundryNode):
    def __init__(self, id=None, name=None, parent=None):
        super(PlateNode,self).__init__(id=id, name=name, parent=parent)

