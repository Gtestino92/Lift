from typing import List
from Lift import Lift
from Person import Person
from constants import FPS, K

def printInformation(lift: Lift, listPersons: List[Person]):
    print("pos=", lift.position, "  " , 
            lift.mode , "  ", 
        "pendOutside=", lift.listPositionsPendingOutside, "  ", 
        "callInside=", lift.listPositionsCalledInside, "  ",
        "cantIn=", len(lift.listPersonsIn), " ",
        "cantPersons=", len(listPersons), "  ",)