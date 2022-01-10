from _typeshed import Self
import math
import pygame
import food
from parameters import *
from vector import Vector
from math import pi, degrees, radians, sqrt, exp, atan, trunc
from calculateDirection_Direct import calculate_Direct_GoingDirection
from random_ant_movement import Random_Travel
from food import bite
from noisy_goingdirection import calculate_Noisy_GoingDirection
import random
import WorldManagement



##Ant Grid Structure: Sahneyi gridlere böl, her grid 2 referans 2 deger tutsun. Referanslar: Biri en son geçenin yemegi bulduğu nokta, 
# digeri en son geçenin evden çıktığı nokta. Degerler: fenomon gucleri

#calculate_Random_GoingDirection: Furkan
#pheromoneMap'ler: Furkan

#Food ve Nest List: Yusuf
#Isır: Yusuf
#Random Travel: Yusuf
#calculate_Direct_GoingDirection: Yusuf

class Ant:
    def __init__(self, mainWIN, position, world):
        self.mainWin = mainWIN
        self.world : WorldManagement.World = world
        self.position = position
        self.velocity = Vector()
        self.max_speed = 3
        self.trigger_radius = 10
        self.smell_radius = 30
        # angle in radiant
        self.angle = -self.velocity.Heading()

        self.state = 0

    def Update(self, pheromones):
        # Yemek ara
        if(self.state == 1):
            closest_food = None
            yemek_cok_yakin_mi = foodList.GetClosestFood(self.position, self.burun_gucu, closest_food)

            #Yemek çok yakın, yemeğe direkt git hatta ısırabiliyorsan ısır
            if(yemek_cok_yakin_mi):
                gidilecek_yol_kaldi_mi = calculate_Direct_GoingDirection(self.position, self.velocity, closest_food)
                #Yemeğe direk gitme hesaplamasını yap, ısırabiliyorsan ısır ve eve dönüş state'lerini vs yap
                if(not gidilecek_yol_kaldi_mi):
                    bite(closest_food)


            #Yemek uzakta, en yakın yemek feromonunu bul sonra yemege git.
            else:
                #food döndürülmeli, okunmamalı
                yemek_feromon_kokusu_aldi_mi = self.world.map_of_pheromones.getClosestPheromone(True, self.position, closest_food)
            

                #Yakında yemek feromonu buldu, yemege gidiyor
                if(yemek_feromon_kokusu_aldi_mi):
                    #Random gitmeyi vs hallet
                    calculate_Noisy_GoingDirection(self.position, self.velocity, closest_food.position)
                else:
                    Random_Travel()


        # Ev ara
        elif(self.state == 2):
            closest_nest = None
            cok_yakinda_ev_var_mi = nestList.getClosestNest(self.position, closest_nest)
            #Ev yakındaysa eve yönel, yemeği bırak
            if(cok_yakinda_ev_var_mi):
                gidilecek_yol_kaldi_mi = calculate_Direct_GoingDirection(self.position, self.velocity, closest_nest.position)
                if(not gidilecek_yol_kaldi_mi):
                    Eve_Bırak_ve_Geri_Yola_Cık()

            #Yakında ev yok, ev feromonu ara
            else:
                ev_kokusu_aldi_mi = self.world.map_of_pheromones.getClosestPheromone(False, self.position, closest_nest)

                if(ev_kokusu_aldi_mi):
                    calculate_Noisy_GoingDirection(self.position, self.velocity)
                else:
                    Random_Travel()

        
            
        self.UpdateVelocity(closest_food, pheromones)
        self.velocity = self.velocity.Scale(self.max_speed)
        # self.position += self.velocity.Normalize()  * dt * self.max_speed
        self.position += self.velocity
        self.angle = self.velocity.Heading()




##DON'T USE THESE FUNCTIONS BELOW!
















    def ReturnToNest(self, pheromone):
        if Vector.WithinRange(self.position, self.nest.position, self.nest.radius):
            self.has_food = False
            self.nest.stock += 1
            self.color = white
            # self.angle = -self.velocity.Heading()
            return
        self.velocity += self.scavenger.Seek(self.position, self.nest.position, self.velocity, self.max_speed)
        # add some randomness to have some more realistic movement
        wander_force = self.scavenger.Wander(self.velocity)
        self.velocity += (wander_force * 0.5)
        pher_direction = self.velocity.Negate()

        pheromone.AppendPheromone(self.position, pher_direction ,"food")

    def SearchForFood(self, closest_food, pheromone):
        dist = Vector.GetDistance(self.position, closest_food.position)

        if dist < self.trigger_radius:
            self.TakeFood(closest_food)
        elif dist < self.smell_radius:
            self.Step(closest_food, pheromone)
        else:
            self.FollowPheromoneOrWander(pheromone)

        pheromone.AppendPheromone(self.position, self.velocity, "home")

    def UpdateVelocity(self, closest_food, pheromone):
        if self.has_food == True:
            self.ReturnToNest(pheromone)
        else:
            self.SearchForFood(closest_food, pheromone)


    def TakeFood(self, closest_food):
        self.has_food = True
        self.isFollowingTrail = False
        self.color = (220, 130 , 30)
        closest_food.Bite()

    def Step(self, closest_food, pheromone):
        self.velocity += self.scavenger.Seek(self.position, closest_food.position, self.velocity, self.max_speed)

    def FollowPheromoneOrWander(self, pheromone):
        pheromone_direction = pheromone.PheromoneDirection(self.position, self.smell_radius, "food")
        pheromone_direction = pheromone_direction.Scale(self.max_speed)
        self.velocity = pheromone_direction
        self.velocity += self.scavenger.Wander(self.velocity)
        # pheromone.AppendPheromone(self.position, self.velocity, "home")



    def Show(self, screen):
        blit_rotate_center(self.mainWin, self.img, (self.x, self.y), self.angle)

class Scavenger:
    def __init__(self):
        self.wander_distance = 20
        self.wander_radius = 10
        self.wander_angle = 1
        self.wander_delta_angle = pi/4

    def Seek(self, position, target, velocity, max_speed):
        diff = target - position
        diff = diff.Scale(max_speed)
        return diff - velocity

    def Wander(self, velocity):
        pos = velocity.Copy()
        pos = pos.Scale(self.wander_distance)
        displacement = Vector(0, -1).Scale(self.wander_radius)
        displacement = displacement.SetAngle(self.wander_angle)
        self.wander_angle += random.uniform(0, 1) * self.wander_delta_angle - self.wander_delta_angle * 0.5
        return pos + displacement
