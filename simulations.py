from lib.data.station import *
from lib.data.toronto import *
from lib.model import *


def generate_observations_on_line(line, start, end):
    return [line[i].generate_observation() for i in range(start, end)]


def line_1_vaughan_to_finch():
    line = Line1
    observations = generate_observations_on_line(Line1, 1, len(Line1))
    execute_simulation(observations, Line1)


def line_1_stgeorge_to_bloor():
    start = Line1.index(Osgoode)
    end = Line1.index(Finch)
    observations = generate_observations_on_line(Line1, start, end)
    execute_simulation(observations, Line1)


if __name__ == "__main__":
    line_1_vaughan_to_finch()
    line_1_stgeorge_to_bloor()