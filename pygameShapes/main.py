#Random art generator with shapes
# With pygame
# Created by Ankith Kumar

import pygame, sys # Imports necessary libraries
import random
import eventListener #my custom module


pygame.init() 
screen = pygame.display.set_mode([1080, 900])#Creates window size [1080, 900]
screen.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]) #Window random background
eventListener.listen(screen)#starts eventlistener & shapeGenerators


           
