from lib.lib import *
from test.simulations import simulations

import sys

experiment = sys.argv[1]
k, conn_const = 5, 1
if len(sys.argv) > 2:
    k = int(sys.argv[2])
if len(sys.argv) > 3:
    conn_const = int(sys.argv[3])

stations = simulations[experiment]

run_simulation_top_k(stations, k, conn_const, verbose=True)