from Organism import Organism


class Food(Organism):

    def __init__(self, position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor):
        super().__init__(position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor)

    def update(self):
        pass

    def draw(self, screen):
        pass

    def reproduce(self, organismList):
        pass