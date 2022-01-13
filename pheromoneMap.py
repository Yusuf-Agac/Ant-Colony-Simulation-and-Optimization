import parameters

class pheromoneMap:
    def __init__(self, GridSizeX, GridSizeY):
        self.GRIDSIZEX = GridSizeX
        self.GRIDSIZEY = GridSizeY
        self.GRID = [[]]
        for i in range(self.GRIDSIZEX * self.GRIDSIZEY):
            self.GRID.append([None, None])


    def setPheromone(self, is_food_pheromone, pheromone_pos, obj_ref):
        index_y = (pheromone_pos.y / (parameters.HEIGHT / self.GRIDSIZEY))
        if(index_y < 0):
            pass
        index_x = ((pheromone_pos.x / (parameters.WIDTH / self.GRIDSIZEX)))
        if(index_x < 0):
            pass
        
        index = (index_y * self.GRIDSIZEX) + index_x
        if(is_food_pheromone):
            self.GRID[index][1] = obj_ref
        else:
            self.GRID[index][0] = obj_ref

    def getClosestPheromone(self, is_searching_for_food, pos, return_obj):
        pheromonetype : int = 0
        if(is_searching_for_food): 
            pheromonetype = 1
        else:
            pheromonetype = 0


        index_y = (pos.y / (parameters.HEIGHT / self.GRIDSIZEY))
        if(index_y < 0):
            pass
        index_x = ((pos.x / (parameters.WIDTH / self.GRIDSIZEX)))
        if(index_x < 0):
            pass
        index = (index_y * self.GRIDSIZEX) + index_x
        return self.GRID[index][pheromonetype]