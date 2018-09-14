#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Factories for creating recurrence analysis computations.
"""

from pyrqa.exceptions import UnsupportedNeighbourhoodException
from pyrqa.neighbourhood import FixedRadius, RadiusCorridor, FAN

from pyrqa.variants.recurrence_plot.fixed_radius.execution_engine import ExecutionEngine as RPFixedRadiusExecutionEngine
from pyrqa.variants.rqa.fixed_radius.execution_engine import ExecutionEngine as RQAFixedRadiusExecutionEngine


class RecurrencePlotComputation(object):
    """
    Factory for creating a recurrence plot computation.
    """

    @classmethod
    def create(cls,
               settings,
               **kwargs):
        """
        Create RQA computation.

        :param settings: Recurrence analysis settings.
        :param kwargs: Keyword arguments.
        """

        if isinstance(settings.neighbourhood,
                      FixedRadius):
            return RPFixedRadiusExecutionEngine(settings,
                                                **kwargs)
        elif isinstance(settings.neighbourhood,
                        RadiusCorridor):
            raise UnsupportedNeighbourhoodException("Neighbourhood '%s' is not yet supported!" % settings.neighbourhood.__class__.__name__)
        elif isinstance(settings.neighbourhood,
                        FAN):
            raise UnsupportedNeighbourhoodException("Neighbourhood '%s' is not yet supported!" % settings.neighbourhood.__class__.__name__)
        else:
            raise UnsupportedNeighbourhoodException("Neighbourhood '%s' is not supported!" % settings.neighbourhood.__class__.__name__)


class RQAComputation(object):
    """
    Factory for creating a recurrence quantification analysis computation.
    """

    @classmethod
    def create(cls,
               settings,
               **kwargs):
        """
        Create recurrence plot computation.

        :param settings: Recurrence analysis settings.
        :param kwargs: Keyword arguments.
        """

        if isinstance(settings.neighbourhood,
                      FixedRadius):
            return RQAFixedRadiusExecutionEngine(settings,
                                                 **kwargs)
        elif isinstance(settings.neighbourhood,
                        RadiusCorridor):
            raise UnsupportedNeighbourhoodException("Neighbourhood '%s' is not yet supported!" % settings.neighbourhood.__class__.__name__)
        elif isinstance(settings.neighbourhood,
                        FAN):
            raise UnsupportedNeighbourhoodException("Neighbourhood '%s' is not yet supported!" % settings.neighbourhood.__class__.__name__)
        else:
            raise UnsupportedNeighbourhoodException("Neighbourhood '%s' is not supported!" % settings.neighbourhood.__class__.__name__)
