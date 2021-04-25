from lib.data.toronto import *

import random


def generate_cycle(stations):
    shift = random.randint(0, len(stations) - 1)
    if random.randint(0, 1) == 1:
        stations = stations[::-1]
    stations = stations[shift:] + stations[:shift]
    return stations


simulations = {
    # Normal experiments.
    "line_1":
        Line1Wrapped[:],
    "line_2":
        Line2Wrapped[:],
    "line_3":
        Line3Wrapped[:],
    "line_4":
        Line4Wrapped[:],
    "line_1_interior":
        Line1Wrapped[1:-1],
    "line_2_interior":
        Line2Wrapped[1:-1],
    "line_3_interior":
        Line3Wrapped[1:-1],
    "line_4_interior":
        Line4Wrapped[1:-1],

    # More interesting experiments.
    "around_kennedy_3": [
        LawrenceEast[1],
        Kennedy3[0],
        LawrenceEast[0],
        Ellesmere[0],
    ],
    "around_stgeorge": [Spadina2[0], StGeorge2[0], StGeorge1[1], Spadina1[1]],
    "around_union": [
        StAndrew[0],
        Union[0],
        StAndrew[1],
    ],
    "yorkville": [
        Sherbourne[1], BloorYonge2[1], Bay[1], BloorYonge2[0], Sherbourne[0],
        BloorYonge2[1], Bay[1], StGeorge2[1], Spadina2[1]
    ],
    "downtown_u": [
        # Museum[0],
        QueensPark[0],
        StPatrick[0],
        Osgoode[0],
        StAndrew[0],
        Union[0],
        King[0],
        Queen[0],
        Dundas[0],
    ],
}