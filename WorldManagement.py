import pheromoneMap
import Food_and_Nest_Lists
import ant
import random
import pygame
import time
import random
import math
import random_ant_movement
from utils import scale_image, blit_rotate_center


#first parameter is speed secone one is turning speed
rotateVel = 0.7
maxVel = 2
antAmount = 100

class World:
    def __init__(self, WIN) -> None:
        self.win = WIN
        self.map_of_pheromones : pheromoneMap.pheromoneMap = pheromoneMap.pheromoneMap(200,200)
        self.ants : ant.tryAnt = []

        #Add ants
        for ant_i in range(antAmount):
            self.ants.append(ant.tryAnt(maxVel, rotateVel))

    def update_and_draw(self):
        for ant in self.ants:
            ant.draw(self.win)

        pygame.display.update()
        random_ant_movement.randomMoveAnts(self.ants)


    def add_Food(food_pos, food_scentrange):
        pass


