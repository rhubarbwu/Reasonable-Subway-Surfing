from lib.data.toronto import *

import random

StGeorgeSpadinaStations = [StGeorge1, StGeorge2, Spadina2, Spadina1]


def generate_cycle(stations):
    shift = random.randint(0, len(stations) - 1)
    if random.randint(0, 1) == 1:
        stations = stations[::-1]
    stations = stations[shift:] + stations[:shift]
    return stations


simulations = {
    "line_1": Line1,
    "stgeorge_spadina_cycle": generate_cycle(StGeorgeSpadinaStations),
}