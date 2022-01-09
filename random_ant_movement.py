import random

def randomMoveAnts(ants):

    turningTimesAmount = 10
    turningMinus = 0.1 
    
    for tryingAnt in ants:
        tryingAnt.max_vel = random.uniform(1.5, 2.5)
        tryingAnt.rotation_vel = random.uniform(0.7, 1.7)
        tryingAnt.acceleration = random.uniform(0.4, 0.8)
        #this code block is deciding how ants are move
        if tryingAnt.timesTurnLeft > 0:
            tryingAnt.rotate(left = True)
            tryingAnt.timesTurnLeft -= turningMinus

        elif tryingAnt.timesTurnRight > 0:
            tryingAnt.rotate(right = True)
            tryingAnt.timesTurnRight -= turningMinus

        elif tryingAnt.timesNoTurn > 0:
            tryingAnt.timesNoTurn -= turningMinus



        elif random.randint(0,1)==1:
            tryingAnt.rotate(left=True)
            tryingAnt.timesTurnLeft = random.randint(0,turningTimesAmount)

        elif random.randint(0,1)==1:
            tryingAnt.timesTurnRight = random.randint(0,turningTimesAmount)
            tryingAnt.rotate(right=True)

        else:
            tryingAnt.timesNoTurn = random.randint(0,turningTimesAmount)
        moved = False

        if random.randint(0,2)==1:
            moved = True
            tryingAnt.move_forward()


            #this code block is an obstacle for curves of window
        if(tryingAnt.x<-40):
            tryingAnt.rotateBehind(1)
        if(tryingAnt.x>1400):
            tryingAnt.rotateBehind(2)
        if(tryingAnt.y<-40):
            tryingAnt.rotateBehind(3)
        if(tryingAnt.y>800):
            tryingAnt.rotateBehind(4)
        
        if not moved:
            tryingAnt.reduce_speed()