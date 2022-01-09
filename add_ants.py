import random
import pygame
import time
import random
import math
import ant
from utils import scale_image, blit_rotate_center

#first parameter is speed secone one is turning speed
rotateVel = 0.7
maxVel = 2
antAmount = 100
foodAmount = 20



class AbstractAnt:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = random.randint(0,360)
        self.x, self.y = self.START_POS

        self.acceleration = 0.4
        self.timesTurnLeft=0
        self.timesTurnRight=0
        self.timesNoTurn=0

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 5, 0)
        self.move()
    
    def rotateBehind(self, key):
        if(key==1):
            self.angle = 270;
        elif(key==2):
            self.angle = 90;
        elif(key==3):
            self.angle = 180;
        elif(key==4):
            self.angle = 0;



ANT = scale_image(pygame.image.load("ant.png"), 0.4)
FOOD = scale_image(pygame.image.load("food.png"), 1)

WIDTH, HEIGHT = 1366, 768
class tryAnt(AbstractAnt):
    IMG = ANT
    START_POS = (WIDTH / 2, HEIGHT / 2)

def add_ants(ants):
    for ant in range(antAmount):
        ants.append(tryAnt(maxVel, rotateVel))