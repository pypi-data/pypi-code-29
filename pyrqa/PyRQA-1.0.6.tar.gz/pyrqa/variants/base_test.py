#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Base test for variant testing.
"""

import sys
import unittest

import numpy as np

from pyrqa.metric import EuclideanMetric, MaximumMetric, TaxicabMetric
from pyrqa.neighbourhood import FixedRadius
from pyrqa.opencl import OpenCL
from pyrqa.selector import SingleSelector, \
    EpsilonGreedySelector, \
    VWGreedySelector, \
    EpsilonDecreasingSelector, \
    EpsilonFirstSelector
from pyrqa.settings import Settings
from pyrqa.time_series import SingleTimeSeries


class BaseTest(unittest.TestCase):
    """
    Tests for RQA, Fixed Radius, OpenCL.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test.

        :cvar time_series: Random time series consisting either of a custom number or 1024 floating point values.
        """

        time_series_length = pow(2, 10)
        try:
            time_series_length = np.int(sys.argv[1])
        except ValueError:
            pass
        except IndexError:
            pass

        cls.time_series = SingleTimeSeries(np.array(np.random.rand(time_series_length),
                                                    dtype=np.float32))

    def compare_recurrence_plot_results(self,
                                        recurrence_plot_result_1,
                                        recurrence_plot_result_2,
                                        variant=None):
        """
        Compare recurrence plot results.

        :param recurrence_plot_result_1: First recurrence plot result.
        :param recurrence_plot_result_2: Second recurrence plot result.
        :param variant: Recurrence plot computing variant.
        """

        if variant:
            msg_prefix = "[Variant: %s] " % variant
        else:
            msg_prefix = "[All Variants] "

        self.assertFalse(False in (recurrence_plot_result_1.recurrence_matrix == recurrence_plot_result_2.recurrence_matrix),
                         msg="%sThe recurrence matrices deviate by '%s'." %
                             (msg_prefix,
                              recurrence_plot_result_2.recurrence_matrix - recurrence_plot_result_1.recurrence_matrix))

    def compare_rqa_results(self,
                            rqa_result_1,
                            rqa_result_2,
                            variant=None):
        """
        Compare recurrence quantification analysis results.

        :param rqa_result_1: First rqa result.
        :param rqa_result_2: Second rqa result.
        :param variant: RQA computing variant.
        """

        if variant:
            msg_prefix = "[Variant: %s] " % variant
        else:
            msg_prefix = "[All Variants] "

        self.assertFalse(False in (rqa_result_1.recurrence_points == rqa_result_2.recurrence_points),
                         msg="%sThe recurrence points deviate by '%s'." %
                             (msg_prefix,
                              rqa_result_2.recurrence_points - rqa_result_1.recurrence_rate))

        self.assertFalse(False in (rqa_result_1.diagonal_frequency_distribution == rqa_result_2.diagonal_frequency_distribution),
                         msg="%sThe diagonal frequency distributions deviate by '%s'." %
                             (msg_prefix,
                              rqa_result_2.diagonal_frequency_distribution - rqa_result_1.diagonal_frequency_distribution))

        self.assertFalse(False in (rqa_result_1.vertical_frequency_distribution == rqa_result_2.vertical_frequency_distribution),
                         msg="%sThe vertical frequency distributions deviate by '%s'." %
                             (msg_prefix,
                              rqa_result_2.vertical_frequency_distribution - rqa_result_1.vertical_frequency_distribution))

        self.assertFalse(False in (rqa_result_1.white_vertical_frequency_distribution == rqa_result_2.white_vertical_frequency_distribution),
                         msg="%sThe white vertical frequency distributions deviate by '%s'." %
                             (msg_prefix,
                              rqa_result_2.white_vertical_frequency_distribution - rqa_result_1.white_vertical_frequency_distribution))

    def perform_recurrence_analysis_computations(self,
                                                 settings,
                                                 opencl=None,
                                                 verbose=False,
                                                 edge_length=None,
                                                 selector=None,
                                                 variants_kwargs=None,
                                                 all_variants=False):
        """
        Perform recurrence analysis computations.

        :param settings: Settings.
        :param opencl: OpenCL environment.
        :param verbose: Verbosity of command line print outs.
        :param edge_length: Default edge length of the sub matrices.
        :param selector: Flavour selection strategy.
        :param variants_kwargs: Variants keyword arguments.
        :param all_variants: Employ all variants.
        """

        pass

    def test_default(self):
        """
        Test using the default recurrence analysis settings.
        """

        for metric in [EuclideanMetric,
                       MaximumMetric,
                       TaxicabMetric]:
            settings = Settings(self.time_series,
                                similarity_measure=metric)

            self.perform_recurrence_analysis_computations(settings,
                                                          selector=SingleSelector(loop_unroll_factors=(1,)))

    def test_optimisations_enabled(self):
        """
        Test using the default recurrence analysis settings.
        """

        for metric in [EuclideanMetric,
                       MaximumMetric,
                       TaxicabMetric]:
            settings = Settings(self.time_series,
                                similarity_measure=metric)

            self.perform_recurrence_analysis_computations(settings,
                                                          selector=SingleSelector(loop_unroll_factors=(1,)),
                                                          variants_kwargs={'optimisations_enabled': True})

    def test_partition(self):
        """
        Test partition of recurrence matrix.
        """

        for metric in [EuclideanMetric,
                       MaximumMetric,
                       TaxicabMetric]:
            settings = Settings(self.time_series,
                                similarity_measure=metric)

            self.perform_recurrence_analysis_computations(settings,
                                                          edge_length=np.random.randint(1, self.time_series.number_of_vectors),
                                                          selector=SingleSelector(loop_unroll_factors=(1,)))

    def test_embedding_parameters(self):
        """
        Test using different than the default recurrence analysis settings.
        """

        for metric in [EuclideanMetric,
                       MaximumMetric,
                       TaxicabMetric]:
            self.time_series.embedding_dimension = np.random.randint(1, 10)
            self.time_series.time_delay = np.random.randint(1, 10)

            settings = Settings(self.time_series,
                                similarity_measure=metric,
                                neighbourhood=FixedRadius(np.random.uniform(.1, 1.)))

            self.perform_recurrence_analysis_computations(settings,
                                                          selector=SingleSelector(loop_unroll_factors=(1,)))

    def test_loop_unroll(self):
        """
        Test using different than the default loop unroll parameter assignment.
        """

        for metric in [EuclideanMetric,
                       MaximumMetric,
                       TaxicabMetric]:
            settings = Settings(self.time_series,
                                similarity_measure=metric)

            choices = np.array([1, 2, 4, 8, 16])

            self.perform_recurrence_analysis_computations(settings,
                                                          verbose=True,
                                                          selector=SingleSelector(loop_unroll_factors=(choices[np.random.randint(0, choices.size - 1)],)))

    def test_selection_strategies(self):
        """
        Test using different selection strategies.
        """

        for metric in [EuclideanMetric,
                       MaximumMetric,
                       TaxicabMetric]:
            settings = Settings(self.time_series,
                                similarity_measure=metric)

            explore = np.arange(1, 11)
            factor = np.arange(1, 4)
            delta = np.arange(1, 6)

            self.perform_recurrence_analysis_computations(settings,
                                                          edge_length=np.random.randint(1, self.time_series.number_of_vectors),
                                                          selector=EpsilonGreedySelector(explore=explore[np.random.randint(0, explore.size)]),
                                                          all_variants=True)

            self.perform_recurrence_analysis_computations(settings,
                                                          edge_length=np.random.randint(1, self.time_series.number_of_vectors),
                                                          selector=VWGreedySelector(explore=explore[np.random.randint(0, explore.size)],
                                                                                    factor=factor[np.random.randint(0, factor.size)]),
                                                          all_variants=True)

            self.perform_recurrence_analysis_computations(settings,
                                                          edge_length=np.random.randint(1, self.time_series.number_of_vectors),
                                                          selector=EpsilonDecreasingSelector(explore=explore[np.random.randint(0, explore.size)],
                                                                                             delta=delta[np.random.randint(0, delta.size)]),
                                                          all_variants=True)

            self.perform_recurrence_analysis_computations(settings,
                                                          edge_length=np.random.randint(1, self.time_series.number_of_vectors),
                                                          selector=EpsilonFirstSelector(explore=explore[np.random.randint(0, explore.size)]),
                                                          all_variants=True)

    @unittest.skipIf("--extended" not in sys.argv, "Activate the test using the argument '--extended'.")
    def test_multiple_devices_per_platform(self):
        """
        Test using all compute devices per OpenCL platform available.
        """

        if sys.version_info.major == 2:
            itr = OpenCL.get_device_ids_per_platform_id().iteritems()
        if sys.version_info.major == 3:
            itr = OpenCL.get_device_ids_per_platform_id().items()

        for platform_id, device_ids in itr:
            opencl = OpenCL(platform_id=platform_id,
                            device_ids=device_ids)

            for metric in [EuclideanMetric,
                           MaximumMetric,
                           TaxicabMetric]:
                settings = Settings(self.time_series,
                                    similarity_measure=metric)

                self.perform_recurrence_analysis_computations(settings,
                                                              opencl=opencl,
                                                              edge_length=np.int(np.ceil(np.float(self.time_series.number_of_vectors) / len(device_ids))),
                                                              selector=SingleSelector(loop_unroll_factors=(1,)))
