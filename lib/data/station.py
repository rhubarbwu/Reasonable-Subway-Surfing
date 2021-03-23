class Station:
    """
    name (string): name of the station
    depth (float): how deep below the surface the station is, in metres
    idle_time (float): amount of time spent at this station, in seconds
    train (Train): the train object in the observation
    waiting (int): number of passengers waiting on the platform

    natural_light (bool): whether or not the platform has natural light
    platforms (int): number of platforms
    rails (int): number of rails
    """

    def __init__(self,
                 name,
                 depth,
                 idle_time,
                 train,
                 waiting,
                 natural_light=False,
                 platforms=2,
                 rails=2):

        self.name = name

        self.depth = depth
        self.idle_time = idle_time
        self.train = train
        self.waiting = waiting

        self.natural_light = natural_light
        self.platforms = platforms
        self.rails = rails
