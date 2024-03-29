from cmath import atan
from math import atan2, degrees, pi, radians
import random
import math

#Neredeyse bir çizgi üzerinden en kısa yoldan git
#Eger gidecek yol kalmadiysa false döndür
def calculate_Noisy_GoingDirection(theAnt, destination):
    ant_to_food : float = [destination.position[0]+((destination.scale*destination.pixelSize)/2) - theAnt.position[0], destination.position[1]+((destination.scale*destination.pixelSize)/2) - theAnt.position[1]]
    
    rads = atan2(-ant_to_food[1], ant_to_food[0])
    rads %= 2*pi
    degs = degrees(rads)
    ant_to_food_degrees = degs - 90

    if(ant_to_food_degrees>theAnt.angle):
        theAnt.angle += (ant_to_food_degrees-theAnt.angle)*random.uniform(0.5, 1)
    elif (ant_to_food_degrees<theAnt.angle):
        theAnt.angle -= (theAnt.angle-ant_to_food_degrees)*random.uniform(0.5, 1)
    
    step1(theAnt)

    

def step1(theAnt):
    theAnt.velocity = random.uniform(1.5, 3.5)
    radians = math.radians(theAnt.angle)
    vertical = math.cos(radians) * theAnt.velocity
    horizontal = math.sin(radians) * theAnt.velocity

    theAnt.position[1] -= vertical
    theAnt.position[0] -= horizontal





"""
from cmath import atan
from math import degrees, radians
import random
import math

#Neredeyse bir çizgi üzerinden en kısa yoldan git
#Eger gidecek yol kalmadiysa false döndür
def calculate_Noisy_GoingDirection(position, angle, food_position) -> float:
    ant_to_food : float = [food_position[0] - position[0], food_position[1] - position[1]]
    ant_to_food_degrees : float = degrees(math.atan2(ant_to_food[1], ant_to_food[0]))
    
    rand : float = (random.random() * (ant_to_food_degrees - angle) * 3)
    return radians(rand + angle)
"""