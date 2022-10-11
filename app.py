from cmath import e
from tkinter import E
from venv import create
from enums import Floor
from Lift import listLifts
from constants import *
from Person import *
from updateFunctions import *
from graphFunctions import * 
import pygame
from Graph import * 
import numpy as np
import matplotlib.pyplot as plt

t = 0
running = True

pygame.init()
pygame.display.set_caption("Lift")

clock = pygame.time.Clock()


liftBlock = LiftBlock(POS_LIFT_INIT_X, POS_LIFT_INIT_Y, LIFT_WIDTH, LIFT_HEIGHT, listLifts[0], "White") 

floorButtonsList = [FloorButton(POS_FLOOR_INIT_X , POS_FLOOR_INIT_Y - floorNum * FLOOR_HEIGHT, FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR_COLOR, floorNum)  for floorNum in Floor.keys()]

createPersonCallEvent = pygame.USEREVENT
pygame.time.set_timer(createPersonCallEvent, T_EVENT_PERSON)


#### AGREGAR: VER COMO SE COMPORTA EL LIFT AL MAX DE CAPACIDAD!!!!

## TODO: AGREGAR EN EVENTO PARA VISUALIZAR LINEA TEMPORAL DE CANT PERSONS!!!

while(running):
    #printPosition(listLifts[0], t)
    try:
        updateLiftsState()
    except Exception as err: 
        print(err)
        running = False
    updatePersonsState()
    updateListPersons()

    screen.fill("Black")
    for floorButton in floorButtonsList:
        triggerOut, triggerIn, floorNum = floorButton.draw()
        if (triggerOut): 
            listLifts[0].callFromPosition(floorNum)
        #if (triggerIn): 
        #    listLifts[0].callToPosition(floorNum)


    liftBlock.draw()
    
    for event in pygame.event.get():
        if event.type == createPersonCallEvent:
            createNewRandPerson()
        if event.type == pygame.QUIT : running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        
    
    if(len(listTimesTotal) == MAX_TOTALS): running = False

    printInformation(listLifts[0], listPersons, t)
    
    
    pygame.display.update()
    clock.tick(FPS)
    t += TIMESTEP

print("Tiempos: ", listTimesTotal) 
print("Promedio de tiempos: ", np.mean(listTimesTotal)) 
print("Desvio de tiempos: ", np.std(listTimesTotal))
pygame.quit()

#counts, bins = np.histogram(listTimesTotal)
#plt.hist(bins[:-1], bins, weights=counts)
#plt.show()

