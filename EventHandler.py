from typing import List
from Person import *
from Graph import createNewRandPerson
import pygame
from Lift import *

def handleEvents(running):
    if(running != True): return

    for event in pygame.event.get():
        if event.type == createPersonCallEvent:
            createNewRandPerson()
        if event.type in [resetBlockEvent.type for resetBlockEvent in resetBlockLiftEventDict.values()]:
            liftIdBlocked = event.liftId
            for lift in listLifts:
                if lift.id == liftIdBlocked:
                    lift.mode = LiftMode.STOP

        if event.type == pygame.QUIT : running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        
    if(len(listTimesTotal) >= MAX_TOTALS): running = False

    return running
    
def handleBlockingLifts():
    for lift in listLifts:
        if(LiftMode.SET_BLOCK == lift.mode):
            event = resetBlockLiftEventDict[lift.id]
            pygame.time.set_timer(event, T_BLOCK_TIMER, 1) 
            lift.mode = LiftMode.BLOCK

createPersonCallEvent = pygame.USEREVENT
pygame.time.set_timer(createPersonCallEvent, T_EVENT_PERSON)

resetBlockLiftEventDict = { lift.id : pygame.event.Event(pygame.USEREVENT + 1 + lift.id, liftId = lift.id) for lift in listLifts}
listLiftIds = [lift.id for lift in listLifts]
