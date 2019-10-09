import pygame

class item:

    def __init__(self,width,height):
        self.width=width;
        self.height=height;

    def __call__(self):
        print (" ")

    def item(self,screen):
        red_potion=pygame.image.load("tile/red-potion.png")
        blue_potion=pygame.image.load("tile/blue-potion.png")


        #바닥 맨 아래
        screen.blit(red_potion,(50,550))
        screen.blit(blue_potion,(30,550))

        screen.blit(blue_potion,(30,460))

        screen.blit(red_potion,(300,50))
        screen.blit(blue_potion,(400,150))

        screen.blit(red_potion,(850,100))
        screen.blit(red_potion,(600,280))
        screen.blit(red_potion,(800,400))
        screen.blit(blue_potion,(600,370))
