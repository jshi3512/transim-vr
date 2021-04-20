import pygame

class Display():
    def __init__(self, width, height, bgrd):
        self.width = width
        self.height = height
        self.bgrd = bgrd
        pygame.init()
        self.display = pygame.display.set_mode((self.width, self.height), flags=pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

    def update_display(self):
        self.display.fill(self.bgrd)

    def get_display(self):
        return self.display

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_clock(self):
        return self.clock