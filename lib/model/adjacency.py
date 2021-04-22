import numpy as np


def build_probabilistic_adjacency(stations, conn_const):
    n = len(stations)
    prob_adj_matrix = np.zeros((n, n))
    for i in range(n):
        stn_i = stations[i]
        conns = max(2, len(stn_i.connections))
        weight = conn_const * conns + 1

        for j in range(1, n):
            stn_j = stations[j]
            if stn_i in stn_j.connections:
                prob_adj_matrix[i][j] = 2 / weight
                prob_adj_matrix[j][i] = 2 / weight

        prob_adj_matrix[i][i] = 1 / weight

    return prob_adj_matrix
