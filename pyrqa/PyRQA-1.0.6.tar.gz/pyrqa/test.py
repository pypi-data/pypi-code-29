#!/usr/bin/python

"""
Run all tests of the project.
"""

import os
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()

    print("\nRecurrence Plot Tests")
    print("=====================")

    recurrence_plot_suite = unittest.TestSuite()
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.recurrence_plot.fixed_radius.brute_force.test.Test'))
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.recurrence_plot.fixed_radius.uniform_grid.test.Test'))

    unittest.TextTestRunner(verbosity=2).run(recurrence_plot_suite)

    print("\nRQA Tests")
    print("=========")

    rqa_suite = unittest.TestSuite()
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.fixed_radius.brute_force.test.Test'))
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.fixed_radius.tree.test.Test'))
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.fixed_radius.uniform_grid.test.Test'))

    unittest.TextTestRunner(verbosity=2).run(rqa_suite)



