import pygame
import time
import random
import math
import ant
from utils import scale_image, blit_rotate_center

BLACK = (0, 0 ,0)
GRAY = (128, 128, 128)

ANT = scale_image(pygame.image.load("ant.png"), 0.4)
FOOD = scale_image(pygame.image.load("food.png"), 1)

WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Colony Optimisation!")

FPS = 60


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




class tryAnt(AbstractAnt):
    IMG = ANT
    START_POS = (WIDTH / 2, HEIGHT / 2)


def draw(win, antList):

    for ants in antList:
        ants.draw(win)

    pygame.display.update()





def randomMoveAnts(ants):

    turningTimesAmount = 10
    turningMinus = 0.1 
    
    for tryingAnt in ants:
        tryingAnt.max_vel = random.uniform(1.5, 2.5)
        tryingAnt.rotation_vel = random.uniform(0.7, 1.7)
        tryingAnt.acceleration = random.uniform(0.4, 0.8)
        #this code block is deciding how ants are move
        if tryingAnt.timesTurnLeft > 0:
            tryingAnt.rotate(left = True)
            tryingAnt.timesTurnLeft -= turningMinus

        elif tryingAnt.timesTurnRight > 0:
            tryingAnt.rotate(right = True)
            tryingAnt.timesTurnRight -= turningMinus

        elif tryingAnt.timesNoTurn > 0:
            tryingAnt.timesNoTurn -= turningMinus



        elif random.randint(0,1)==1:
            tryingAnt.rotate(left=True)
            tryingAnt.timesTurnLeft = random.randint(0,turningTimesAmount)

        elif random.randint(0,1)==1:
            tryingAnt.timesTurnRight = random.randint(0,turningTimesAmount)
            tryingAnt.rotate(right=True)

        else:
            tryingAnt.timesNoTurn = random.randint(0,turningTimesAmount)
        moved = False

        if random.randint(0,2)==1:
            moved = True
            tryingAnt.move_forward()


            #this code block is an obstacle for curves of window
        if(tryingAnt.x<-40):
            tryingAnt.rotateBehind(1)
        if(tryingAnt.x>1400):
            tryingAnt.rotateBehind(2)
        if(tryingAnt.y<-40):
            tryingAnt.rotateBehind(3)
        if(tryingAnt.y>800):
            tryingAnt.rotateBehind(4)
        
        if not moved:
            tryingAnt.reduce_speed()

run = True
clock = pygame.time.Clock()
images = []

#first parameter is speed secone one is turning speed





rotateVel = 0.7
maxVel = 2
antAmount = 100
foodAmount = 20

ants = []

for ant in range(antAmount):
    ants.append(tryAnt(maxVel, rotateVel))


while run:

    clock.tick(FPS)

    WIN.fill(GRAY)
    draw(WIN, ants)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    randomMoveAnts(ants)
    
    pygame.display.flip()


pygame.quit()