"""
Populate contains two functions that are called on application startup
(if you haven't modified kotti.populators).
"""
from kotti_controlpanel.util import add_settings
from kotti_group_manager.controlpanel import GroupRulesControlPanel

def populate():
    add_settings(GroupRulesControlPanel)

