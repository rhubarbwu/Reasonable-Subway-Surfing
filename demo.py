from lib.model.filter import run_simulation_top_k
from test.simulations import simulations
import sys

experiment = sys.argv[1]
k, conn_const = 5, 1
if len(sys.argv) > 2:
    k = int(sys.argv[2])
if len(sys.argv) > 3:
    conn_const = int(sys.argv[3])

stations = simulations[experiment]

output_dir = "images"
output_dir = None
ll = run_simulation_top_k(stations, k, verbose=True, output_dir=output_dir)
