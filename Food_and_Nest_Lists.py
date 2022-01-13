#from _typeshed import Self
import pygame
from parameters import *
from math import pi, degrees, radians, sqrt, exp, atan, trunc
import random
import WorldManagement
from utils import *
from typing import List



class food:
    def __init__(self):
        #self.mainWin = mainWIN
        #self.world : WorldManagement.World = world
        self.position = [20, 30]
        self.angle = 0
        self.size = 30
        self.img = scale_image(pygame.image.load("food.png"), 10)
    
    def draw(self, win):
        blit_rotate_center(win, self.img, self.position, self.angle)
    
    def kill(self):
        del self

FoodList : List[food] = []



def WhichFoodIsClosest(position):
        theClosest = None
        closestLen = 9999999999999999999

        for food_i in range(len(FoodList)):

            waysXlength = FoodList[food_i].position[0] - position[0]
            waysYlength = FoodList[food_i].position[1] - position[1]
            theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
            
            if theLength < closestLen:
                closestLen = theLength
                theClosest = FoodList[food_i]

        return theClosest

def Bite(Food, theAnt):
    Food:food
    theAnt.state = 2
    Food.size -= 1
    print("The Ant Bite The Food")
    theAnt.gidilecek_yol_kaldi_mi = True
    
    if Food.size <= 0:
        print("Food is done")
        print(Food)
        FoodList.remove(Food)
        del Food
        



NestList = []

class nest:
    def __init__(self):
        #self.mainWin = mainWIN
        #self.world : WorldManagement.World = world
        self.position = [1000, 250]
        self.angle = 0
        self.sizeOfFoodStocks = 0
        self.img = scale_image(pygame.image.load("nest.png"), 1)
    
    def draw(self, win):
        blit_rotate_center(win, self.img, self.position, self.angle)
    
def StockTheFood(Nest, theAnt):
        Nest.sizeOfFoodStocks += 1
        theAnt.gidilecek_yol_kaldi_mi = True
        theAnt.state = print("The Ant Stock The Food")
        theAnt.state = 1

def WhichNestIsClosest(position):
        theClosest = None
        closestLen = 9999999999999999999

        for nest_i in range(len(NestList)):

            waysXlength = NestList[nest_i].position[0] - position[0]
            waysYlength = NestList[nest_i].position[1] - position[1]
            theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
            
            if theLength < closestLen:
                closestLen = theLength
                theClosest = NestList[nest_i]

        return theClosest

    


















"""
def foodGenerator(foodAmount, xSpace, ySpace):
    for counter1 in range(0,foodAmount):
        for counter2 in range(0, foodAmount):
            foods.append(tryFood(counter1 * xSpace, counter2 * ySpace))

foodGenerator(foodAmount, 10, 10)
"""