import time
from Lift import listLifts
from enums import Floor
from constants import *
from Lift import Lift
from Person import *
from updateFunctions import *
from graphFunctions import * 

t = 0
running = True

#BEGIN
person1.callLift(listLifts[0])


while(running):
    printPosition(listLifts[0], t)
    updateLiftsState()
    updatePersonsState()
    time.sleep(float(TIMESTEP))
    
    if(t == T1):
        person2.callLift(listLifts[0])  
    #if(t == T2):
    #    person3.callLift(liftMiddle)  
    if(t > END ): 
        running = False
    t += TIMESTEP
    
exit()

