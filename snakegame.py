import pygame

from pygame.locals import *

if __name__== "__main__":
    pygame.init()

    surface= pygame.display.set_mode((500,500))
    surface.fill((110,110,5))
    pygame.display.flip()


    running= True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            elif event.type== QUIT:
                running = False