# coding=utf-8
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

u"""Gates that are commonly used for quantum simulation of fermions."""

from __future__ import division
from __future__ import absolute_import
from typing import Optional, Union

import numpy

import cirq


class FermionicSwapGate(cirq.InterchangeableQubitsGate,
                        cirq.KnownMatrix,
                        cirq.ReversibleEffect,
                        cirq.TextDiagrammable,
                        cirq.TwoQubitGate):
    u"""Swaps two adjacent fermionic modes under the JWT."""

    def matrix(self):
        return numpy.array([[1, 0, 0, 0],
                            [0, 0, 1, 0],
                            [0, 1, 0, 0],
                            [0, 0, 0, -1]])

    def inverse(self):
        return self

    def text_diagram_info(self, args
                          ):
        if args.use_unicode_characters:
            wire_symbols = (u'×ᶠ', u'×ᶠ')
        else:
            wire_symbols = (u'fswap', u'fswap')
        return cirq.TextDiagramInfo(wire_symbols=wire_symbols)

    def __repr__(self):
        return u'FSWAP'


class XXYYGate(cirq.EigenGate,
               cirq.CompositeGate,
               cirq.InterchangeableQubitsGate,
               cirq.TextDiagrammable,
               cirq.TwoQubitGate):
    u"""XX + YY interaction.

    There are two ways to instantiate this gate.

    The first is to provide an angle in units of either half-turns,
    radians, or degrees. In this case, the gate's matrix is defined
    as follows::

        XXYY**h ≡ exp(-i π h (X⊗X + Y⊗Y) / 4)
                ≡ exp(-i rads (X⊗X + Y⊗Y) / 4)
                ≡ exp(-i π (degs / 180) (X⊗X + Y⊗Y) / 4)
                ≡ [1 0             0             0]
                  [0 cos(π·h/2)    -i·sin(π·h/2) 0]
                  [0 -i·sin(π·h/2) cos(π·h/2)    0]
                  [0 0             0             1]

    where h is the angle in half-turns.

    The second way is to provide a duration of time. In this case, the gate
    implements the unitary::

        exp(-i t (X⊗X + Y⊗Y) / 2) ≡ [1 0         0         0]
                                    [0 cos(t)    -i·sin(t) 0]
                                    [0 -i·sin(t) cos(t)    0]
                                    [0 0         0         1]

    where t is the duration. This corresponds to evolving under the
    Hamiltonian (X⊗X + Y⊗Y) / 2 for that duration of time.
    """

    def __init__(self, **_3to2kwargs):
        if 'duration' in _3to2kwargs: duration = _3to2kwargs['duration']; del _3to2kwargs['duration']
        else: duration = None
        if 'degs' in _3to2kwargs: degs = _3to2kwargs['degs']; del _3to2kwargs['degs']
        else: degs = None
        if 'rads' in _3to2kwargs: rads = _3to2kwargs['rads']; del _3to2kwargs['rads']
        else: rads = None
        if 'half_turns' in _3to2kwargs: half_turns = _3to2kwargs['half_turns']; del _3to2kwargs['half_turns']
        else: half_turns = None
        u"""Initializes the gate.

        At most one of half_turns, rads, degs, or duration may be specified.
        If more are specified, the result is considered ambiguous and an
        error is thrown. If no argument is given, the default value of one
        half-turn is used.

        Args:
            half_turns: The exponent angle, in half-turns.
            rads: The exponent angle, in radians.
            degs: The exponent angle, in degrees.
            duration: The exponent as a duration of time.
        """
        if len([1 for e in [half_turns, rads, degs, duration]
                if e is not None]) > 1:
            raise ValueError(u'Redundant exponent specification. '
                             u'Use ONE of half_turns, rads, degs, or duration.')

        if duration is not None:
            exponent = 2 * duration / numpy.pi
        else:
            exponent = cirq.value.chosen_angle_to_half_turns(
                    half_turns=half_turns,
                    rads=rads,
                    degs=degs)

        super(XXYYGate, self).__init__(exponent=exponent)

    @property
    def half_turns(self):
        return self._exponent

    def _eigen_components(self):
        return [
            (0, numpy.diag([1, 0, 0, 1])),
            (-0.5, numpy.array([[0, 0, 0, 0],
                                [0, 0.5, 0.5, 0],
                                [0, 0.5, 0.5, 0],
                                [0, 0, 0, 0]])),
            (+0.5, numpy.array([[0, 0, 0, 0],
                                [0, 0.5, -0.5, 0],
                                [0, -0.5, 0.5, 0],
                                [0, 0, 0, 0]]))
        ]

    def _canonical_exponent_period(self):
        return 4

    def _with_exponent(self, exponent):
        return XXYYGate(half_turns=exponent)

    def default_decompose(self, qubits):
        a, b = qubits
        yield cirq.Z(a) ** 0.5
        yield YXXY(a, b) ** self.half_turns
        yield cirq.Z(a) ** -0.5

    def text_diagram_info(self, args
                          ):
        return cirq.TextDiagramInfo(
            wire_symbols=(u'XXYY', u'XXYY'),
            exponent=self.half_turns)

    def __repr__(self):
        if self.half_turns == 1:
            return u'XXYY'
        return u'XXYY**{!r}'.format(self.half_turns)


