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

PosBlockInitX = int(SCREEN_WIDTH/2)  - int(BLOCK_WIDTH/2)

PosBlockInitY = SCREEN_HEIGTH-BLOCK_HEIGHT
whiteBlock = FloorButton(PosBlockInitX, PosBlockInitY, BLOCK_WIDTH, BLOCK_HEIGHT, "White") 

liftBlock = FloorButton(PosBlockInitX, PosBlockInitY, BLOCK_WIDTH, BLOCK_HEIGHT, "White") 

person2.callLift(listLifts[0])  

while(running):
    #printPosition(listLifts[0], t)
    updateLiftsState()
    updatePersonsState()
    screen.fill("Black")
    #if(t == T1):
    #    person2.callLift(listLifts[0])  
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT : running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        ##elif event.type == 
        
    #if(whiteBlock.draw()): print("CLICK")
    print(listLifts[0].position, whiteBlock.posY)

    whiteBlock.posY = PosBlockInitY - (int(listLifts[0].position * BLOCK_HEIGHT))
    
    whiteBlock.draw()
    
    #printPosition(listLifts[0], t)

    
    pygame.display.update()
    clock.tick(FPS)
    t += TIMESTEP
    
pygame.quit()


###
# PEND: CORREGIR TIMER, CORREGIR POS DEL BLOCK
