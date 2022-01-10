import parameters

class pheromoneMap:
    def __init__(self, GridSizeX, GridSizeY):
        self.GRIDSIZEX = GridSizeX
        self.GRIDSIZEY = GridSizeY
        self.GRID = [[]]
        for i in range(self.GRIDSIZEX * self.GRIDSIZEY):
            self.GRID.append([None, None])


    def setPheromone(self, is_food_pheromone, pheromone_pos, obj_ref):
        index_y = ((pheromone_pos.y / (parameters.HEIGHT / self.GRIDSIZEY)) * self.GRIDSIZEX)
        if(index_y < 0):
            pass
        index =  + (pheromone_pos.x / (parameters.WIDTH / self.GRIDSIZEX))
        if(is_food_pheromone):
            self.GRID[index][1] = obj_ref
        else:
            self.GRID[index][0] = obj_ref

    def getClosestPheromone(is_searching_for_food, pos, return_obj):
        pass