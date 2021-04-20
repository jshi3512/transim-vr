import pygame
import random
import time
import math

class OscillatingCircle():
    def __init__(self, display, color, x, y, max_radius, freq):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.max_radius = max_radius
        self.freq = freq

    def display_circle(self, ticks):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.max_radius*(math.sin(self.freq*math.pi*ticks/30)+1)/2, width=1)

