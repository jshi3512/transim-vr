import pygame
import random
import time
import math
def draw_circle(screen,color,x,y,radius):
    # this function draws/creates the circle, 
    # the screen variable tells the circle what screen to be drawn to. 
    # the color variable sets the color the radius variable sets how large of a circle will be.
    pygame.draw.circle(screen,(0,255,0),(x,y),radius,width =1)

pygame.init()
width = 1570
height = 800
screen = pygame.display.set_mode((width,height),flags=pygame.DOUBLEBUF)
running = True
count = 0;
clock = pygame.time.Clock()
FPS = 60
max_radius=400
period = 200

# main program loop
while running:
    count = count + 1;
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0,0,0))

    # Draw the circles
    draw_circle(screen,(0,255,0),width/2, 400,max_radius*math.sin((math.pi/(2*period))*count))

    # Flip the display
    pygame.display.flip()
    #lock.tick()
    #print("fps: ",clock.get_fps())