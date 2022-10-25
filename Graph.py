import pygame
from constants import *
from Lift import Lift, listLifts
from Person import Person, listPersons, listTimesTotal
from enums import Floor, PersonMode

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
        cantInLift = font.render(str(len(self.lift.listPersonsIn)), True, (0,0,0))
        screen.blit(cantInLift, (self.posX + self.width/2 - cantInLift.get_width()/2, self.posY))


class PersonBlock():
    def __init__(self,posX, posY, width, heigth, person: Person):
        self.image = pygame.Surface((width,int(heigth*18/20)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX,posY)
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        self.posX = posX
        self.posY = posY
        self.person = person
    
    def draw(self):
        if(self.person.mode == PersonMode.IN): return
        if(self.person.mode == PersonMode.OUT): return
        self.posY = POS_PERSON_INIT_Y - (int(self.person.floor * FLOOR_HEIGHT))
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
        self.rightClicked = False
        self.leftClicked = False
    
    def draw(self):
        triggerActionOut = False
        triggerActionIn = False
        if(self.leftClicked):
            self.color = FLOOR_COLOR_PRESSED_LEFT
        elif(self.rightClicked):
            self.color = FLOOR_COLOR_PRESSED_RIGHT
        else: 
            self.color = FLOOR_COLOR
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
                    if (self.leftClicked == False):
                        self.leftClicked = True
                        triggerActionOut = True
                else:
                    self.leftClicked = False
                if pygame.mouse.get_pressed()[2] == 1:
                    if (self.rightClicked == False):
                        self.rightClicked = True
                        triggerActionIn = True
                else:
                    self.rightClicked = False
        
        return triggerActionOut, triggerActionIn, self.floor

def drawMetrics():
    cantPersonsWaiting = font.render(str(len(listPersons)), True, (255,255,255))
    screen.blit(cantPersonsWaiting, (0,0))
    cantPersonsOut = font.render(str(len(listTimesTotal)), True, (255,255,255))
    screen.blit(cantPersonsOut, ((SCREEN_WIDTH - cantPersonsOut.get_width()),0))
    

size = (SCREEN_WIDTH, SCREEN_HEIGTH)
screen = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 32)

liftBlockMiddle = LiftBlock(POS_LIFT_INIT_X, POS_LIFT_INIT_Y, LIFT_WIDTH, LIFT_HEIGHT, listLifts[0], "White") 
floorButtonsList = [FloorButton(POS_FLOOR_INIT_X , POS_FLOOR_INIT_Y - floorNum * FLOOR_HEIGHT, FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR_COLOR, floorNum)  for floorNum in Floor.keys()]

listLiftBlocks = [liftBlockMiddle]
listPersonBlocks = []