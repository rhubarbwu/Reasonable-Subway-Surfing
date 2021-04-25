from lib.model.filter import run_simulation_top_k
from test.simulations import simulations
from os import mkdir, path
import sys

experiment = sys.argv[1]
output_dir = "experiments/{}".format(experiment)
if not path.exists(output_dir):
    mkdir(output_dir)

stations = simulations[experiment]
ll = run_simulation_top_k(stations, 5, output_dir, verbose=True)
