import math
from math import pi, degrees, radians, sqrt, atan2
import random

#Belirtilen konumuna

def calculate_Direct_GoingDirection(FocusObj, ant):
    global stepAmount

    waysXlength = (FocusObj.position[0]+((FocusObj.scale*FocusObj.pixelSize)/2)) - ant.position[0]
    waysYlength = (FocusObj.position[1]+((FocusObj.scale*FocusObj.pixelSize)/2)) - ant.position[1]

    theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))

    dx = waysXlength
    dy = waysYlength
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)

    ant.angle = degs - 90 

    if theLength > 5:
        directStep(ant)
    else:
        ant.gidilecek_yol_kaldi_mi = False

def directStep(ant):
    ant.velocity = random.uniform(1.5, 3.5)
    radians = math.radians(ant.angle)
    vertical = math.cos(radians) * ant.velocity
    horizontal = math.sin(radians) * ant.velocity

    ant.position[1] -= vertical
    ant.position[0] -= horizontal
