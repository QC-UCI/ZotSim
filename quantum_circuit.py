# quantum_circuit.py

import numpy as np


# TODO: make a base simulator abstract class
class BasicSimulator:
    def __init__(self, qc: QuantumCircuit):
        # quantum circuit we want to run
        self.qc = qc

        # construct our statevector which is an array of the amplitudes of our quantum state
        # these amplitudes can be negative 
        self.state = np.array(2 ** self.qreg.qubits)
        self.state[0] = 1.0

    def run(self, shots: int = 1024):
        pass

    def _apply_full(self, unitary: np.array):
        assert len(unitary.shape) == 2
        assert 2 ** self.qreg.qubits == unitary.shape[0]
        assert 2 ** self.qreg.qubits == unitary.shape[1]

        # apply the unitary gate to the state
        self.state = unitary @ self.state 


# holds the unitary for a gate
class Gate:
    def __init__(self):
        pass


class QuantumCircuit:
    def __init__(self, qreg: QuantumRegister, creg: ClassicalRegister):
        self.qreg = qreg
        self.creg = creg

        self.gates = []


    def apply(self, gate: Gate):
        pass

    





class QuantumRegister:
    def __init__(self, qubits: int):
        self.qubits = qubits


class ClassicalRegister:
    def __init__(self, bit: int):
        self.bits = bits


