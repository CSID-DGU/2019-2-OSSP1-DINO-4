import pygame
from const import *

class item:
    def __init__(self):
        self.width=WIDTH
        self.height=HEIGHT

    def __call__(self):
        print (" ")

    def item_display(self,screen):
        red_potion=pygame.image.load("tile/red-potion.png")
        blue_potion=pygame.image.load("tile/blue-potion.png")

        #아이템 표시
        screen.blit(red_potion,(50,530))
        screen.blit(blue_potion,(30,530))

        screen.blit(blue_potion,(30,460))

        screen.blit(red_potion,(300,50))
        screen.blit(blue_potion,(400,150))

        screen.blit(red_potion,(850,100))
        screen.blit(red_potion,(600,280))
        screen.blit(red_potion,(800,400))
        screen.blit(blue_potion,(600,370))
