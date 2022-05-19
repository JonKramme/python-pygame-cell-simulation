import pygame

from Organism import Organism


class Food(Organism):

    def __init__(self, position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor):
        super().__init__(position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor)

    def update(self):
        pass

    def draw(self, screen):
        points = ((self.position[0]+1*self.size, self.position[1]), (self.position[0], self.position[1]+1*self.size),
                  (self.position[0]-1*self.size, self.position[1]), (self.position[0], self.position[1]-1*self.size))
        pygame.draw.polygon(screen, self.primaryColor, points)
        pygame.draw.lines(screen, self.secondaryColor, True, points,3)

    def reproduce(self, organismList):
        pass
