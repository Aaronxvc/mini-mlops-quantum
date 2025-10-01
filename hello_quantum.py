"""
This is showing a HGATE = putting qubit in superposition

q: ┤ H ├
"""


from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
print(qc)