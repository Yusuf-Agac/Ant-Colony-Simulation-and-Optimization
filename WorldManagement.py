import pheromoneMap
import Food_and_Nest_Lists
import ant
import random
import pygame
import time
import random
import math
import ant
import random_ant_movement
from utils import scale_image, blit_rotate_center


#first parameter is speed secone one is turning speed
rotateVel = 0.7
maxVel = 2
antAmount = 100

def add_ants(ants):
    for ant in range(antAmount):
        ants.append(ant.tryAnt(maxVel, rotateVel))


class World:
    def __init__(self, WIN) -> None:
        self.win = WIN
        self.map_of_pheromones : pheromoneMap.pheromoneMap = pheromoneMap.pheromoneMap(200,200)
        self.ants : ant.Ant = []
        ant.add_ants(self.ants)

        pass

    def update_and_draw(self):
        for ant in self.ants:
            ant.draw(self.win)

        pygame.display.update()
        random_ant_movement.randomMoveAnts(self.ants)


    def add_Food(food_pos, food_scentrange):
        pass


