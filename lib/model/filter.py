from .adjacency import build_probabilistic_adjacency
from .display import print_beautify, rewrap
from ..data.toronto import Network
from ..visualization.likelihood import show_likelihoods

import numpy as np


def run_simulation_top_k(path, k, output_dir, verbose=False):
    PAM = build_probabilistic_adjacency(Network)

    observations = [s.generate_observation() for s in path]
    ll = execute_simulation(observations, Network, PAM, verbose)
    ll = rewrap(ll)

    if verbose:
        for i in range(len(observations)):
            print_beautify(path[i], observations[i], ll[i + 1], k)
        print(output_dir)
        show_likelihoods("lib/visualization/images/ttc_map.jpg", ll, path,
                         observations, output_dir)

    return ll


def normalize(x):
    return x / np.sum(x)


def execute_simulation(observations, path, PAM, verbose=False):
    n = len(path)
    I = np.eye(n) / n
    ll = np.ndarray((len(observations) + 1, n))

    def update(state, observation, PAM):
        state = PAM @ state
        new_state = np.array([
            path[i].probability_of_observation(*observation) * state[i]
            for i in range(n)
        ])

        return normalize(new_state)

    ll[0] = normalize(np.ones((n)))

    for i in range(len(observations)):
        ll[i + 1] = update(ll[i], observations[i], PAM)
    return ll
