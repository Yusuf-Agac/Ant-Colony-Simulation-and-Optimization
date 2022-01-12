from typing import AnyStr
import pheromoneMap
from Food_and_Nest_Lists import *
from ant import *
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
foodAmount = 1
ants = []

class World:
    global ants
    def __init__(self, WIN) -> None:
        self.win = WIN
        self.map_of_pheromones : pheromoneMap.pheromoneMap = pheromoneMap.pheromoneMap(200,200)
        

        #Add ants
        for ant_i in range(antAmount):
            ants.append(Ant(self.win, self))
        
        #fill do FOODLIST
        for food_i in range(antAmount):
            FoodList.append(food())

    def update_and_draw(self):
        for ant in ants:
            ant.draw(self.win)
            ant.Update()
        
        for food in FoodList:
            food.draw(self.win)

        pygame.display.update()

        for ant in ants:
            random_ant_movement.Random_Travel(ant)


    def add_Food(food_pos, food_scentrange):
        pass


