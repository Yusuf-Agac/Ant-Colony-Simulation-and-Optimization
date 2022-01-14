from typing import AnyStr
from main import WIN
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
from typing import List


#first parameter is speed secone one is turning speed
rotateVel = 0.7
maxVel = 2
antAmount = 100
foodAmount = 3
nestAmount = 1

RED = (255, 0, 0)
BLUE = (0, 0, 255)

class World:
    def __init__(self, WIN) -> None:
        self.win = WIN
        self.map_of_pheromones : pheromoneMap.pheromoneMap = pheromoneMap.pheromoneMap(200,200)
        self.ants:List[Ant] = list()

        #Add ants
        for ant_i in range(antAmount):
            self.ants.append(Ant(self.win, self))
        
        #fill do FOODLIST
        for food_i in range(foodAmount):
            FoodList.append(food())

        for nest_i in range(nestAmount):
            NestList.append(nest())

    def update_and_draw(self):
        for ant in self.ants:
            ant.draw(self.win)
            ant.Update()
        
        for food in FoodList:
            food.draw(self.win)

        for nest in NestList:
            nest.draw(self.win)


        pygame.display.update()
