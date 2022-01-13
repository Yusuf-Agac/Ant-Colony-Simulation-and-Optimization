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