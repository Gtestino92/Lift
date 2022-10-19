import pygame
pygame.font.init()

from enums import Floor
from Lift import listLifts
from constants import *
from Person import *
from updateFunctions import *
from graphFunctions import * 
from Graph import * 
import numpy as np
import matplotlib.pyplot as plt

t = 0
running = True

pygame.init()
pygame.display.set_caption("Lift")

clock = pygame.time.Clock()


floorButtonsList = [FloorButton(POS_FLOOR_INIT_X , POS_FLOOR_INIT_Y - floorNum * FLOOR_HEIGHT, FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR_COLOR, floorNum)  for floorNum in Floor.keys()]

createPersonCallEvent = pygame.USEREVENT
pygame.time.set_timer(createPersonCallEvent, T_EVENT_PERSON)

#### AGREGAR: VER COMO SE COMPORTA EL LIFT AL MAX DE CAPACIDAD!!!!

## TODO: AGREGAR EN EVENTO PARA VISUALIZAR LINEA TEMPORAL DE CANT PERSONS!!!
## TODO: hay un problema con algun colgado. En algun caso (apretar 4 en PB), no llama despues de ser rechazado. Quizas es por los calledLifts


while(running):
    #printPosition(listLifts[0], t)
    screen.fill("Black")

    try:
        updateLiftsState()
        updatePersonsState()
        updateListPersons()
    except Exception as err: 
        print(err)
        running = False

    for floorButton in floorButtonsList:
        triggerOut, triggerIn, floorNum = floorButton.draw()
        if (triggerOut): 
            if(floorNum == 0):
                createNewRandLeavingPerson()
            else:
                createNewRandEnteringPerson(floorNum)
        #if (triggerIn): 
        #    listLifts[0].callToPosition(floorNum)


    for liftBlock in listLiftBlocks:
        liftBlock.draw()
    
    cantPersonsWaiting = font.render(str(len(listPersons) - len(liftBlock.lift.listPersonsIn)), True, (255,255,255))
    screen.blit(cantPersonsWaiting, (0,0))
    cantPersonsOut = font.render(str(len(listTimesTotal)), True, (255,255,255))
    screen.blit(cantPersonsOut, ((SCREEN_WIDTH - cantPersonsOut.get_width()),0))

    for event in pygame.event.get():
        if event.type == createPersonCallEvent:
            createNewRandPerson()
        if event.type == pygame.QUIT : running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        
    
    if(len(listTimesTotal) >= MAX_TOTALS): running = False

    printInformation(listLifts[0], listPersons, t)
    
    
    pygame.display.update()
    clock.tick(FPS)
    t += TIMESTEP

#print("Tiempos: ", listTimesTotal) 
print("Promedio de tiempos: ", np.mean(listTimesTotal)) 
print("Desvio de tiempos: ", np.std(listTimesTotal))

print("Pisos que quedaron colgados: ", longTimesFloorList)
counts, bins = np.histogram(listTimesTotal)
plt.hist(bins[: -1], bins, weights = counts)
plt.show()

pygame.quit()


