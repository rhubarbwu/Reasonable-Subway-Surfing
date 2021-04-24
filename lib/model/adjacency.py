import numpy as np
from lib.data.toronto import *
from .hparams import *


def build_probabilistic_adjacency(stations):
    n = len(stations)
    prob_adj_matrix = np.zeros((n, n))
    for i in range(n):
        stn_i = stations[i]
        total_weight = compute_weight(stn_i)

        for j in range(n):
            stn_j = stations[j]

            def compute_matrix_val(connection, weight):
                if stn_j == connection:
                    prob_adj_matrix[i][j] = weight / total_weight
                    prob_adj_matrix[j][i] = weight / total_weight

            compute_matrix_val(stn_i.backward, backward)
            compute_matrix_val(stn_i.forward, forward)
            compute_matrix_val(stn_i.opposite, opposite)
            for t in stn_i.transfers:
                compute_matrix_val(t, transfer)

        prob_adj_matrix[i][i] = 1 / total_weight

    return prob_adj_matrix


def compute_weight(station):
    weight = 1
    if station.backward:
        weight += backward
    if station.forward:
        weight += forward
    if station.opposite:
        weight += opposite
    weight += len(station.transfers) * transfer
    return weight
