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
from EventHandler import *

running = True

pygame.init()
pygame.display.set_caption("Lift")

clock = pygame.time.Clock()

## TODO: AGREGAR EN EVENTO PARA VISUALIZAR LINEA TEMPORAL DE CANT PERSONS?

while(running):
    screen.fill("Black")
    drawMetrics()

    for floorButton in floorButtonsList:
        floorButton.draw()

    for liftBlock in listLiftBlocks:
        liftBlock.draw()

    for personBlock in listPersonBlocks:
        personBlock.draw()

    try:
        updateLiftsState()
        updatePersonsState()
        updateListPersons()
    except Exception as err: 
        print(err)
        running = False
    
    running = handleEvents(running)
    
    handleBlockingLifts()

    printInformation(listLifts[0], listPersons)

    pygame.display.update()
    clock.tick(FPS)

#print("Tiempos: ", listTimesTotal) 
print("Promedio de tiempos: ", np.mean(listTimesTotal)) 
print("Desvio de tiempos: ", np.std(listTimesTotal))

print("Tiempos mucha espera: ", longTimesFloorsList) 

counts, bins = np.histogram(listTimesTotal)
plt.hist(bins[: -1], bins, weights = counts)
plt.show()

pygame.quit()


