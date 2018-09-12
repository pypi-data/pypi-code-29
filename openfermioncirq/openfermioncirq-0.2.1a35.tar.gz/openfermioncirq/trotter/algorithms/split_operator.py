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

"""A Trotter algorithm using a split-operator approach."""

from typing import Optional, Sequence, Tuple

import cirq
from openfermion import DiagonalCoulombHamiltonian, QuadraticHamiltonian

from openfermioncirq import Rot111Gate, bogoliubov_transform, swap_network

from openfermioncirq.trotter.trotter_algorithm import (
        Hamiltonian,
        TrotterStep,
        TrotterAlgorithm)


class SplitOperatorTrotterAlgorithm(TrotterAlgorithm):
    """A Trotter algorithm using a split-operator approach.

    This algorithm simulates a DiagonalCoulombHamiltonian. It uses Bogoliubov
    transformations to switch between a basis in which the one-body terms are
    convenient to simulate and a basis in which the two-body terms are
    convenient to simulate. The Bogoliubov transformations are implemented
    using Givens rotations.

    This algorithm is described in arXiv:1706.00023.
    """
    # TODO Maybe use FFFT

    supported_types = {DiagonalCoulombHamiltonian}

    def symmetric(self, hamiltonian: Hamiltonian) -> Optional[TrotterStep]:
        return SymmetricSplitOperatorTrotterStep(hamiltonian)

    def asymmetric(self, hamiltonian: Hamiltonian) -> Optional[TrotterStep]:
        return AsymmetricSplitOperatorTrotterStep(hamiltonian)

    def controlled_symmetric(self, hamiltonian: Hamiltonian
                             ) -> Optional[TrotterStep]:
        return ControlledSymmetricSplitOperatorTrotterStep(hamiltonian)

    def controlled_asymmetric(self, hamiltonian: Hamiltonian
                              ) -> Optional[TrotterStep]:
        return ControlledAsymmetricSplitOperatorTrotterStep(hamiltonian)


SPLIT_OPERATOR = SplitOperatorTrotterAlgorithm()


class SplitOperatorTrotterStep(TrotterStep):

    def __init__(self, hamiltonian: DiagonalCoulombHamiltonian) -> None:
        quad_ham = QuadraticHamiltonian(hamiltonian.one_body)
        # Get the coefficients of the one-body terms in the diagonalizing basis
        self.orbital_energies, _ = quad_ham.orbital_energies()
        # Get the basis change matrix that diagonalizes the one-body term
        self.basis_change_matrix = (
                quad_ham.diagonalizing_bogoliubov_transform())
        super().__init__(hamiltonian)


class SymmetricSplitOperatorTrotterStep(SplitOperatorTrotterStep):

    def prepare(self,
                qubits: Sequence[cirq.QubitId],
                control_qubits: Optional[cirq.QubitId]=None
                ) -> cirq.OP_TREE:
        # Change to the basis in which the one-body term is diagonal
        yield cirq.inverse(
                bogoliubov_transform(qubits, self.basis_change_matrix))

    def trotter_step(
            self,
            qubits: Sequence[cirq.QubitId],
            time: float,
            control_qubit: Optional[cirq.QubitId]=None
            ) -> cirq.OP_TREE:

        n_qubits = len(qubits)

        # Simulate the one-body terms for half of the full time
        yield (cirq.RotZGate(rads=
                   -0.5 * self.orbital_energies[i] * time).on(qubits[i])
               for i in range(n_qubits))

        # Rotate to the computational basis
        yield bogoliubov_transform(qubits, self.basis_change_matrix)

        # Simulate the two-body terms for the full time
        def two_body_interaction(p, q, a, b) -> cirq.OP_TREE:
            yield cirq.Rot11Gate(rads=
                    -2 * self.hamiltonian.two_body[p, q] * time).on(a, b)
        yield swap_network(qubits, two_body_interaction)
        # The qubit ordering has been reversed
        qubits = qubits[::-1]

        # Rotate back to the basis in which the one-body term is diagonal
        yield cirq.inverse(
                bogoliubov_transform(qubits, self.basis_change_matrix))

        # Simulate the one-body terms for half of the full time
        yield (cirq.RotZGate(rads=
                   -0.5 * self.orbital_energies[i] * time).on(qubits[i])
               for i in range(n_qubits))

    def step_qubit_permutation(self,
                               qubits: Sequence[cirq.QubitId],
                               control_qubit: Optional[cirq.QubitId]=None
                               ) -> Tuple[Sequence[cirq.QubitId],
                                          Optional[cirq.QubitId]]:
        # A Trotter step reverses the qubit ordering
        return qubits[::-1], None

    def finish(self,
               qubits: Sequence[cirq.QubitId],
               n_steps: int,
               control_qubit: Optional[cirq.QubitId]=None,
               omit_final_swaps: bool=False
               ) -> cirq.OP_TREE:
        # Rotate back to the computational basis
        yield bogoliubov_transform(
                qubits, self.basis_change_matrix)
        # If the number of Trotter steps is odd, possibly swap qubits back
        if n_steps & 1 and not omit_final_swaps:
            yield swap_network(qubits)


