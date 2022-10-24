from Lift import listLifts
from Person import listPersons, Person, listTimesTotal
from enums import PersonMode
import pygame.time as time
from constants import K

longTimesFloorsList = {}

def updateLiftsState():
    for lift in listLifts:
        lift.updateState()

def updatePersonsState():
    for person in listPersons:
        person: Person
        person.updateState()
        if person.mode == PersonMode.OUT: 
            timeEnd = time.get_ticks()
            print(timeEnd)
            timeElapsed = (timeEnd-person.timeStart)*K/1000
            listTimesTotal.append(timeElapsed)
            if(timeElapsed>200):
                longTimesFloorsList[person.id] = (person.startingFloor, person.wantedFloor, timeElapsed)
            
def updateListPersons():
    for person in listPersons:
        person: Person
        if(PersonMode.OUT == person.mode):
            listPersons.remove(person)
        