class YXXYGate(cirq.EigenGate,
               cirq.CompositeGate,
               cirq.TextDiagrammable,
               cirq.TwoQubitGate):
    u"""YX - XY interaction.

    There are two ways to instantiate this gate.

    The first is to provide an angle in units of either half-turns,
    radians, or degrees. In this case, the gate's matrix is defined
    as follows::

        YXXY**h ≡ exp(-i π h (Y⊗X - X⊗Y) / 4)
                ≡ exp(-i rads (Y⊗X - X⊗Y) / 4)
                ≡ exp(-i π (degs / 180) (Y⊗X - X⊗Y) / 4)
                ≡ [1 0          0           0]
                  [0 cos(π·h/2) -sin(π·h/2) 0]
                  [0 sin(π·h/2) cos(π·h/2)  0]
                  [0 0          0           1]

    where h is the angle in half-turns.

    The second way is to provide a duration of time. In this case, the gate
    implements the unitary::

        exp(-i t (Y⊗X - X⊗Y) / 2) ≡ [1 0      0       0]
                                    [0 cos(t) -sin(t) 0]
                                    [0 sin(t) cos(t)  0]
                                    [0 0      0       1]

    where t is the duration. This corresponds to evolving under the
    Hamiltonian (Y⊗X - X⊗Y) / 2 for that duration of time.
    """

    def __init__(self, **_3to2kwargs):
        if 'duration' in _3to2kwargs: duration = _3to2kwargs['duration']; del _3to2kwargs['duration']
        else: duration = None
        if 'degs' in _3to2kwargs: degs = _3to2kwargs['degs']; del _3to2kwargs['degs']
        else: degs = None
        if 'rads' in _3to2kwargs: rads = _3to2kwargs['rads']; del _3to2kwargs['rads']
        else: rads = None
        if 'half_turns' in _3to2kwargs: half_turns = _3to2kwargs['half_turns']; del _3to2kwargs['half_turns']
        else: half_turns = None
        u"""Initializes the gate.

        At most one of half_turns, rads, degs, or duration may be specified.
        If more are specified, the result is considered ambiguous and an
        error is thrown. If no argument is given, the default value of one
        half-turn is used.

        Args:
            half_turns: The exponent angle, in half-turns.
            rads: The exponent angle, in radians.
            degs: The exponent angle, in degrees.
            duration: The exponent as a duration of time.
        """
        if len([1 for e in [half_turns, rads, degs, duration]
                if e is not None]) > 1:
            raise ValueError(u'Redundant exponent specification. '
                             u'Use ONE of half_turns, rads, degs, or duration.')

        if duration is not None:
            exponent = 2 * duration / numpy.pi
        else:
            exponent = cirq.value.chosen_angle_to_half_turns(
                    half_turns=half_turns,
                    rads=rads,
                    degs=degs)

        super(YXXYGate, self).__init__(exponent=exponent)

    @property
    def half_turns(self):
        return self._exponent

    def _eigen_components(self):
        return [
            (0, numpy.diag([1, 0, 0, 1])),
            (-0.5, numpy.array([[0, 0, 0, 0],
                                [0, 0.5, -0.5j, 0],
                                [0, 0.5j, 0.5, 0],
                                [0, 0, 0, 0]])),
            (0.5, numpy.array([[0, 0, 0, 0],
                               [0, 0.5, 0.5j, 0],
                               [0, -0.5j, 0.5, 0],
                               [0, 0, 0, 0]]))
        ]

    def _canonical_exponent_period(self):
        return 4

    def _with_exponent(self, exponent):
        return YXXYGate(half_turns=exponent)

    def default_decompose(self, qubits):
        a, b = qubits
        yield cirq.Z(a) ** -0.5
        yield XXYY(a, b) ** self.half_turns
        yield cirq.Z(a) ** 0.5

    def text_diagram_info(self, args
                          ):
        return cirq.TextDiagramInfo(
            wire_symbols=(u'YXXY', u'#2'),
            exponent=self.half_turns)

    def __repr__(self):
        if self.half_turns == 1:
            return u'YXXY'
        return u'YXXY**{!r}'.format(self.half_turns)


