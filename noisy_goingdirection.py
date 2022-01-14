from cmath import atan
from math import degrees, radians
import random
import math

#Neredeyse bir çizgi üzerinden en kısa yoldan git
#Eger gidecek yol kalmadiysa false döndür
def calculate_Noisy_GoingDirection(theAnt, theFood):
    ant_to_food : float = [theFood.position[0] - theAnt.position[0], theFood.position[1] - theAnt.position[1]]
    print(ant_to_food)
    ant_to_food_degrees : float = degrees(math.atan2(ant_to_food[1], ant_to_food[0]))
    
    rand : float = (random.random() * (ant_to_food_degrees - theAnt.angle) * 3)
    theAnt.angle = radians(rand + theAnt.angle)
    
    step1(theAnt)

    

def step1(theAnt):
    print(theAnt.velocity)
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