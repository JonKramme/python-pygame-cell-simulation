import pygame

from Organism import Organism


def generateID():
    i = 0
    while True:
        yield i
        i += 1


class Cell(Organism):
    def __init__(self, position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor, generation,
                 speed, direction, consumptionSpeed, requiredNutrientsPerCycle):
        super().__init__(position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor)
        self.id = next(generateID())
        self.generation = generation
        self.speed = speed
        self.direction = direction
        self.consumptionSPeed = consumptionSpeed
        self.requiredNutrientsPerCycle = requiredNutrientsPerCycle

    def update(self):
        pass

    def move(self):
        pass

    def eat(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen,self.primaryColor,self.position,self.size,width=0)
        pygame.draw.circle(screen, self.secondaryColor,self.position,self.size,width=3)

    def reproduce(self, organismList):
        pass