class ZZGate(cirq.EigenGate,
             cirq.TwoQubitGate,
             cirq.TextDiagrammable,
             cirq.InterchangeableQubitsGate):
    u"""ZZ interaction.

    There are two ways to instantiate this gate.

    The first is to provide an angle in units of either half-turns,
    radians, or degrees. In this case, the gate's matrix is defined
    as follows::

        ZZ**h ≡ exp(-i π h (Z⊗Z) / 2)
              ≡ exp(-i rads (Z⊗Z) / 2)
              ≡ exp(-i π (degs / 180) (Z⊗Z) / 2)
              ≡ [exp(-i·π·h/2) 0             0                         0]
                [0             exp(+i·π·h/2) 0                         0]
                [0             0             exp(+i·π·h/2)             0]
                [0             0             0             exp(-i·π·h/2)]

    where h is the angle in half-turns. At a value of one half-turn, this
    gate is equivalent to Z⊗Z = diag(1, -1, -1, 1) up to a global phase.
    More generally, ZZ**h is equivalent to diag(1, (-1)**h, (-1)**h, 1)
    up to a global phase.

    The second way to instantiate this gate is to provide a duration
    of time. In this case, the gate implements the unitary::

        exp(-i t Z⊗Z) ≡ [exp(-it) 0          0               0]
                        [0          exp(+it) 0               0]
                        [0          0        exp(+it)        0]
                        [0          0        0        exp(-it)]

    where t is the duration. This corresponds to evolving under the
    Hamiltonian Z⊗Z for that duration of time.
    """

    def __init__(self, **_3to2kwargs):
        if 'duration' in _3to2kwargs: duration = _3to2kwargs['duration']; del _3to2kwargs['duration']
        else: duration = None
        if 'degs' in _3to2kwargs: degs = _3to2kwargs['degs']; del _3to2kwargs['degs']
        else: degs = None
        if 'rads' in _3to2kwargs: rads = _3to2kwargs['rads']; del _3to2kwargs['rads']
        else: rads = None
        if 'half_turns' in _3to2kwargs: half_turns = _3to2kwargs['half_turns']; del _3to2kwargs['half_turns']
        else: half_turns = None
        u"""Initializes the gate.

        At most one of half_turns, rads, degs, or duration may be specified.
        If more are specified, the result is considered ambiguous and an
        error is thrown. If no argument is given, the default value of one
        half-turn is used.

        Args:
            half_turns: The exponent angle, in half-turns.
            rads: The exponent angle, in radians.
            degs: The exponent angle, in degrees.
            duration: The exponent as a duration of time.
        """
        if len([1 for e in [half_turns, rads, degs, duration]
                if e is not None]) > 1:
            raise ValueError(u'Redundant exponent specification. '
                             u'Use ONE of half_turns, rads, degs, or duration.')

        if duration is not None:
            exponent = 2 * duration / numpy.pi
        else:
            exponent = cirq.value.chosen_angle_to_half_turns(
                    half_turns=half_turns,
                    rads=rads,
                    degs=degs)

        super(ZZGate, self).__init__(exponent=exponent)

    @property
    def half_turns(self):
        return self._exponent

    def _eigen_components(self):
        return [
            (-0.5, numpy.diag([1, 0, 0, 1])),
            (0.5, numpy.diag([0, 1, 1, 0])),
        ]

    def _canonical_exponent_period(self):
        return 2

    def _with_exponent(self,
                       exponent):
        return ZZGate(half_turns=exponent)

    def text_diagram_info(self, args
                          ):
        return cirq.TextDiagramInfo(
            wire_symbols=(u'Z', u'Z'),
            exponent=self.half_turns)

    def __repr__(self):
        if self.half_turns == 1:
            return u'ZZ'
        return u'ZZ**{!r}'.format(self.half_turns)


FSWAP = FermionicSwapGate()
XXYY = XXYYGate()
YXXY = YXXYGate()
ZZ = ZZGate()
