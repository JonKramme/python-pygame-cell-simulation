import math
import random

import numpy as np
import pygame

from Organism import Organism


class Food(Organism):

    def __init__(self, position, primaryColor, secondaryColor, nutrients=200, resistance=0,reproductionSizeThreshold=25
                 ,canGrow=True):
        super().__init__(position, primaryColor, secondaryColor, nutrients, self.calc_size(nutrients), resistance,
                         reproductionSizeThreshold)
        self.baseGrowthAmount = 5
        self.growthTimer = 2
        self.counter = 0
        self.canGrow = canGrow

    def update(self,screen,cells, height, width):
        if self.nutrients <= 0:
            cells.remove(self)
        if self.canGrow:
            self.grow()
        self.size = self.calc_size(self.nutrients)
        self.reproduce(cells)
        self.draw(screen)

    @staticmethod
    def calc_size(nutrients):
        return math.ceil(nutrients/100)

    def grow(self):
        if self.counter <= 0:
            self.nutrients += self.baseGrowthAmount+self.size
            self.counter = self.growthTimer
        else:
            self.counter -= 1


    def draw(self, screen):
        points = ((self.position[0]+1*self.size, self.position[1]), (self.position[0], self.position[1]+1*self.size),
                  (self.position[0]-1*self.size, self.position[1]), (self.position[0], self.position[1]-1*self.size))
        pygame.draw.polygon(screen, self.primaryColor, points)
        pygame.draw.lines(screen, self.secondaryColor, True, points, 3)

    def reproduce(self, organismList):
        if self.size >= self.reproductionSizeThreshold:
            self.nutrients = self.nutrients / 2
            self.size = self.size / 2
            tmp = random.uniform(0, self.reproductionSizeThreshold*2)
            direct = np.array((tmp, self.reproductionSizeThreshold*2-tmp),dtype="float64")

            organismList.append(
                Food(self.position+direct, self.primaryColor, self.secondaryColor,
                     nutrients=self.nutrients, resistance=self.resistance,
                     reproductionSizeThreshold=self.reproductionSizeThreshold)
            )
