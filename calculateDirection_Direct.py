import math
from math import pi, degrees, radians, sqrt, exp, atan

#Belirtilen konumuna
stepAmount = 0
def calculate_Direct_GoingDirection(Position, Velocity, focusPosition):
    global stepAmount
    waysXlength = focusPosition.x - Position.x
    waysYlength = focusPosition.y - Position.y
    theLength = sqrt(((waysXlength)*(waysXlength))+((waysYlength)*(waysYlength)))
    inclination = (waysYlength)/(waysXlength)
    howMuchStep = int(theLength/Velocity)
    theAngle = atan(inclination)
    self.angle = theAngle
    stepAmount = howMuchStep

def directStep():
    radians = math.radians(self.angle)
    vertical = math.cos(radians) * self.velocity
    horizontal = math.sin(radians) * self.velocity

    self.y -= vertical
    self.x -= horizontal
    
    stepAmount = stepAmount - 1

    if(stepAmount <= 0):
        pass
