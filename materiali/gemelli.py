# La moneta che gira · capitolo 12, paragrafo 12.1
# L'«Hello World» dei computer quantistici: la ricetta dei gemelli.
# Per farlo girare:  pip install qiskit qiskit-aer   e poi   python gemelli.py

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)     # due monete, ferme su testa
qc.h(0)                    # la prima comincia a girare
qc.cx(0, 1)                # CNOT: le due diventano gemelle
qc.measure_all()           # la mano: si fermano entrambe

risultato = AerSimulator().run(qc, shots=1000).result()
print(risultato.get_counts())