class ControlledSymmetricSplitOperatorTrotterStep(SplitOperatorTrotterStep):

    def prepare(self,
                qubits: Sequence[cirq.QubitId],
                control_qubits: Optional[cirq.QubitId]=None
                ) -> cirq.OP_TREE:
        # Change to the basis in which the one-body term is diagonal
        yield cirq.inverse(
                bogoliubov_transform(qubits, self.basis_change_matrix))

    def trotter_step(
            self,
            qubits: Sequence[cirq.QubitId],
            time: float,
            control_qubit: Optional[cirq.QubitId]=None
            ) -> cirq.OP_TREE:

        n_qubits = len(qubits)

        # Simulate the one-body terms for half of the full time
        yield (cirq.Rot11Gate(rads=
                   -0.5 * self.orbital_energies[i] * time).on(
                       control_qubit, qubits[i])
               for i in range(n_qubits))

        # Rotate to the computational basis
        yield bogoliubov_transform(qubits, self.basis_change_matrix)

        # Simulate the two-body terms for the full time
        def two_body_interaction(p, q, a, b) -> cirq.OP_TREE:
            yield Rot111Gate(rads=
                    -2 * self.hamiltonian.two_body[p, q] * time).on(
                            control_qubit, a, b)
        yield swap_network(qubits, two_body_interaction)
        # The qubit ordering has been reversed
        qubits = qubits[::-1]

        # Rotate back to the basis in which the one-body term is diagonal
        yield cirq.inverse(
                bogoliubov_transform(qubits, self.basis_change_matrix))

        # Simulate the one-body terms for half of the full time
        yield (cirq.Rot11Gate(rads=
                   -0.5 * self.orbital_energies[i] * time).on(
                       control_qubit, qubits[i])
               for i in range(n_qubits))

        # Apply phase from constant term
        yield cirq.RotZGate(rads=
                -self.hamiltonian.constant * time).on(control_qubit)

    def step_qubit_permutation(self,
                               qubits: Sequence[cirq.QubitId],
                               control_qubit: Optional[cirq.QubitId]=None
                               ) -> Tuple[Sequence[cirq.QubitId],
                                          Optional[cirq.QubitId]]:
        # A Trotter step reverses the qubit ordering
        return qubits[::-1], control_qubit

    def finish(self,
               qubits: Sequence[cirq.QubitId],
               n_steps: int,
               control_qubit: Optional[cirq.QubitId]=None,
               omit_final_swaps: bool=False
               ) -> cirq.OP_TREE:
        # Rotate back to the computational basis
        yield bogoliubov_transform(qubits, self.basis_change_matrix)
        # If the number of Trotter steps is odd, possibly swap qubits back
        if n_steps & 1 and not omit_final_swaps:
            yield swap_network(qubits)


