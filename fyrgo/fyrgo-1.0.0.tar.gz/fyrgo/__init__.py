#-*-coding:utf-8-*-

#main classes and functions
from fyrgo.load import DataLoader
from fyrgo.postprocess import profile, crop, write_a_fargo_binary, torque_from_density

#submodules
from fyrgo.phys import hill_radius, omega_frame
from fyrgo.geometry import circle, ellipse

#package information

__version__ = '1.0.0'
__author__  = 'Clément Robert'
__contact__ = 'clement.robert@oca.eu'
__credits__ = ['Héloïse Méheut']
__licence__ = 'GNU'
