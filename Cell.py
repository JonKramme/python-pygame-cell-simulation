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
    def __init__(self, position, primaryColor, secondaryColor, nutrients=200, size=2, resistance=random.randint(0, 10),
                 generation=0, speed=0.5, direction=(0, 0), growthThreshold=random.randint(15, 30),
                 consumptionSpeed=random.randint(5, 10), requiredNutrientsPerCycle=50,
                 reproductionSizeThreshold=random.randint(15, 30), maxSpeed=(1, 1)):
        super().__init__(position, primaryColor, secondaryColor, nutrients, size, resistance, reproductionSizeThreshold)
        self.id = next(generateID())
        self.generation = generation
        self.speed = speed
        self.direction = np.array(direction, dtype='float64')
        self.growthThreshold = growthThreshold
        self.consumptionAmount = consumptionSpeed
        self.requiredNutrientsPerCycle = requiredNutrientsPerCycle
        self.maxSpeed = maxSpeed
        self.age = 0

    def update(self, screen, cells, height, width):
        self.liveOrDie(cells)
        self.move(cells, height, width)
        collisions = self.checkCollisions(cells)
        if len(collisions) > 0:
            self.eat(collisions[random.randint(0, len(collisions) - 1)])  # eat from a random overlappping cell
        self.reproduce(cells)
        self.grow()
        self.draw(screen)

    def liveOrDie(self, cells: list):
        if self.nutrients < self.requiredNutrientsPerCycle:
            cells.remove(self)
        #self.nutrients -= self.requiredNutrientsPerCycle
        self.age += 1

    def move(self, cells, height, width):
        direct = np.array((random.uniform(-self.speed, self.speed), random.uniform(-self.speed, self.speed)))
        self.direction += direct
        if abs(self.direction[0]) + abs(self.direction[1]) > self.maxSpeed[0] + self.maxSpeed[1]:
            self.direction = [(a / abs(a)) * b for a, b in zip(self.direction, self.maxSpeed)]
        self.position += self.direction

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

    def checkCollisions(self, cells):
        collisions = list()
        for c in cells:
            if c is not self:
                dist = math.hypot(c.position[0] - self.position[0], c.position[1] - self.position[1])
                if dist - c.size < self.size:
                    collisions.append(c)
        return collisions

    def grow(self):
        if self.nutrients > self.growthThreshold*self.size:
            self.size += 1
            #self.nutrients -= self.growthThreshold

    def eat(self, cell):
        food = -cell.resistance # init as negative resistance to lower the amount of "food" added/taken away
        food += cell.nutrients if cell.nutrients < self.consumptionAmount else self.consumptionAmount
        cell.nutrients -= food
        self.nutrients += food

    def draw(self, screen):
        pygame.draw.circle(screen, self.primaryColor, self.position, self.size, width=0)
        pygame.draw.circle(screen, self.secondaryColor, self.position, self.size, width=3)

    def reproduce(self, organismList):
        if self.size >= self.reproductionSizeThreshold and self.nutrients > self.requiredNutrientsPerCycle * 2:
            self.nutrients = self.nutrients / 2
            self.size = self.size / 2
            organismList.append(
                Cell(self.position, self.primaryColor, self.secondaryColor,
                     nutrients=self.nutrients, size=self.size, growthThreshold=self.growthThreshold,
                     resistance=self.resistance, generation=self.generation + 1, speed=self.speed,
                     consumptionSpeed=self.consumptionAmount, requiredNutrientsPerCycle=self.requiredNutrientsPerCycle,
                     reproductionSizeThreshold=self.reproductionSizeThreshold, maxSpeed=self.maxSpeed)
            )
