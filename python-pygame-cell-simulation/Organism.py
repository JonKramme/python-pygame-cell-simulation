from abc import ABC, abstractmethod

import numpy as np
import pygame


class Organism(ABC):
    def __init__(self, position, primaryColor, secondaryColor, nutrients, size, resistance, reproductionSizeThreshold):
        self.position = np.array(position, dtype='float64')
        self.nutrients = nutrients
        self.size = size
        self.resistance = resistance
        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor
        self.reproductionSizeThreshold = reproductionSizeThreshold

    @abstractmethod
    def update(self, screen, cells, height, width):
        pass

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 220), self.position.dtype('int64'), self.size)


    @abstractmethod
    def reproduce(self, organismList):
        pass
