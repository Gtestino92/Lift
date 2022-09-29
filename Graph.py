from pickle import FALSE
import pygame
from constants import *
from Lift import Lift
from enums import Floor

class LiftBlock:
    def __init__(self,posX, posY, width, heigth, lift: Lift, color):
        self.image = pygame.Surface((width,int(heigth*19/20)))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX,posY)
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.posX = posX
        self.posY = posY
        self.lift = lift
        self.clicked = False
    
    def draw(self):
        self.posY = POS_LIFT_INIT_Y - (int(self.lift.position * FLOOR_HEIGHT))
        screen.blit(self.image, (self.posX, self.posY))
        

class FloorButton:
    def __init__(self,posX, posY, width, heigth, color, floor: Floor):
        self.image = pygame.Surface((width,heigth))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX,posY)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.posX = posX
        self.posY = posY
        self.floor = floor
        self.clicked = False
    
    def draw(self):
        triggerAction = False
        self.color = FLOOR_COLOR_PRESSED if self.clicked else FLOOR_COLOR
        self.image.fill(self.color)
        buttonPos = (self.posX, self.posY)
        mousePos = pygame.mouse.get_pos()
        screen.blit(self.image, buttonPos)
        border = pygame.Surface((self.width, int(self.height/20)))
        border.fill("Red")
        screen.blit(border, buttonPos)
        
        
        if (mousePos[0] in range(self.posX, self.posX + self.width)):
            if (mousePos[1] in range(self.posY, self.posY + self.height)):
                if pygame.mouse.get_pressed()[0] == 1:
                    if (self.clicked == False):
                        self.clicked = True
                        triggerAction = True
                else:
                    self.clicked = False
        return triggerAction, self.floor

size = (SCREEN_WIDTH, SCREEN_HEIGTH)
screen = pygame.display.set_mode(size)
