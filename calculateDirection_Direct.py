import math
from math import pi, degrees, radians, sqrt, atan2

#Belirtilen konumuna
stepAmount = 0

def calculate_Direct_GoingDirection(focusX, focusY, ant):
    global stepAmount

    waysXlength = (focusX - ant.x)**2
    waysYlength = (focusY - ant.y)**2

    theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
    
    howMuchStep = theLength/ant.velocity

    radian = atan2(waysYlength, waysYlength)
    degree = radian*(180/pi)
    ant.angle = degree

    stepAmount = howMuchStep

    directStep(ant)

def directStep(ant):
    global stepAmount

    while stepAmount <= 0:
        radians = math.radians(ant.angle)
        vertical = math.cos(radians) * ant.velocity
        horizontal = math.sin(radians) * ant.velocity

        ant.y -= vertical
        ant.x -= horizontal
    
        stepAmount = stepAmount - 1

    if(stepAmount <= 0):
        ant.gidilecek_yol_kaldi_mi = False
