from math import sqrt
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

    def __init__(self,
                 name,
                 idle_time=(0., 0.),
                 ridership=(0., 0.),
                 platforms=2,
                 rails=2,
                 natural_light=False):

        # name (used in substring matching)
        self.name = name

        # Gaussian features. Need VARIANCE VALUES!
        self.main_colour = None
        self.secondary_colour = None
        self.idle_time = idle_time
        self.ridership = ridership

        # Classification features.
        self.natural_light = natural_light
        self.platforms = platforms
        self.rails = rails

        # Potential next stations.
        self.connections = []

    def connect(self, other):
        self.connections.append(other)
        other.connections.append(self)

    def generate_observation(self):
        idle_time = gauss(self.idle_time[0], sqrt(self.idle_time[1]))
        ridership = gauss(self.ridership[0], sqrt(self.ridership[1]))
        return idle_time, ridership
