from pickle import FALSE
import pygame
from constants import *

class FloorButton:
    def __init__(self,posX, posY, width, heigth, color):
        self.image = pygame.Surface((width,heigth))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX,posY)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.posX = posX
        self.posY = posY
        self.clicked = False
    
    def draw(self):
        triggerAction = False
        pos = pygame.mouse.get_pos()
        screen.blit(self.image, (self.posX, self.posY))
        #print(self.posX, self.posY)
        if (pos[0] in range(self.posX, self.posX + self.width)):
            if (pos[1] in range(self.posY, self.posY + self.height)):
                if pygame.mouse.get_pressed()[0] == 1:
                    if (self.clicked == False):
                        self.clicked = True
                        triggerAction = True
                else:
                    self.clicked = False
        return triggerAction



size = (SCREEN_WIDTH, SCREEN_HEIGTH)
screen = pygame.display.set_mode(size)
