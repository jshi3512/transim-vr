import pygame
import random


class MovingDots():
    def __init__(self, display, color, width, y, radius):
        self.display = display
        self.color = color
        self.width = width
        self.y = y
        self.radius = radius

    #draws circle to screen
    def display_circle(self):
        pygame.draw.circle(self.display, self.color, (random.randint(0,self.width), self.y), self.radius)

