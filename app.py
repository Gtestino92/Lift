from asyncio import events
import time
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

floorButton = FloorButton(POS_FLOOR_INIT_X, POS_FLOOR_INIT_Y, FLOOR_WIDTH, FLOOR_HEIGHT, "Blue") 

person2.callLift(listLifts[0])  

while(running):
    #printPosition(listLifts[0], t)
    updateLiftsState()
    updatePersonsState()
    screen.fill("Black")
    clicked = floorButton.draw()
    liftBlock.draw()

    if(t == T1):
        person1.callLift(listLifts[0])  
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT : running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        ##elif event.type == 
        
    if(clicked): print("CLICK")
    
    printPosition(listLifts[0], t)

    
    pygame.display.update()
    clock.tick(FPS)
    t += TIMESTEP
    
pygame.quit()


###
# PEND: CORREGIR TIMER, CORREGIR POS DEL BLOCK
