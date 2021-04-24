from lib.data import lines
from lib.data.toronto import *
from lib.model.display import rewrap
from lib.model.filter import run_simulation_top_k
from lib.model.adjacency import build_probabilistic_adjacency

stations = [
    StGeorge2[0], Bay[0], BloorYonge2[0], BloorYonge1[0], Wellesley[0],
    College[0], Dundas[0], Queen[0], King[0], Union[0], StAndrew[0], Osgoode[0],
    StPatrick[0], QueensPark[0], Museum[0], StGeorge1[0], StGeorge1[1]
]

k = 5

ll = run_simulation_top_k(stations, k, verbose=True)
