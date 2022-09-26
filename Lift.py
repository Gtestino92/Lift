import math
from enums import LiftMode
from enums import PersonMode
from enums import Floor

from constants import *

class Lift:
    def __init__(self,id):
        self.id = id
        self.position = 0
        self.listPersonsIn = []
        self.listPositionsPendingOutside = []
        self.listPositionsCalledInside = []
        self.mode = LiftMode.STOP
        self.blockTimer = BLOCK_TIMER_MAX
    
    def callFromPosition(self, positionFrom: int):
        if(positionFrom not in self.listPositionsPendingOutside):
            self.listPositionsPendingOutside.append(positionFrom)
            self.listPositionsPendingOutside.sort(reverse=True)
        if(len(self.listPositionsPendingOutside) > 0 ):
            if(self.mode == LiftMode.STOP and self.listPositionsPendingOutside[0] > math.floor(self.position) ):
                self.mode = LiftMode.ASC
            elif(self.mode == LiftMode.STOP and self.listPositionsPendingOutside[0] < math.floor(self.position) ):
                self.mode = LiftMode.DESC

    def callToPosition(self, positionTo: int):
        if(positionTo not in self.listPositionsCalledInside):
            self.listPositionsCalledInside.append(positionTo)
            self.listPositionsCalledInside.sort()
        if(len(self.listPositionsCalledInside) > 0 ):
            if(self.mode == LiftMode.STOP and self.listPositionsCalledInside[0] > math.floor(self.position) ):
                self.mode = LiftMode.ASC
            elif(self.mode == LiftMode.STOP and self.listPositionsCalledInside[0] < math.floor(self.position) ):
                self.mode = LiftMode.DESC

    def getFloor(self):
        return int(math.floor(self.position))

    def updateBlockTimer(self):
        if(self.blockTimer == 0):
            self.mode = LiftMode.STOP
            self.blockTimer = BLOCK_TIMER_MAX
        else:
            self.blockTimer -= TIMESTEP

    def updateLiftState(self):
        if(len(self.listPositionsCalledInside) > 0):
            if(self.position == self.listPositionsCalledInside[0]):
                self.listPositionsCalledInside = self.listPositionsCalledInside[1:]
                self.mode = LiftMode.BLOCK
            if(self.mode == LiftMode.STOP):
                self.callToPosition(self.listPositionsCalledInside[0])
        elif(len(self.listPositionsPendingOutside) > 0):
            if(self.position == self.listPositionsPendingOutside[0]):
                self.listPositionsPendingOutside = self.listPositionsPendingOutside[1:]
                self.mode = LiftMode.BLOCK
            if(self.mode == LiftMode.STOP):
                self.callFromPosition(self.listPositionsPendingOutside[0])
        
        if(self.mode == LiftMode.ASC):
            self.position += STEP
        elif(self.mode == LiftMode.DESC):
                self.position -= STEP
        elif(self.mode == LiftMode.BLOCK):
            self.updateBlockTimer()

def getPossibleLiftsByFloor(floor):
    listPossibleLifts = [liftMiddle]
    #if(floor%2 == 0):
    #    listLifts.append(liftEvens)
    #else:
    #    listLifts.append(liftOdds)
    return listPossibleLifts

liftMiddle = Lift(id = 0)
liftOdds = Lift(id = 1)
liftEvens = Lift(id = 2)
listLifts = [liftMiddle]
