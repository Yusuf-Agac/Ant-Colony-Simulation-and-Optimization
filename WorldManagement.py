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
import pheremoneSquareList
from utils import scale_image, blit_rotate_center
from typing import List


#first parameter is speed secone one is turning speed
rotateVel = 0.7
maxVel = 2
antAmount = 100
foodAmount = 1
nestAmount = 1



class World:
    def __init__(self, WIN) -> None:
        self.win = WIN
        self.map_of_pheromones : pheromoneMap.pheromoneMap = pheromoneMap.pheromoneMap(pheremoneSquareList.SQUAREAMOUNT,pheremoneSquareList.SQUAREAMOUNT)
        self.ants:List[Ant] = list()

        #fill do NestList
        for nest_i in range(nestAmount):
            NestList.append(nest())

        #Add ants
        for ant_i in range(antAmount):
            self.ants.append(Ant(self.win, self))
        
        #fill do FOODLIST
        for food_i in range(foodAmount):
            FoodList.append(food())


    def update_and_draw(self):

        pheremoneSquareList.drawRectList(self.win)
        

        for nest in NestList:
            nest.draw(self.win)

        for ant in self.ants:
            ant.draw(self.win)
            ant.Update()
        
        for food in FoodList:
            food.draw(self.win)

        pygame.display.update()

        

    def add_Food(self, food_pos, food_scentrange):
        pass


