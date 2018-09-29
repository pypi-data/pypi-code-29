

from sc2gameLobby import debugCmds
from sc2gameLobby import gameConstants as c


################################################################################
def setupScenario(controller, scenario):
    """once in the in_game state, use the controller to set up the scenario"""
    knownUnits = []
    gl = 0
    getGameState = controller.observe # function that observes what's changed since the prior gameloop(s)
    while True:
        obs = getGameState()
        if obs.observation.game_loop <= 1: continue
        knownUnits = obs.observation.raw_data.units # identify existing units (requieres no fog to be disabled?)
        if knownUnits: break # wait until units are found in the raw observation
    createCmds = debugCmds.create(*scenario.units.values())
    controller.debug(*createCmds) # send create cmd via controller
    rmTags = []
    keepUnits = {18, 59, 86} # command center, nexus and hatchery
    for unit in list(knownUnits):
        if unit.alliance == c.NEUTRAL:  continue # ignore neutral units visible via snapshot to start the game
        if unit.mineral_contents:       continue # don't remove mineral nodes
        if unit.vespene_contents:       continue # don't remove vespene nodes
        if unit.unit_type in keepUnits: continue # don't remove the main building
        if unit.owner != 1:
            print(unit)
        rmTags.append(unit.tag)
    if rmTags:
        rmCmd = debugCmds.remove(*rmTags) # create command to remove existing units
        controller.debug(rmCmd) # send remove cmd to remove existing units
    newUnits = {}
    print("modify!")
    while len(newUnits) < len(scenario.units): # wait until new units are created
        print("*"*80)
        print(">>", len(newUnits), "<", len(scenario.units))
        print("*"*80)
        units = getGameState().observation.raw_data.units
        for unit in scenario.units.values(): # match new unit tags with their originating units
            if unit.tag: continue # already found a matching tag for this unit
            for liveUnit in units: # identify new units and their tags
                print("unit_type", liveUnit.unit_type, type(liveUnit.unit_type),
                    "vs", unit.code, type(unit.code))
                if liveUnit.unit_type != unit.code: continue # can't match a unit of a different type
                print("owner", liveUnit.owner, type(liveUnit.owner),
                    "vs", unit.owner, type(unit.owner))
                if liveUnit.owner != unit.owner: continue # can't match units with different owners
                #l = liveUnit.pos
                #x, y, z = unit.position
                #if (l.x - x) >= 5: continue
                #if (liveUnit.shield - unit
                unit.tag = liveUnit.tag # found a match; sync tags + decalre this unit matched
                print(unit)
                newUnits[unit.tag] = unit # remember this association between unit and its properties
                break
    modifyCmds = debugCmds.modify(**newUnits) # create command to set properties of in-game units
    #controller.debug(*modifyCmds) # send modify cmd via controller
    print("announce scenario setup is finished")

