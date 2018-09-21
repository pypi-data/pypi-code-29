# -*- coding: utf-8 -*-
import logging


logger = logging.getLogger(__name__)


default_profile = 'profile-rer.subsites:default'


def to_2100(context):
    """
    """
    logger.info('Upgrading rer.subsites to version 2100')
    context.runImportStepFromProfile(default_profile, 'rolemap')
    context.runImportStepFromProfile(default_profile, 'actions')


def to_2200(context):
    """
    """
    logger.info('Removing resources for colorpicker')
    context.runAllImportStepsFromProfile(
        'profile-rer.subsites:remove_colorpicker')
