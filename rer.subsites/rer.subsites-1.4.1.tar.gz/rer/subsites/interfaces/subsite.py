# -*- coding: utf-8 -*-
from zope.interface import Interface


class IRERSubsiteLayer(Interface):
    """A layer specific to subsite product
    """


class IRERSubsiteEnabled(Interface):
    """
    Marker interface for Subsite folders
    """


class IRERSubsiteUtilsView(Interface):
    """ Marker interface for SubsiteUtilsView """

    def get_subsite_folder():
        """
        Return the parent folder marked as "Subsite", for retrieve some infos
        like a color and the image pin
        """

    def get_subsite_attributes():
        """
        Retrieve the subsite folder, and get saved css class
        """
