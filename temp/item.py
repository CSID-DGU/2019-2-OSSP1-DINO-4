import pygame
from const import *

class item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def __call__(self):
        print (" ")

    def item_display(self,screen):
        #potion 사진 불러옴
        red_potion=pygame.image.load("tile/red-potion.png")
        blue_potion=pygame.image.load("tile/blue-potion.png")

        #아이템 화면에 표시
        screen.blit(red_potion,(50,530))
        screen.blit(blue_potion,(30,530))

        screen.blit(blue_potion,(30,460))

        screen.blit(red_potion,(300,50))
        screen.blit(blue_potion,(400,150))

        screen.blit(red_potion,(850,100))
        screen.blit(red_potion,(600,280))
        screen.blit(red_potion,(800,400))
        screen.blit(blue_potion,(600,370))

    def item_eat(self,screen,item):
        self.rect.x=300
        self.rect.y=50

        hits=pygame.sprite.spritecollide(self,self.platforms,False)
        hits_item=pygame.sprite.spritecollide(self.self.game.player)
















#
