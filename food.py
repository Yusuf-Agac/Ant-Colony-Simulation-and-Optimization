import pygame
import time
import random
import math
from utils import scale_image, blit_rotate_center
from parameters import *
from random import randint
from vector import Vector

screen_offset = 30
pygame.font.init()
text_color = (white)





##DON'T USE THESE THINGS BELOW!






class Food:
    #Size is size of food
    def __init__(self, position, size, win):
        self.position = position
        self.stock = size
        self.bite_size = 1
        self.image = scale_image(pygame.image.load("food.png"), size / 25.0)
        self.mainWin = win

    def Bite(self):
        self.stock -= self.bite_size

    def Update(self):
        if self.stock < 0:
            pass
            # self.position.x = randint(screen_offset, width-screen_offset)
            # self.position.y = randint(screen_offset,height-screen_offset)
            # self.stock = 25

    def Show(self, screen):
        if self.stock > 0 :
            self.draw(self.mainWin)
            text_font = pygame.font.SysFont("Arial", self.stock)
            text_surface = text_font.render(str(self.stock), True, text_color)
            text_rectangle = text_surface.get_rect(center=self.position.xy())
            screen.blit(text_surface, text_rectangle)
class FoodMap:
    def __init__(self, food_stock):
        self.size = food_stock
        self.foods = self.InitializeFood()

    def InitializeFood(self):
        return [ Food(Vector(randint(screen_offset, width-screen_offset), randint(screen_offset, height-screen_offset))) for _ in range(self.size)]

    def Update(self):
        for f in self.foods:
            f.Update()
            if f.stock <= 0:
                self.foods.remove(f)

    def GetClosestFood(self, position, uzaklik, CLOSESTFOOD):
        closest_food = self.foods[0]
        closest_distance = Vector.GetDistanceSQ(position, closest_food.position)
        temp_distance = closest_distance

        for x in range(1, len(self.foods)):
            temp_distance = Vector.GetDistanceSQ(position, self.foods[x].position)
            if temp_distance < closest_distance:
                closest_food = self.foods[x]
                closest_distance = temp_distance

        CLOSESTFOOD = closest_food
        if(closest_distance <= uzaklik):
            return True
        else:
            return False
            

    def foodGenerator(foodAmount, xSpace, ySpace):
        for counter1 in range(0,foodAmount):
            for counter2 in range(0, foodAmount):
                foods.append(tryFood(counter1 * xSpace, counter2 * ySpace))

    def Show(self, screen):
        for food in self.foods:
            food.Show(screen)




