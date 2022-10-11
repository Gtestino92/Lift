from Lift import listLifts
from Person import listPersons, Person
from enums import PersonMode
from constants import K,FPS

listTimesTotal = []

def updateLiftsState():
    for lift in listLifts:
        lift.updateState()

def updatePersonsState():
    for person in listPersons:
        person: Person
        person.updateState()
        if person.mode == PersonMode.OUT: listTimesTotal.append(person.timeTotal*K/FPS)

def updateListPersons():
    for person in listPersons:
        person: Person
        if(PersonMode.OUT == person.mode):
            listPersons.remove(person)
        elif(PersonMode.INIT == person.mode):
            person.callLift(listLifts[0])

