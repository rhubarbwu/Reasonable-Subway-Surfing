from lib.data.station import *
from lib.data.toronto import *
from lib.model import *


def print_beautify(curr_ll, k):
    states = zip(Network, curr_ll)

    top_k = sorted(states, key=lambda x: -x[1])
    print()
    for i in range(k):
        print(top_k[i][0].name, top_k[i][1])


def run_simulation_top_k(stations, k, conn_const, verbose=False):
    PAM = build_probabilistic_adjacency(Network, 2)

    observations = [s.generate_observation() for s in stations]
    ll = execute_simulation(observations, Network, PAM, verbose)

    if verbose:
        for curr_ll in ll:
            print_beautify(curr_ll, k)

    return ll


def line_1_vaughan_to_finch():
    stations = Line1
    k = 5
    conn_const = 1
    run_simulation_top_k(stations, k, conn_const)


if __name__ == "__main__":
    line_1_vaughan_to_finch()
    # stgeorge_spadina_cycle()