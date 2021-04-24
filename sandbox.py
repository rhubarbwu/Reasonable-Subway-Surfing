from lib.data import lines
from lib.data.toronto import *
from lib.model.display import rewrap
from lib.model.filter import run_simulation_top_k
from lib.model.adjacency import build_probabilistic_adjacency

stations = [Kipling[0], Islington[0], Islington[1]]

k = 5

ll = run_simulation_top_k(stations, k, verbose=True)

PAM = build_probabilistic_adjacency(Network)
