from enums import Floor
from Lift import listLifts
from constants import *
from Person import *
from updateFunctions import *
from graphFunctions import * 
import sys, pygame
from Graph import * 

t = 0
running = True

pygame.init()
pygame.display.set_caption("Lift")

clock = pygame.time.Clock()


liftBlock = LiftBlock(POS_LIFT_INIT_X, POS_LIFT_INIT_Y, LIFT_WIDTH, LIFT_HEIGHT, listLifts[0], "White") 

floorButtonsList = [FloorButton(POS_FLOOR_INIT_X , POS_FLOOR_INIT_Y - floorNum * FLOOR_HEIGHT, FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR_COLOR, floorNum)  for floorNum in Floor.keys()]



### CASO: APRETAR 9 con izq, y en un piso de abajo con el der mientras está subiendo
while(running):
    #printPosition(listLifts[0], t)
    updateLiftsState()
    updatePersonsState()
    personNumber = 0
    screen.fill("Black")
    for floorButton in floorButtonsList:
        triggerOut, triggerIn, floorNum = floorButton.draw()
        if (triggerOut): 
            listLifts[0].callFromPosition(floorNum)
        if (triggerIn): 
            listLifts[0].callToPosition(floorNum)

    liftBlock.draw()
    print(listLifts[0].listPositionsPendingOutside, " ", listLifts[0].listPositionsCalledInside)

    #if(t == T1):
    #    listPersons[0].callLift(listLifts[0]) 
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT : running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        ##elif event.type == 
        
    
    #printPosition(listLifts[0], t)
    
    
    pygame.display.update()
    clock.tick(FPS)
    t += TIMESTEP
    
pygame.quit()


###
# PEND: CORREGIR TIMER, CORREGIR POS DEL BLOCK
