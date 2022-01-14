#from _typeshed import Self
import math
import pygame
import Food_and_Nest_Lists
from parameters import *
from vector import Vector
from math import pi, degrees, radians, sqrt, exp, atan, trunc
from calculateDirection_Direct import calculate_Direct_GoingDirection
from random_ant_movement import Random_Travel
from noisy_goingdirection import calculate_Noisy_GoingDirection
import random
import WorldManagement
import Food_and_Nest_Lists
from Food_and_Nest_Lists import *
from random_ant_movement import Random_Travel
from utils import *


##Ant Grid Structure: Sahneyi gridlere böl, her grid 2 referans 2 deger tutsun. Referanslar: Biri en son geçenin yemegi bulduğu nokta, 
# digeri en son geçenin evden çıktığı nokta. Degerler: fenomon gucleri

#calculate_Random_GoingDirection: Furkan
#pheromoneMap'ler: Furkan

#Food ve Nest List: Yusuf
#Isır: Yusuf
#Random Travel: Yusuf
#calculate_Direct_GoingDirection: Yusuf
#self, mainWIN, world (parameters)
class Ant:
    def __init__(self, mainWIN, world):
        self.mainWin : pygame.Surface = mainWIN
        self.world : WorldManagement.World = world
        self.position = [1000, 250]

        self.velocity = 2
        self.maxVel = 3
        self.rotationVel = 0.5
        self.acceleration = 0.4

        self.timesTurnLeft=0
        self.timesTurnRight=0
        self.timesNoTurn=0

        self.trigger_radius = 10
        self.burun_gucu = 200

        self.angle = random.randint(0,360)

        self.state = 1
        self.img = scale_image(pygame.image.load("ant.png"), 0.4)

        self.gidilecek_yol_kaldi_mi = True
        self.remembered_nest : nest = WhichNestIsClosest(self.position)
        self.remembered_food : food = None

    def draw(self, win):
        blit_rotate_center(win, self.img, self.position, self.angle)

    def isCloseEnoughToFood(self, burun_gucu, closestFood):

        if closestFood is None:
            return False

        waysXlength = closestFood.position[0] - self.position[0]
        waysYlength = closestFood.position[1] - self.position[1]
        theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
        
        if theLength > burun_gucu:
            return False
        else:
            return True

    def isCloseEnoughToNest(self, burun_gucu, closestNest):

        if closestNest is None:
            return False

        waysXlength = closestNest.position[0] - self.position[0]
        waysYlength = closestNest.position[1] - self.position[1]
        theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
        
        if theLength > burun_gucu:
            return False
        else:
            return True


    def Update(self):
        # Yemek ara
        if(self.state == 1):
            closest_food = WhichFoodIsClosest(self.position)
            
            yemek_cok_yakin_mi = self.isCloseEnoughToFood(self.burun_gucu, closest_food)

            #Yemek çok yakın, yemeğe direkt git hatta ısırabiliyorsan ısır
            if(yemek_cok_yakin_mi):

                calculate_Direct_GoingDirection(closest_food.position, self)

                #Yemeğe direk gitme hesaplamasını yap, ısırabiliyorsan ısır ve eve dönüş state'lerini vs yap
                if(not self.gidilecek_yol_kaldi_mi):
                    Bite(closest_food, self)
                    self.remembered_food = closest_food


            #Yemek uzakta, en yakın yemek feromonunu bul sonra yemege git.
            else:
                
                #food döndürülmeli, okunmamalı
                yemek_feromon_kokusu_aldi_mi = self.world.map_of_pheromones.getClosestPheromone(True, self.position, closest_food)
            
                
                #Yakında yemek feromonu buldu, yemege gidiyor
                if(yemek_feromon_kokusu_aldi_mi):
                    #Random gitmeyi vs hallet
                    
                    if(closest_food is not None):
                        calculate_Noisy_GoingDirection(self, closest_food)
                    else:
                        Random_Travel(self)
                    #self.mainWin.set_at((int(self.position[0]), int(self.position[1])), (0,0, 0))

                else:
                    Random_Travel(self)
                
                    if(not self.remembered_nest == None):
                        self.world.map_of_pheromones.setPheromone(self)


        # Ev ara
        elif(self.state == 2):

            closest_nest = None
            closest_nest = WhichNestIsClosest(self.position)

            cok_yakinda_ev_var_mi = self.isCloseEnoughToNest(self.burun_gucu, closest_nest)

            #Ev yakındaysa eve yönel, yemeği bırak
            if(cok_yakinda_ev_var_mi):
                
                calculate_Direct_GoingDirection(closest_nest.position, self)

                if(not self.gidilecek_yol_kaldi_mi):
                    StockTheFood(closest_nest, self)
                    self.remembered_nest = closest_nest

            #Yakında ev yok, ev feromonu ara
            else:
                
                ev_kokusu_aldi_mi = self.world.map_of_pheromones.getClosestPheromone(False, self.position, closest_nest)

                if(ev_kokusu_aldi_mi):

                    calculate_Noisy_GoingDirection(self, closest_nest)

                    #self.mainWin.set_at((self.position[0], self.position[1]), (255,255, 255))
                else:
                    Random_Travel(self)
                    if(not self.remembered_food == None):
                        self.world.map_of_pheromones.setPheromone(self)
        
            
        #self.UpdateVelocity(closest_food, pheromones)
        #self.velocity = self.velocity.Scale(self.max_speed)
        # self.position += self.velocity.Normalize()  * dt * self.max_speed
        #self.position += self.velocity
        #self.angle = self.velocity.Heading()

