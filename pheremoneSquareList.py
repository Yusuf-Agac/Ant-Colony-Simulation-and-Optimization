from turtle import position
from typing import AnyStr
from Food_and_Nest_Lists import *
from ant import *
import pygame
import random
from utils import scale_image, blit_rotate_center
from typing import List
import parameters

SQUAREAMOUNT = 150
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
                rectList[i].drawRed(WIN)
                rectList[i].blueAlphaNumber -= 1
                rectList[i].redAlphaNumber -= 1
                        
                
def addBlueAlpha(index, GRIDSIZEX, GRIDSIZEY):
        index_y : int = int(index % GRIDSIZEX)
        index_x : int = int((index - index_y) / GRIDSIZEX)

        if rectList[int((index_y * GRIDSIZEX) + (index_x))].blueAlphaNumber<255:
                rectList[int((index_y * GRIDSIZEX) + (index_x))].blueAlphaNumber = 255

def addRedAlpha(index, GRIDSIZEX, GRIDSIZEY):
        index_y : int = int(index % GRIDSIZEX)
        index_x : int = int((index - index_y) / GRIDSIZEX)
        
        if rectList[int((index_y * GRIDSIZEX) + (index_x))].redAlphaNumber<255:
                rectList[int((index_y * GRIDSIZEX) + (index_x))].redAlphaNumber = 255
