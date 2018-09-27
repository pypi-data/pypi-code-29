#!/usr/bin/env python
#
# License: BSD
#   https://raw.githubusercontent.com/stonier/py_trees/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
.. argparse::
   :module: py_trees.demos.curb_climb
   :func: command_line_argument_parser
   :prog: py-trees-demo-selector

.. graphviz:: dot/demo-selector.dot

.. image:: images/selector.gif

"""
##############################################################################
# Imports
##############################################################################

import argparse
import py_trees
import sys
import time

import py_trees.console as console

##############################################################################
# Classes
##############################################################################


def description():
    content = "Higher priority switching and interruption in the children of a selector.\n"
    content += "\n"
    content += "In this example the higher priority child is setup to fail initially,\n"
    content += "falling back to the continually running second child. On the third\n"
    content += "tick, the first child succeeds and cancels the hitherto running child.\n"
    if py_trees.console.has_colours:
        banner_line = console.green + "*" * 79 + "\n" + console.reset
        s = "\n"
        s += banner_line
        s += console.bold_white + "Selectors".center(79) + "\n" + console.reset
        s += banner_line
        s += "\n"
        s += content
        s += "\n"
        s += banner_line
    else:
        s = content
    return s


def epilog():
    if py_trees.console.has_colours:
        return console.cyan + "And his noodly appendage reached forth to tickle the blessed...\n" + console.reset
    else:
        return None


def command_line_argument_parser():
    parser = argparse.ArgumentParser(description=description(),
                                     epilog=epilog(),
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     )
    parser.add_argument('-r', '--render', action='store_true', help='render dot tree to file')
    return parser


def create_tree():
    root = py_trees.composites.Sequence("Curb Climb")
    
    toes_to_curb = py_trees.behaviours.Success(name="Toes to Curb")
    
    haul_ass = py_trees.composites.Parallel(
        name="Haul Ass",
        policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
    front_toes_down = py_trees.behaviours.Success(name="Front Toes Down")
    lift_bum = py_trees.behaviours.Success(name="Lift Bum")
    haul_ass.add_children([front_toes_down, lift_bum])
    
    front_toe_traverse=py_trees.behaviours.Success(name="Front Toe Traverse")
    drive=py_trees.behaviours.Success(name="Drive")
    rear_toe_down=py_trees.behaviours.Success(name="Rear Toe Down")
    lift_back_wheel=py_trees.behaviours.Success(name="Lift Back Wheel")
    rear_toe_traverse=py_trees.behaviours.Success(name="Rear Toe Traverse")
    toes_go_home=py_trees.behaviours.Success(name="Toes go Home")
    
    root.add_children([toes_to_curb, haul_ass,
                       front_toe_traverse, drive,
                       rear_toe_down, lift_back_wheel,
                       rear_toe_traverse, toes_go_home
                       ])
    return root

def create_tree_with_timeouts():
    root=py_trees.composites.Parallel(
        name="Curb Climb",
        policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)

    timeout = py_trees.meta.success_is_failure(py_trees.timers.Timer)(
        name="Timeout\n(15s)",
        duration=15.0) # seconds                                             
    just_do_it = py_trees.composites.Sequence(name="Just Do it")
    
    toes_to_curb = py_trees.behaviours.Success(name="Toes to Curb")
    
    haul_ass = py_trees.composites.Parallel(
        name="Haul Ass",
        policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
    front_toes_down = py_trees.behaviours.Success(name="Front Toes Down")
    lift_bum = py_trees.behaviours.Success(name="Lift Bum")
    haul_ass.add_children([front_toes_down, lift_bum])
    
    front_toe_traverse=py_trees.behaviours.Success(name="Front Toe Traverse")
    drive=py_trees.behaviours.Success(name="Drive")
    rear_toe_down=py_trees.behaviours.Success(name="Rear Toe Down")
    lift_back_wheel=py_trees.behaviours.Success(name="Lift Back Wheel")
    rear_toe_traverse=py_trees.behaviours.Success(name="Rear Toe Traverse")
    toes_go_home=py_trees.behaviours.Success(name="Toes go Home")
    
    just_do_it.add_children([toes_to_curb, haul_ass,
                             front_toe_traverse, drive,
                             rear_toe_down, lift_back_wheel,
                             rear_toe_traverse, toes_go_home
                            ])
    root.add_children([timeout, just_do_it])
    return root

def create_tree_with_timeouts_and_recovery():
    
    root = py_trees.composites.Selector(name="Curb Climb")
    
    do_or_die=py_trees.composites.Parallel(
        name="Do or Die",
        policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)

    timeout = py_trees.meta.success_is_failure(py_trees.timers.Timer)(
        name="Timeout\n(15s)",
        duration=15.0) # seconds                                             
    just_do_it = py_trees.composites.Sequence(name="Just Do it")
    
    toes_to_curb = py_trees.behaviours.Success(name="Toes to Curb")
    
    haul_ass = py_trees.composites.Parallel(
        name="Haul Ass",
        policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
    front_toes_down = py_trees.behaviours.Success(name="Front Toes Down")
    lift_bum = py_trees.behaviours.Success(name="Lift Bum")
    haul_ass.add_children([front_toes_down, lift_bum])
    
    front_toe_traverse=py_trees.behaviours.Success(name="Front Toe Traverse")
    drive=py_trees.behaviours.Success(name="Drive")
    rear_toe_down=py_trees.behaviours.Success(name="Rear Toe Down")
    lift_back_wheel=py_trees.behaviours.Success(name="Lift Back Wheel")
    rear_toe_traverse=py_trees.behaviours.Success(name="Rear Toe Traverse")
    toes_go_home=py_trees.behaviours.Success(name="Toes go Home")
    
    just_do_it.add_children([toes_to_curb, haul_ass,
                             front_toe_traverse, drive,
                             rear_toe_down, lift_back_wheel,
                             rear_toe_traverse, toes_go_home
                            ])
    do_or_die.add_children([timeout, just_do_it])
    
    help=py_trees.behaviours.Running("Help!")
    
    root.add_children([do_or_die, help])
    return root

##############################################################################
# Main
##############################################################################

def main():
    """
    Entry point for the demo script.
    """
    args = command_line_argument_parser().parse_args()
    print(description())
    py_trees.logging.level = py_trees.logging.Level.DEBUG

    tree = create_tree()

    ####################
    # Rendering
    ####################
    if args.render:
        py_trees.display.render_dot_tree(tree)
        sys.exit()

    ####################
    # Execute
    ####################
    tree.setup(timeout=15)
    for i in range(1, 4):
        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            tree.tick_once()
            print("\n")
            py_trees.display.print_ascii_tree(tree, show_status=True)
            time.sleep(1.0)
        except KeyboardInterrupt:
            break
    print("\n")
