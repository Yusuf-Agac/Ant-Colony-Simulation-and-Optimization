#from _typeshed import Self
import pygame
from parameters import *
from math import pi, degrees, radians, sqrt, exp, atan, trunc
import random
import WorldManagement
from utils import *

def bite(nearFood):
    nearFood.Bite()

FoodList = []

class food:
    def __init__(self):
        #self.mainWin = mainWIN
        #self.world : WorldManagement.World = world
        self.x, self.y = (700, 250)
        self.angle = 0
        self.size = 2
        self.img = scale_image(pygame.image.load("food.png"), 1)
    
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    
    def kill(self):
        del self


def WhichFoodIsClosest(x, y):

        theClosest = food()
        closestLen = 9999999999999999999

        for food_i in range(len(FoodList)):

            waysXlength = FoodList[food_i].x - x
            waysYlength = FoodList[food_i].y - y
            theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
            
            if theLength < closestLen:
                closestLen = theLength
                theClosest = FoodList[food_i]

        return theClosest

def Bite(Food, theAnt):
    Food.size -= 1
    theAnt.gidilecek_yol_kaldi_mi = True
    #theAnt.state = 2
    if Food.size <= 0:
        Food.kill()
    


















"""
def foodGenerator(foodAmount, xSpace, ySpace):
    for counter1 in range(0,foodAmount):
        for counter2 in range(0, foodAmount):
            foods.append(tryFood(counter1 * xSpace, counter2 * ySpace))

foodGenerator(foodAmount, 10, 10)
"""