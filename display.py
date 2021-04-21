import pygame
import time

class Display():
    def __init__(self, width, height, bgrd):
        self.width = width
        self.height = height
        self.bgrd = bgrd
        pygame.init() #initialize pygame, creates display instance
        self.display = pygame.display.set_mode((self.width, self.height), flags=pygame.DOUBLEBUF) #DOUBLEBUF used for hardware rendering
        self.clock = pygame.time.Clock()

    def run_oscillating(self, osc, fps):
        running = True
        ticks = 0

        while running:
            ticks = ticks + 1
            self.display.fill(self.bgrd)

            osc.display_circle(ticks)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(fps)


    def run_dots(self, dots):
        running = True

        while running:
            self.display.fill(self.bgrd)
            dots.display_circle()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            time.sleep(1)

            pygame.display.flip()


    def get_display(self):
        return self.display

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
