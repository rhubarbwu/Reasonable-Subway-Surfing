from lib.lib import *
from test.simulations import simulations
from visualize_likelihood import show_likelihoods
import sys

experiment = sys.argv[1]
k, conn_const = 5, 1
if len(sys.argv) > 2:
    k = int(sys.argv[2])
if len(sys.argv) > 3:
    conn_const = int(sys.argv[3])

stations = simulations[experiment]

ll=run_simulation_top_k(stations, k, conn_const, verbose=True)

show_likelihoods(ll)
