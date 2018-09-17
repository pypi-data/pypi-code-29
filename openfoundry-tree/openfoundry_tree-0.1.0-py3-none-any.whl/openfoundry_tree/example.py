request = {"request_id": "UUID",
        "request_date": "timestamp",
        "completion_date": "timestamp",
        "requested_actions": [],
        "completed_actions": []}

move = {"command": "MOVE",
        "target_id": "UUID",
        "to": "UUID",
        "location": 1}

trash = {"command": "TRASH",
        "target_id": "UUID"}

command_delete = {"command": "FULL_DELETE",
        "target_id": "UUID"}

create_node = {"command": "CREATE",
        "type": "NODE", # Node, Plate, Well
        "target_id": None, # Optional
        "name": "NAME",
        "location": "location",
        "potential_locations": [],
        "parent": "UUID"}

create_plate = {"command": "CREATE",
        "type": "PLATE",
        "target_id": None, # Optional
        "name": "NAME",
        "location": "location",
        "potential_locations": [],
        "parent": "UUID",
        "plate_type": "Standard",
        "storage_conditions": "4c"}

create_well = {"command": "CREATE",
        "type": "WELL",
        "target_id": None,
        "name": "NAME",
        "location": "location",
        "potential_locations": [],
        "parent": "UUID",
        "volume": int(100),
        "well_type": "standard", # PCR_tube, PCR_well, centrifuge_tube_15ml, centrifuge_tube_50ml, microcentrifuge_tube_2ml, microcentrifuge_tube_1.5ml
        "state": "PROCESSING"}

update_node = {"command": "UPDATE",
        "target_id": "UUID",
        "attribute": "location",
        "value": 4 }

