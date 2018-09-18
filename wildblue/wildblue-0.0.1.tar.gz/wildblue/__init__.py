from blueqat.pauli import qubo_bit

def qubo_to_pauli(qubo):
    h = 0.0
    assert all(len(q) == len(qubo) for q in qubo)
    for i in range(len(qubo)):
        h += qubo_bit(i) * qubo[i][i]
        for j in range(i + 1, len(qubo)):
            h += qubo_bit(i)*qubo_bit(j) * (qubo[i][j] + qubo[j][i])
    return h
