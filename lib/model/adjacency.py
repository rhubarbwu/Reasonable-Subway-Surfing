import numpy as np
from lib.data.toronto import *


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

if __name__ == "__main__":
    PAM = build_probabilistic_adjacency(Network, 2)
    #print(PAM[:20,:20])
    for row in PAM[:20,:20]:
        print(list(row))