class AsymmetricSplitOperatorTrotterStep(SplitOperatorTrotterStep):

    def trotter_step(
            self,
            qubits: Sequence[cirq.QubitId],
            time: float,
            control_qubit: Optional[cirq.QubitId]=None
            ) -> cirq.OP_TREE:

        n_qubits = len(qubits)

        # Simulate the two-body terms for the full time
        def two_body_interaction(p, q, a, b) -> cirq.OP_TREE:
            yield cirq.Rot11Gate(rads=
                    -2 * self.hamiltonian.two_body[p, q] * time).on(a, b)
        yield swap_network(qubits, two_body_interaction)
        # The qubit ordering has been reversed
        qubits = qubits[::-1]

        # Rotate to the basis in which the one-body term is diagonal
        yield cirq.inverse(
                bogoliubov_transform(qubits, self.basis_change_matrix))

        # Simulate the one-body terms for the full time
        yield (cirq.RotZGate(rads=
                   -self.orbital_energies[i] * time).on(qubits[i])
               for i in range(n_qubits))

        # Rotate back to the computational basis
        yield bogoliubov_transform(qubits, self.basis_change_matrix)

    def step_qubit_permutation(self,
                               qubits: Sequence[cirq.QubitId],
                               control_qubit: Optional[cirq.QubitId]=None
                               ) -> Tuple[Sequence[cirq.QubitId],
                                          Optional[cirq.QubitId]]:
        # A Trotter step reverses the qubit ordering
        return qubits[::-1], None

    def finish(self,
               qubits: Sequence[cirq.QubitId],
               n_steps: int,
               control_qubit: Optional[cirq.QubitId]=None,
               omit_final_swaps: bool=False
               ) -> cirq.OP_TREE:
        # If the number of Trotter steps is odd, possibly swap qubits back
        if n_steps & 1 and not omit_final_swaps:
            yield swap_network(qubits)


class ControlledAsymmetricSplitOperatorTrotterStep(SplitOperatorTrotterStep):

    def trotter_step(
            self,
            qubits: Sequence[cirq.QubitId],
            time: float,
            control_qubit: Optional[cirq.QubitId]=None
            ) -> cirq.OP_TREE:

        n_qubits = len(qubits)

        # Simulate the two-body terms for the full time
        def two_body_interaction(p, q, a, b) -> cirq.OP_TREE:
            yield Rot111Gate(rads=
                    -2 * self.hamiltonian.two_body[p, q] * time).on(
                            control_qubit, a, b)
        yield swap_network(qubits, two_body_interaction)
        # The qubit ordering has been reversed
        qubits = qubits[::-1]

        # Rotate to the basis in which the one-body term is diagonal
        yield cirq.inverse(
                bogoliubov_transform(qubits, self.basis_change_matrix))

        # Simulate the one-body terms for the full time
        yield (cirq.Rot11Gate(rads=
                   -self.orbital_energies[i] * time).on(
                       control_qubit, qubits[i])
               for i in range(n_qubits))

        # Rotate back to the computational basis
        yield bogoliubov_transform(qubits, self.basis_change_matrix)

        # Apply phase from constant term
        yield cirq.RotZGate(rads=
                -self.hamiltonian.constant * time).on(control_qubit)

    def step_qubit_permutation(self,
                               qubits: Sequence[cirq.QubitId],
                               control_qubit: Optional[cirq.QubitId]=None
                               ) -> Tuple[Sequence[cirq.QubitId],
                                          Optional[cirq.QubitId]]:
        # A Trotter step reverses the qubit ordering
        return qubits[::-1], control_qubit

    def finish(self,
               qubits: Sequence[cirq.QubitId],
               n_steps: int,
               control_qubit: Optional[cirq.QubitId]=None,
               omit_final_swaps: bool=False
               ) -> cirq.OP_TREE:
        # If the number of Trotter steps is odd, possibly swap qubits back
        if n_steps & 1 and not omit_final_swaps:
            yield swap_network(qubits)
