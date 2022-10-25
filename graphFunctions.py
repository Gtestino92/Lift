from typing import List
from Graph import PersonBlock
from Lift import Lift
from Person import Person
from constants import FPS, K

def printInformation(lift: Lift, listPersonBlocks: List[PersonBlock]):
    print("pos=", lift.position, "  " , 
            lift.mode , "  ", 
        "pendOutside=", lift.listPositionsPendingOutside, "  ", 
        "callInside=", lift.listPositionsCalledInside, "  ",
        "cantIn=", len(lift.listPersonsIn), " ",
        "cantPersons=", len(listPersonBlocks))