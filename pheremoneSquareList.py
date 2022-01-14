from turtle import position
from typing import AnyStr
from Food_and_Nest_Lists import *
from ant import *
import random
import pygame
import random
from utils import scale_image, blit_rotate_center
from typing import List

rectList = []
SQUAREAMOUNT = 100


class pheremoneRect:
#the four parameter is transparency
        

        def __init__(self, position):
            
                self.RED = (255, 0, 0)
                self.BLUE = (0, 0, 255)
                self.size = (width/SQUAREAMOUNT-1, height/SQUAREAMOUNT-1)
                

                self.red_image = pygame.Surface(self.size, pygame.SRCALPHA)
                self.redAlphaNumber = 10

                self.blue_image = pygame.Surface(self.size, pygame.SRCALPHA)
                self.blueAlphaNumber = 10
                

                

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
                position = (width/SQUAREAMOUNT * (i), height/SQUAREAMOUNT * (j))
                rectList.append(pheremoneRect(position))

def drawRectList(WIN):
        for i in range(SQUAREAMOUNT*SQUAREAMOUNT):
                        rectList[i].drawRed(WIN)
                        rectList[i].drawBlue(WIN)
                
                