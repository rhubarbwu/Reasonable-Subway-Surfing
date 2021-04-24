from ..data.toronto import Network, NetworkWrapped, TerminusIndices

import numpy as np


def print_beautify(station, observation, curr_ll, k):
    states = zip(NetworkWrapped, curr_ll)

    top_k = sorted(states, key=lambda x: -x[1])
    print("\nAt {} with idle time of {}s, and {} patrons, estimations:".format(
        station.name, round(observation[0], 2), round(observation[1])))
    for i in range(k):
        print("\t", top_k[i][0].name, top_k[i][1])


def rewrap(ll):
    wrapped_ll = ll[:, 0:1]
    index = 1
    while index < ll.shape[1]:
        new = ll[:, index:index + 1]

        if index not in TerminusIndices:
            index += 1
            new += ll[:, index:index + 1]
        index += 1

        wrapped_ll = np.concatenate((wrapped_ll, new), axis=1)

    return wrapped_ll
