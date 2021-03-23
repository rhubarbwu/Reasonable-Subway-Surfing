class Train:
    """
    direction (string): (rough) cardinal direction the train is facing
    length (int): number of train cars coupled
    occupancy (int): number of occupants
    """

    def __init__(self, direction, length=6, occupancy=150):
        self.direction = direction
        self.length = length
        self.occupancy = occupancy
