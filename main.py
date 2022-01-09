import pygame
import random_ant_movement
import add_ants
from utils import scale_image, blit_rotate_center

BLACK = (0, 0 ,0)
GRAY = (150, 150, 150)


WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Colony Optimisation!")

FPS = 60


def draw(win, antList):

    for ants in antList:
        ants.draw(win)

    pygame.display.update()






run = True
clock = pygame.time.Clock()
images = []

ants = []
add_ants.add_ants(ants)


while run:

    clock.tick(FPS)

    WIN.fill(GRAY)
    draw(WIN, ants)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    random_ant_movement.randomMoveAnts(ants)
    
    pygame.display.flip()


pygame.quit()