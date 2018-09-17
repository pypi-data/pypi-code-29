import unittest
import tree

# Test for proper world setup and functioning
class world():
    # Setup world
    world = tree.FoundryNode(name='World', id='world')
    trash = tree.FoundryNode(name='Trash',id='trash',parent=world)
    freezer = tree.FoundryNode(name='Freezer', parent=world)
    plate1 = tree.PlateNode(location=1, name='Plate 38', storage_conditions='-20c', parent=freezer)
    plate2 = tree.PlateNode(location=2, name='Plate 39', storage_conditions='-20c', parent=freezer)
    well = tree.WellNode(name='Well1', parent=plate1)
    well2 = tree.WellNode(name='Well2', parent=plate1)
    well3 = tree.WellNode(name='Well3', parent=plate2)
    well4 = tree.WellNode(name='Well4', parent=plate2)
    koengtron = tree.WellNode(name='KoengTron', parent=world)

    # Create a node

    print("Creating a node")
    parent_node = world.get_node(name='Freezer').id
    create_node = {"command": "CREATE",
        "type": "NODE", 
        "target_id": None, 
        "name": "Plate 40",
        "location": None,
        "potential_locations": [],
        "parent": parent_node}
    world.action(create_node)
    world.render()
    
    print("Move a node")
    parent_node = world.get_node(name='KoengTron').id
    move_node = world.get_node(name='Plate 40').id
    move = {"command": "MOVE",
        "target_id": move_node,
        "to": parent_node,
        "location": None}
    world.action(move)
    world.render()
    
    print("Trash a node")
    trash = {"command": "TRASH",
        "target_id": move_node}
    world.action(trash)
    world.render()

    print("Print history")
    print(world.history)

