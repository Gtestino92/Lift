import math
from enums import LiftMode
from utils import splitArrayByValue

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
    
    ######################## VER CODIGO REPETIDO ##################################
    def callFromPosition(self, positionFrom: int): 
        if(positionFrom in self.listPositionsPendingOutside): return
        self.listPositionsPendingOutside.append(positionFrom)
        ## DIVIDO EL ARRAY CON self.position
        listPositionsLwr, listPositionsGrEq = splitArrayByValue(self.listPositionsPendingOutside, math.floor(self.position))
        ## ORDENO UNO U OTRO DEP DE ESTADO
        listPositionsGrEq.sort()
        listPositionsLwr.sort(reverse=True)
        if(self.mode == LiftMode.DESC ):
            self.listPositionsPendingOutside = listPositionsLwr + listPositionsGrEq
        elif(self.mode == LiftMode.ASC):
            self.listPositionsPendingOutside = listPositionsGrEq + listPositionsLwr
          

    def callToPosition(self, positionTo: int): 
        if(positionTo in self.listPositionsCalledInside): return
        self.listPositionsCalledInside.append(positionTo)
        ## DIVIDO EL ARRAY CON self.position
        listPositionsLwr, listPositionsGrEq = splitArrayByValue(self.listPositionsCalledInside, math.floor(self.position))
        ## ORDENO UNO U OTRO DEP DE ESTADO
        listPositionsGrEq.sort()
        listPositionsLwr.sort(reverse=True)
        if(self.mode == LiftMode.DESC ):
            self.listPositionsCalledInside = listPositionsLwr + listPositionsGrEq
        elif(self.mode == LiftMode.ASC):
            self.listPositionsCalledInside = listPositionsGrEq + listPositionsLwr

    def getFloor(self):
        return int(math.floor(self.position))

    def updateBlockTimer(self):
        if(self.blockTimer == 0):
            self.mode = LiftMode.STOP
            self.blockTimer = BLOCK_TIMER_MAX
        else:
            self.blockTimer -= TIMESTEP

    def updateState(self):
        if(len(self.listPositionsCalledInside) > 0):
            if(self.position == self.listPositionsCalledInside[0]):
                self.listPositionsCalledInside = self.listPositionsCalledInside[1:]
                self.mode = LiftMode.BLOCK
            
            if(self.mode == LiftMode.STOP):
                self.callToPosition(self.listPositionsCalledInside[0])
            ######################## VER CODIGO REPETIDO ##################################
                if(self.listPositionsCalledInside[0] > math.floor(self.position) ):
                    self.mode = LiftMode.ASC
                elif(self.listPositionsCalledInside[0] < math.floor(self.position) ):
                    self.mode = LiftMode.DESC
        
        if(len(self.listPositionsPendingOutside) > 0):
            if(self.position == self.listPositionsPendingOutside[0]):
                self.listPositionsPendingOutside = self.listPositionsPendingOutside[1:]
                self.mode = LiftMode.BLOCK
            if(self.mode == LiftMode.STOP):
                self.callFromPosition(self.listPositionsPendingOutside[0])
        
                if(self.listPositionsPendingOutside[0] > math.floor(self.position) ):
                    self.mode = LiftMode.ASC
                elif(self.listPositionsPendingOutside[0] < math.floor(self.position) ):
                    self.mode = LiftMode.DESC

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

