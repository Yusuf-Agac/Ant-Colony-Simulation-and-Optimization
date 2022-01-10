import pheromoneMap
import Food_and_Nest_Lists


class World:
    def __init__(self) -> None:
        self.map_of_pheromones : pheromoneMap.pheromoneMap = pheromoneMap.pheromoneMap(200,200)
        pass


    def add_Food(food_pos, food_scentrange):
        pass