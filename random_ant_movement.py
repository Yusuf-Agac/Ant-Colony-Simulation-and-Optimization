import math
import random

def Random_Travel(ant):

    turningTimesAmount = 5
    turningMinus = 0.1
    
    ant.maxVel = random.uniform(1.5, 2.5)
    ant.rotationVel = random.uniform(0.7, 1.7)
    ant.acceleration = random.uniform(0.4, 0.8)
    
    #this code block is deciding how ants are move
    if ant.timesTurnLeft > 0:
        ant.angle += ant.rotationVel
        ant.timesTurnLeft -= turningMinus

    elif ant.timesTurnRight > 0:
        ant.angle -= ant.rotationVel
        ant.timesTurnRight -= turningMinus

    elif ant.timesNoTurn > 0:
        ant.timesNoTurn -= turningMinus


    else:
        key = random.randint(0,2)
        switcher = {
            0: "zero",
            1: "one",
            2: "two",
        }
        if switcher.get(key)=="zero":
            ant.timesTurnLeft = random.randint(0,turningTimesAmount)

        elif switcher.get(key)=="one":
            ant.timesTurnRight = random.randint(0,turningTimesAmount)

        else:
            ant.timesNoTurn = random.randint(0,turningTimesAmount)

    moved = False

    if random.randint(0,2)==1:
        moved = True
        ant.velocity = min(ant.velocity + ant.acceleration, ant.maxVel)
        radians = math.radians(ant.angle)
        vertical = math.cos(radians) * ant.velocity
        horizontal = math.sin(radians) * ant.velocity

        ant.y -= vertical
        ant.x -= horizontal


    #this code block is an obstacle for curves of window
    if(ant.x<-40):
        ant.angle = 270;
    if(ant.x>1400):
        ant.angle = 90;
    if(ant.y<-40):
        ant.angle = 180;
    if(ant.y>800):
        ant.angle = 0;
        
    if not moved:
        ant.velocity = max(ant.velocity - ant.acceleration / 3, 0)

        radians = math.radians(ant.angle)
        vertical = math.cos(radians) * ant.velocity
        horizontal = math.sin(radians) * ant.velocity

        ant.y -= vertical
        ant.x -= horizontal


#Hedefi yok, random gez
#Yani bir kareliğine random hareket et