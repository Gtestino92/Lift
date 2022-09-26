from Lift import *
from enums import LiftMode
from enums import PersonMode
from typing import List
from enums import Floor
from constants import *

class Person:
    def __init__(self,id,floor: int, wantedFloor: int):
        self.id = id
        self.floor = floor
        self.wantedFloor = wantedFloor
        self.mode = PersonMode.OUT
        self.lift = None

    def callLift(self, lift: Lift):
        self.mode = PersonMode.WAIT
        lift.callFromPosition(self.floor)

    def enter(self, lift: Lift):
        if (len(lift.listPersonsIn) == CAPACITY_MAX): return
        self.lift = lift
        self.lift.listPersonsIn.append(self)
        self.mode = PersonMode.IN
        self.lift.callToPosition(self.wantedFloor)
    
    def leave(self):
        self.floor = int(self.lift.position)
        self.mode = PersonMode.OUT
        self.lift.listPersonsIn.remove(self)
        self.lift = None
        self.wantedFloor = None

    def updateState(self):
        if (self.lift != None):
            if(self.lift.mode  == LiftMode.BLOCK): 
                if(self.mode == PersonMode.IN):
                    if(self.wantedFloor == self.lift.position and (self in self.lift.listPersonsIn)):
                        self.leave()
                    elif (self.floor == self.lift.position):
                        self.lift.callToPosition(self.wantedFloor)
        else:
            if(self.mode == PersonMode.WAIT):
                listPossibleLifts = getPossibleLiftsByFloor(self.floor)
                for possibleLift in listPossibleLifts:
                    if(self.floor == possibleLift.position):
                        if (possibleLift.mode in [LiftMode.BLOCK, LiftMode.STOP]):
                            self.enter(possibleLift)        


person1 = Person(1, Floor["PB"], Floor["P2"])
person2 = Person(2, Floor["P3"], Floor["PB"])
person3 = Person(3, Floor["P5"], Floor["PB"])

listPersons = [person1, person2]
