from turtle import position
from typing import AnyStr
from Food_and_Nest_Lists import *
from ant import *
import pygame
import random
from utils import scale_image, blit_rotate_center
from typing import List
import parameters

SQUAREAMOUNT = 50
rectList = []

class pheremoneRect:
#the four parameter is transparency
        

        def __init__(self, position):
            
                self.RED = (255, 0, 0)
                self.BLUE = (0, 0, 255)
                self.size = (width/SQUAREAMOUNT-1, height/SQUAREAMOUNT-1)
                

                self.red_image = pygame.Surface(self.size, pygame.SRCALPHA)
                self.redAlphaNumber = 0

                self.blue_image = pygame.Surface(self.size, pygame.SRCALPHA)
                self.blueAlphaNumber = 0
                

                

                self.position = position

        def drawRed(self, WIN):
                self.red_image.fill(self.RED)
                self.red_image.set_alpha(self.redAlphaNumber)
                WIN.blit(self.red_image, self.position)

        def drawBlue(self, WIN):
                self.blue_image.fill(self.BLUE)
                self.blue_image.set_alpha(self.blueAlphaNumber)
                WIN.blit(self.blue_image, self.position)

for i in range(SQUAREAMOUNT):
        for j in range(SQUAREAMOUNT):
                position = (((i) * (width / SQUAREAMOUNT)), ((j) * (height / SQUAREAMOUNT)))
                rectList.append(pheremoneRect(position))


def drawRectList(WIN):
        for i in range(SQUAREAMOUNT*SQUAREAMOUNT):
                #draw
                rectList[i].drawBlue(WIN)
                        
                
def addBlueAlpha(index, GRIDSIZEX, GRIDSIZEY):
        index_y : int = int(index % GRIDSIZEX)
        index_x : int = int((index - index_y) / GRIDSIZEX)

        if rectList[int(((SQUAREAMOUNT - index_y - 1) * SQUAREAMOUNT) + (SQUAREAMOUNT - index_x - 1))].blueAlphaNumber<255:
                rectList[int((index_y * GRIDSIZEX) + (index_x))].blueAlphaNumber += 3

def addRedAlpha(index, GRIDSIZEX, GRIDSIZEY):
        index_y : int = int(index % GRIDSIZEX)
        index_x : int = int((index - index_y) / GRIDSIZEX)

        if rectList[int(((SQUAREAMOUNT - index_y - 1) * SQUAREAMOUNT) + (SQUAREAMOUNT - index_x - 1))].redAlphaNumber<255:
                rectList[int((index_y * GRIDSIZEX) + (index_x))].redAlphaNumber += 3
