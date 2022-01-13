import math
from math import pi, degrees, radians, sqrt, atan2

#Belirtilen konumuna

def calculate_Direct_GoingDirection(focusPosition, ant):
    global stepAmount

    waysXlength = focusPosition[0] - ant.position[0]
    waysYlength = focusPosition[1] - ant.position[1]

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

    radians = math.radians(ant.angle)
    vertical = math.cos(radians) * ant.velocity
    horizontal = math.sin(radians) * ant.velocity

    ant.position[1] -= vertical
    ant.position[0] -= horizontal
