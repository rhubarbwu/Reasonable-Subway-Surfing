from lib.data.station import *
from lib.data.toronto import *
from lib.model import *


def print_beautify(station, observation, curr_ll, k):
    states = zip(Network, curr_ll)

    top_k = sorted(states, key=lambda x: -x[1])
    print("\nAt {} with idle time of {}s, and {} patrons, estimations:".format(
        station.name, round(observation[0], 2), round(observation[1])))
    for i in range(k):
        print("\t", top_k[i][0].name, top_k[i][1])


def run_simulation_top_k(stations, k, conn_const, verbose=False):
    PAM = build_probabilistic_adjacency(Network, 2)

    observations = [s.generate_observation() for s in stations]
    ll = execute_simulation(observations, Network, PAM, verbose)

    if verbose:
        for i in range(len(stations)):
            print_beautify(stations[i], observations[i], ll[i + 1], k)

    return ll