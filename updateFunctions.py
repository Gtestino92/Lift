from Lift import listLifts
from Person import Person, listTimesTotal
from enums import PersonMode
import pygame.time as time
from constants import K
from Graph import listPersonBlocks, PersonBlock

longTimesFloorsList = {}

def updateLiftsState():
    for lift in listLifts:
        lift.updateState()

def updatePersonsState():
    for personBlock in listPersonBlocks:
        personBlock : PersonBlock
        person : Person = personBlock.person 
        person.updateState()
        if person.mode == PersonMode.OUT: 
            timeEnd = time.get_ticks()
            print(timeEnd)
            timeElapsed = (timeEnd-person.timeStart)*K/1000
            listTimesTotal.append(timeElapsed)
            if(timeElapsed>200):
                longTimesFloorsList[person.id] = (person.startingFloor, person.wantedFloor, timeElapsed)
            
def updateListPersonBlocks():
    for personBlock in listPersonBlocks:
        personBlock: PersonBlock
        if(PersonMode.OUT == personBlock.person.mode):
            listPersonBlocks.remove(personBlock)
        

