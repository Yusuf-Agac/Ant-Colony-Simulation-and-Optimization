import pygame
import noise
import WorldManagement
from utils import scale_image, blit_rotate_center

BLACK = (0, 0 ,0)
GRAY = (150, 150, 150)


WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Colony Optimisation!")

FPS = 60




run = True
clock = pygame.time.Clock()
WORLDMANAGER : WorldManagement.World = WorldManagement.World(WIN)

while run:
    clock.tick(FPS)
    WIN.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    WORLDMANAGER.update_and_draw()
    
    pygame.display.flip()


pygame.quit()