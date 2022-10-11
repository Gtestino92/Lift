from Lift import *
from enums import LiftMode
from enums import PersonMode
from typing import List
from enums import Floor
from constants import *
import itertools
import random

class Person:
    def __init__(self, floor: int, wantedFloor: int):
        self.id = next(itertools.count())
        self.floor = floor
        self.wantedFloor = wantedFloor
        self.mode = PersonMode.INIT
        self.timeTotal = 0
        self.lift = None

    def callLift(self, lift: Lift):
        self.mode = PersonMode.WAIT
        lift.callFromPosition(self.floor)

    def enter(self, lift: Lift):
        if (len(lift.listPersonsIn) == CAPACITY_MAX):
            print("OLEEE")
            return
        self.lift = lift
        self.lift.listPersonsIn.append(self)
        self.mode = PersonMode.IN
        self.lift.mode = LiftMode.BLOCK
        self.lift.callToPosition(self.wantedFloor)
    
    def leave(self):
        self.floor = int(self.lift.position)
        self.mode = PersonMode.OUT
        self.lift.listPersonsIn.remove(self)
        self.lift = None
        if(self.floor != self.wantedFloor): 
            print("Floor did not match, ", self.floor, " ", self.wantedFloor )
            raise Exception("WRONG FLOOR")

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
        self.timeTotal += TIMESTEP       

def createNewRandPerson():
    newPerson : Person
    possibleFloors = list(Floor.keys())
    possibleFloors.remove(0)
    if(random.choice([0,1]) == 0):      
        newPerson = Person(random.choice(possibleFloors), 0)
        print("LEAVING PERSON CREATED")
    else:
        newPerson = Person(0, random.choice(possibleFloors))
        print("COMING PERSON CREATED")
    listPersons.append(newPerson)
    

#person1 = Person(3, 0)
#person2 = Person(0, 5)
#person3 = Person(5, 0)

listPersons = []
