from Lift import listLifts
from Person import listPersons, Person
from enums import PersonMode
from constants import K,FPS

listTimesTotal = []
longTimesFloorList = {}

def updateLiftsState():
    for lift in listLifts:
        lift.updateState()

def updatePersonsState():
    for person in listPersons:
        person: Person
        person.updateState()
        if person.mode == PersonMode.OUT: 
            outPersonTime = person.timeTotal*K/FPS
            listTimesTotal.append(outPersonTime)
            if(outPersonTime>100):
                longTimesFloorList[person.id] = (person.startingFloor, person.wantedFloor, outPersonTime)
            
def updateListPersons():
    for person in listPersons:
        person: Person
        if(PersonMode.OUT == person.mode):
            listPersons.remove(person)
        

