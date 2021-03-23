class Station:
    """
    name: name of the station
    depth: how deep below the surface the station is
    idle_time: amount of time spent at this station
    train: the train object in the observation
    waiting: number of passengers waiting on the platform

    natural_light: whether or not the platform has natural light
    platforms: number of platforms
    rails: number of rails
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
