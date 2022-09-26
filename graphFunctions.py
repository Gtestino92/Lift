from Lift import Lift

def printPosition(lift: Lift, time):
    print("t=", time, "  ",  
        "pos=", lift.position, "  " , 
        lift.mode , "  ", 
        "pendOutside=", lift.listPositionsPendingOutside, "  ", 
        "callInside=", lift.listPositionsCalledInside, "  ",
        "cant=", len(lift.listPersonsIn))
