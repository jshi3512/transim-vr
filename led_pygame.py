import pygame
import random
import time

def draw_circle(screen,color,x,y,radius):
    # this function draws/creates the circle, 
    # the screen variable tells the circle what screen to be drawn to. 
    # the color variable sets the color the radius variable sets how large of a circle will be.
    pygame.draw.circle(screen,(0,255,0),(x,y),radius)

pygame.init()
width = 1570
height = 800
screen = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
# main program loop
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0,0,0))

    time.sleep(1)

    # Draw the circles
    draw_circle(screen,(0,255,0),random.randint(0,width), 400,20)

    # Flip the display
    pygame.display.flip()