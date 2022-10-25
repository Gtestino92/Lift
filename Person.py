from Lift import *
from enums import LiftMode
from enums import PersonMode
from typing import List
from enums import Floor
from constants import *
import itertools
import pygame.time as time

iter = itertools.count()
class Person:
    def __init__(self, floor: int, wantedFloor: int):
        self.id = next(iter)
        self.floor = floor
        self.startingFloor = floor
        self.wantedFloor = wantedFloor
        self.mode = PersonMode.WAIT
        self.timeStart = time.get_ticks()
        print(self.timeStart)
        self.lift = None
        self.calledLifts = []

    def callLift(self, lift: Lift):
        #self.lift = lift
        self.calledLifts.append(lift)
        lift.callFromPosition(self.floor)

    def enter(self, lift: Lift):
        self.calledLifts = []
        if (len(lift.listPersonsIn) == CAPACITY_MAX):
            print("OLEEE")
            return
        self.lift = lift
        self.lift.listPersonsIn.append(self)
        self.mode = PersonMode.IN
        self.lift.startBlock()
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
                    else:
                        if(possibleLift not in self.calledLifts):
                            self.callLift(possibleLift)       

listTimesTotal = []

