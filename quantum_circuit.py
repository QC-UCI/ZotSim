# quantum_circuit.py

import numpy as np


# TODO: make a base simulator abstract class
class BasicSimulator:
    def __init__(self, qc: "QuantumCircuit"):
        # quantum circuit we want to run
        self.qc = qc

        # construct our statevector which is an array of the amplitudes of our quantum state
        # these amplitudes can be negative 
        self.state = np.array(2 ** self.qreg.qubits)
        self.state[0] = 1.0

    def run(self, shots: int = 1024):
        pass

    def _apply_full(self, unitary: np.ndarray):
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
    def __init__(self, qreg: "QuantumRegister", creg: "ClassicalRegister"):
        self.qreg = qreg
        self.creg = creg

        # list of gates and the list of qubit indices they are applying to
        self.gates: list[tuple] = []


    def apply(self, gate: Gate, qubits: list[int]):
        self.gates.append((gate, qubits))
    





class QuantumRegister:
    def __init__(self, qubits: int):
        self.qubits = qubits


class ClassicalRegister:
    def __init__(self, bits: int):
        self.bits = bin(bits)


class Gate:
    def __init__(self, qubits: int, amplitudes: np.ndarray):
        assert len(amplitudes.shape) == 2, "Amplitude array should be 2 dimensional"
        assert amplitudes.shape[0] == 2 ** qubits
        assert amplitudes.shape[1] == 2 ** qubits
        # TODO: make sure unitary
        self.qubits = qubits
        self.amplitudes = amplitudes

    def mult(self, other: "Gate") -> Gate:
        assert self.qubits == other.qubits
        new_gate_amplitudes = self.amplitudes @ other.amplitudes
        return Gate(self.qubits, new_gate_amplitudes)

    def __matmul__(self, other):
        if not isinstance(other, Gate):
            raise ValueError(f"Cannot mulitply gate by {type(other)}")
        return self.mult(other)
    
    def tensor(self, other: "Gate"):
        new_gate_amplitudes = np.kron(self.amplitudes, other.amplitudes)
        new_gate_qubits = self.qubits + other.qubits
        return Gate(new_gate_qubits, new_gate_amplitudes)

    def i():
        id_gate = Gate(1, np.array([[1., 0.], [0., 1.]]))
        return id_gate

    def x():
        x_gate = Gate(1, np.array([[0., 1.], [1., 0.]]))
        return x_gate
    
    def z():
        z_gate = Gate(1, np.array([[1., 0.], [0., -1.]]))
        return z_gate
    
    def h():
        h_gate = Gate(1, (1 / np.sqrt(2)) * np.array([[1., 1.], [1., -1.]]))
        return h_gate
    
