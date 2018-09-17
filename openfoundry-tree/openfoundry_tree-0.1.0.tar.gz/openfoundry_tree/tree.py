from anytree import AnyNode, RenderTree, NodeMixin
import uuid
from enum import Enum
from anytree.exporter import DictExporter
from anytree import NodeMixin, RenderTree
from anytree.exporter import JsonExporter
from anytree import search
import datetime


class EnumString(Enum):
    def __str__(self):
        return str(self.value)

def timestamp():
    return str(datetime.datetime.now())

class FoundryBase(object):
    def __init__(self, id=None, name=None, location=None, potential_locations=[]):
        self.location = location
        self.name = name
        self.epoch = timestamp()
        self.potential_locations = potential_locations
        if id == None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id

# History:
# CREATE, MOVE, EDIT, DELETE
# TRANSFER, WAIT

class FoundryNode(FoundryBase, NodeMixin):
    def __init__(self, id=None, name=None, location=None, parent=None, potential_locations=[]):
        super(FoundryNode,self).__init__(id=id,name=name,location=location, potential_locations=potential_locations) # add potential locations
        self.parent = parent
        self.history = []

    def render(self):
        for pre, _, node in RenderTree(self):
            treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8), node.id)
    
    def search_tree(self, attr, value, render=False):
        search_result = search.find_by_attr(self, name=attr, value=value)
        if search_result == None:
            raise ValueError("Search result not found")
        if render == True: world.render()
        return search_result

    def get_node(self, name=None, id=None, render=False):
        """A function to get the id of a node given the name"""
        if not name == None:
            return self.search_tree("name", name, render=render)
        elif not id == None:
            return self.search_tree("id", id, render=render)
        else:
            raise ValueError("No name or id given.")
    
    def view_node(self, uuid, render=False):
        """Returns node of uuid"""
        return self.search_tree('id', uuid, render=render)

    def json_export(self):
        exporter = JsonExporter()
        return exporter.export(self)


    # TODO refactor this boilerplate
    def move(self, json_command):
        target = self.get_node(id=json_command["target_id"])
        target.parent = self.get_node(id=json_command["to"])
        target.location = json_command["location"]

    def trash(self, json_command):
        json_command["to"] = "trash"
        json_command["location"] = None
        self.move(json_command)

    def create(self, json_command):
        if json_command["type"] == "NODE":
            FoundryNode(id=json_command["target_id"], name=json_command["name"], location=json_command["location"], potential_locations=json_command["potential_locations"], parent=self.get_node(id=json_command["parent"]))
        if json_command["type"] == "PLATE":
            pass
        if json_command["type"] == "WELL":
            pass

    def action(self, json_command):
        # Do requested action
        if json_command["command"] == "MOVE":
            self.move(json_command)
        if json_command["command"] == "TRASH":
            self.trash(json_command)
        if json_command["command"] == "CREATE":
            self.create(json_command)
        # Log the action
        json_command["completed"] = timestamp()
        root_node = self.get_node(id='world')
        root_node.history.append(json_command)

    # TODO UUID validator

    # TODO locations as a matrix - location validator

class WellNode(FoundryNode):
    def __init__(self, id=None, name=None, location=None, parent=None, state=None, well_type=None, volume=None, potential_locations=[]):
        super(WellNode,self).__init__(id=id, name=name, parent=parent, location=location, potential_locations=potential_locations)
        self.well_type = well_type
        self.volume = volume

class PlateNode(FoundryNode):
    def __init__(self, id=None, name=None, location=None, parent=None, plate_type=None, storage_conditions=None, potential_locations=[]):
        super(PlateNode,self).__init__(id=id, name=name, parent=parent, location=location, potential_locations=potential_locations)
        self.plate_type = plate_type
        self.storage_conditions = storage_conditions # RT, 4c, -20c, -80c

class DnaNode(FoundryNode):
    def __init__(self, id=None, name=None, location=None, parent=None, potential_locations=[]):
        super(PlateNode,self).__init__(id=id, name=name, parent=parent, location=location, potential_locations=potential_locations)

