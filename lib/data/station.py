import math
from random import gauss

MINUTE = 60


class Station:
    """
    name (string): name of the station
    idle_time (float, float): mean and variance of amount of time spent
        at this station, in seconds.
    ridership (float, float): mean and variance of ridership per period.

    natural_light (bool): whether or not the platform has natural light
    platforms (int): number of platforms
    rails (int): number of rails
    """

    def __init__(self, name, idle_time=(0., 0.), ridership=(0., 0.)):

        # name (used in substring matching)
        self.name = name

        # Gaussian features. Need VARIANCE VALUES!
        assert (len(idle_time) == 2)
        assert (len(ridership) == 2)
        self.idle_time = idle_time
        self.ridership = ridership

        # Potential next stations.
        self.backward = None
        self.forward = None
        self.opposite = None
        self.transfers = []

    def generate_observation(self):
        idle_time = gauss(self.idle_time[0], self.idle_time[1])
        ridership = gauss(self.ridership[0], self.ridership[1])
        return max(0., idle_time), int(max(0., ridership))

    def probability_of_observation(self, idle_time, ridership):

        def normpdf(x, mean, sd):
            var = sd**2
            denom = (2 * math.pi * var)**.5
            num = math.exp(-(x - mean)**2 / (2 * var))
            return num / denom

        p1 = normpdf(idle_time, self.idle_time[0], self.idle_time[1])
        p2 = normpdf(ridership, self.ridership[0], self.ridership[1])
        return p1 * p2


def connect_transfer(stations_1, stations_2):
    for s1 in stations_1:
        for s2 in stations_2:
            s1.transfers.append(s2)
            s2.transfers.append(s1)
