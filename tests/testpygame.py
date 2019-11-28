import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

def updateDisplay(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Camera')
    screen.fill(background_colour)

    pygame.display.flip()
    pygame.display.update()

running = True
pygame.init()
background_colour = (255,255,255)
(width, height) = (600, 600)

updateDisplay(width,height)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # zoom in
                background_colour = (0, 0, 0)
                # glTranslatef(1,0,0)
            elif event.key == pygame.K_DOWN:
                # zoom out
                background_colour = (255, 0, 0)
            elif event.key == pygame.K_LEFT:
                background_colour = (0, 255, 0)
            elif event.key == pygame.K_RIGHT:
                background_colour = (0, 0, 255)
            else:
                background_colour = (255, 255, 255)
            updateDisplay(width,height)


pygame.quit()

