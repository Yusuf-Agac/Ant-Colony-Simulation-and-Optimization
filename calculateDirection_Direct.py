import math
from math import pi, degrees, radians, sqrt, atan2

#Belirtilen konumuna

def calculate_Direct_GoingDirection(focusX, focusY, ant):
    global stepAmount

    waysXlength = focusX - ant.x
    waysYlength = focusY - ant.y

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

    ant.y -= vertical
    ant.x -= horizontal
