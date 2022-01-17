from turtle import position
from typing import AnyStr
from Food_and_Nest_Lists import *
from ant import *
import pygame
import random
from utils import scale_image, blit_rotate_center
from typing import List
import parameters

SQUAREAMOUNT = 113
VAPORIZEAMOUNT = 1.5
rectList = []

class pheremoneRect:
#the four parameter is transparency
        

        def __init__(self, position):
            
                self.RED = (1, 0, 0)
                self.BLUE = (0, 0, 1)
                self.Color = [0, 0, 0]
                self.size = (width/SQUAREAMOUNT-1, height/SQUAREAMOUNT-1)
                

                self.image = pygame.Surface(self.size, pygame.SRCALPHA)
                self.redAlphaNumber = 0
                self.blueAlphaNumber = 0
                

                

                self.position = position

        def draw(self, WIN):

                self.Color[0] = self.redAlphaNumber
                self.Color[2] = self.blueAlphaNumber
                self.image.fill(tuple(self.Color))

                if(self.redAlphaNumber>self.blueAlphaNumber):
                        self.image.set_alpha(self.redAlphaNumber/1.5)
                else:
                        self.image.set_alpha(self.blueAlphaNumber/1.5)

                WIN.blit(self.image, self.position)

for i in range(SQUAREAMOUNT):
        for j in range(SQUAREAMOUNT):
                position = (((i) * (width / SQUAREAMOUNT)), ((j) * (height / SQUAREAMOUNT)))
                rectList.append(pheremoneRect(position))


def drawRectList(WIN):
        for i in range(SQUAREAMOUNT*SQUAREAMOUNT):
                #draw
                rectList[i].draw(WIN)
                if(rectList[i].blueAlphaNumber-VAPORIZEAMOUNT>VAPORIZEAMOUNT):
                        rectList[i].blueAlphaNumber -= VAPORIZEAMOUNT
                if(rectList[i].redAlphaNumber-VAPORIZEAMOUNT>VAPORIZEAMOUNT):
                        rectList[i].redAlphaNumber -= VAPORIZEAMOUNT
                        
                
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
