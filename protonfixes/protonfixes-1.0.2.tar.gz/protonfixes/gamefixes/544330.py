""" Game fix for Snake Pass
WIP
"""
#pylint: disable=C0103


import os
import sys


def main():
    """ Changes the proton argument from the launcher to the game
    """

    print('Applying Snake Pass Game Fixes')

    # Fix crackling audio
    os.environ['PULSE_LATENCY_MSEC'] = '60'

    # Adding -d3d12 -d3d11 d3d10 -vulkan -opengl
    # passive install repair uninstall layout quiet norestart log log.txtjdd
    print(sys.argv)
    '''
    for idx, env in enumerate(sys.argv):
        if 'vulkan' in env:
            sys.argv[idx] = env.replace('vulkan', 'd3d12')
    '''
