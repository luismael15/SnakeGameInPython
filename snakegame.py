import pygame

from pygame.locals import *

def draw_block():
    surface.fill((250, 222, 240))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()


if __name__== "__main__":
    pygame.init()

    surface= pygame.display.set_mode((1000,500))
    surface.fill((250, 222, 240))

    block=pygame.image.load('resources/block.jpg').convert()
    block_x=100
    block_y=110
    surface.blit(block,(block_x,block_y))

    pygame.display.flip()


    running= True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
            elif event.type == QUIT:
                running = False