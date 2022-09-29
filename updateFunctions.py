from Lift import listLifts
from Person import listPersons

def updateLiftsState():
    for lift in listLifts:
        lift.updateState()

def updatePersonsState():
    for person in listPersons:
        person.updateState()
