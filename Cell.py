import math
import random
import numpy as np
import pygame

from Organism import Organism


def generateID():
    i = 0
    while True:
        yield i
        i += 1


class Cell(Organism):
    def __init__(self, position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor, generation,
                 speed, direction, consumptionSpeed, requiredNutrientsPerCycle, maxSpeed=(1, 1)):
        super().__init__(position, nutrients, size, growthThreshold, resistance, primaryColor, secondaryColor)
        self.id = next(generateID())
        self.generation = generation
        self.speed = speed
        self.direction = np.array(direction, dtype='float64')
        self.consumptionSpeed = consumptionSpeed
        self.requiredNutrientsPerCycle = requiredNutrientsPerCycle
        self.maxSpeed = maxSpeed

    def update(self):
        pass

    def move(self,cells, height, width):
        direct = np.array((random.uniform(-self.speed, self.speed), random.uniform(-self.speed, self.speed)))
        self.direction += direct
        if abs(self.direction[0]) + abs(self.direction[1]) > self.maxSpeed[0] + self.maxSpeed[1]:
            self.direction = [(a / abs(a)) * b for a, b in zip(self.direction, self.maxSpeed)]
        self.position += self.direction

        for c in cells:
            if c is not self:
                dist = math.hypot(c.position[0] - self.position[0], c.position[1] - self.position[1])
                if dist-c.size < self.size:
                    factor = (self.size+c.size)-dist
                    vec = (c.position-self.position)*factor
                    self.eat(c)


        # screen boundary detection
        if self.position[0] < 0:
            self.position[0] = 0
            self.direction[0] = -self.direction[0]
        if self.position[0] > width - self.size:
            self.position[0] = width - self.size
            self.direction[0] = -self.direction[0]

        if self.position[1] < 0:
            self.position[1] = 0
            self.direction[1] = -self.direction[1]
        if self.position[1] > height - self.size:
            self.position[1] = height - self.size
            self.direction[1] = -self.direction[1]

    def eat(self,cell):
        cell.nutrients = cell.nutrients-self.consumptionSpeed
        self.nutrients += self.consumptionSpeed

    def draw(self, screen):
        pygame.draw.circle(screen, self.primaryColor, self.position, self.size, width=0)
        pygame.draw.circle(screen, self.secondaryColor, self.position, self.size, width=3)

    def reproduce(self, organismList):
        pass
