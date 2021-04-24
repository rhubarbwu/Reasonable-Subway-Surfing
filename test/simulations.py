from lib.data.toronto import *

import random


def generate_cycle(stations):
    shift = random.randint(0, len(stations) - 1)
    if random.randint(0, 1) == 1:
        stations = stations[::-1]
    stations = stations[shift:] + stations[:shift]
    return stations


simulations = {
    "line_1": Line1Wrapped[:],
    "line_2": Line2Wrapped[:],
    "line_3": Line2Wrapped[:],
    "line_4": Line2Wrapped[:],
}