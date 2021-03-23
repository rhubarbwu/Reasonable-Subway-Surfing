class Train:
    """
    direction: (rough) cardinal direction the train is facing
    length: number of train cars coupled
    occupancy: number of occupants
    """

    def __init__(self, direction, length=6, occupancy=150):
        self.direction = direction
        self.length = length
        self.occupancy = occupancy
