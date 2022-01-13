from cmath import atan
from math import degrees, radians
import random

#Neredeyse bir çizgi üzerinden en kısa yoldan git
#Eger gidecek yol kalmadiysa false döndür
def calculate_Noisy_GoingDirection(position, angle):
    rand : float = (random.random() * 15)
    return radians(rand + angle)