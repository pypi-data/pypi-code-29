# coding=utf-8
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

u"""Subclasses of abstract classes for use in tests."""

from __future__ import division
from __future__ import absolute_import
from typing import Iterable, Optional, Sequence, Union, cast

import numpy

import cirq

from openfermioncirq.optimization.algorithm import OptimizationAlgorithm
from openfermioncirq.optimization.black_box import BlackBox, StatefulBlackBox
from openfermioncirq.optimization.result import OptimizationResult
from openfermioncirq.variational.ansatz import VariationalAnsatz
from openfermioncirq.variational.objective import VariationalObjective


class ExampleAlgorithm(OptimizationAlgorithm):
    u"""Evaluates 5 random points and returns the best answer found."""

    def optimize(self,
                 black_box,
                 initial_guess=None,
                 initial_guess_array=None
                 ):
        opt = numpy.inf
        opt_params = None
        for _ in xrange(5):
            guess = numpy.random.randn(black_box.dimension)
            val = black_box.evaluate(guess)
            if val < opt:
                opt = val
                opt_params = guess
        return OptimizationResult(
                optimal_value=opt,
                optimal_parameters=cast(numpy.ndarray, opt_params),
                num_evaluations=1,
                cost_spent=0.0,
                status=0,
                message=u'success')


class ExampleBlackBox(BlackBox):
    u"""Returns the sum of the squares of the inputs."""

    @property
    def dimension(self):
        return 2

    def _evaluate(self,
                  x):
        return numpy.sum(x**2)


class ExampleBlackBoxNoisy(ExampleBlackBox):
    u"""Returns the sum of the squares of the inputs plus some noise.
    The noise is drawn from the standard normal distribution, then divided
    by the cost provided.
    """

    def _evaluate_with_cost(self,
                            x,
                            cost):
        return numpy.sum(x**2) + numpy.random.randn() / cost


class ExampleStatefulBlackBox(ExampleBlackBox, StatefulBlackBox):
    u"""Returns the sum of the squares of the inputs."""
    pass


class ExampleAnsatz(VariationalAnsatz):
    u"""An example variational ansatz.

    The ansatz produces the operations::

        0: ───X^theta0───@───X^theta0───M('all')───
                         │              │
        1: ───X^theta1───@───X^theta1───M──────────
    """

    def params(self):
        for i in xrange(2):
            yield cirq.Symbol(u'theta{}'.format(i))

    def _generate_qubits(self):
        return cirq.LineQubit.range(2)

    def operations(self, qubits):
        a, b = qubits
        yield cirq.RotXGate(half_turns=cirq.Symbol(u'theta0')).on(a)
        yield cirq.RotXGate(half_turns=cirq.Symbol(u'theta1')).on(b)
        yield cirq.CZ(a, b)
        yield cirq.RotXGate(half_turns=cirq.Symbol(u'theta0')).on(a)
        yield cirq.RotXGate(half_turns=cirq.Symbol(u'theta1')).on(b)
        yield cirq.MeasurementGate(u'all').on(a, b)


class ExampleVariationalObjective(VariationalObjective):
    u"""An example variational objective.

    The value of the study is the number of qubits that were measured to be 1.
    """

    def value(self,
              circuit_output
              ):
        measurements = circuit_output.measurements[u'all']
        return numpy.sum(measurements)


class ExampleVariationalObjectiveNoisy(ExampleVariationalObjective):
    u"""An example variational objective with a noise model.

    The noise is drawn from the standard normal distribution, then divided
    by the cost provided. If a cost is not specified, the noise is 0.
    """

    def noise(self, cost=None):
        if cost is None:
            return 0.0  # coverage: ignore
        return numpy.random.randn() / cost
