import pygame
from const import *

class item(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        #self.screen=screen
        self.width=WIDTH
        self.height=HEIGHT

        self.redItem=[50,530,300,50,850,100,600,280,800,400]
        self.blueItem=Item=[30,530,30,460,400,150,600,370]
        #potion 사진 불러옴
        self.image=pygame.image.load("tile/red-potion.png")
        self.rect = self.image.get_rect()
        self.red_potion=pygame.image.load("tile/red-potion.png")
        self.blue_potion=pygame.image.load("tile/blue-potion.png")

        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()


    def __call__(self):
        print (" ")


    def item_display(self,screen):
        #아이템 화면에 표시
        screen.blit(self.red_potion,(50,530)) #red1
        screen.blit(self.blue_potion,(30,530))

        screen.blit(self.blue_potion,(30,460))

        screen.blit(self.red_potion,(300,50)) #red2
        screen.blit(self.blue_potion,(400,150))

        screen.blit(self.image,(850,100)) #red3
        screen.blit(self.red_potion,(600,280)) #red4
        screen.blit(self.red_potion,(800,400)) #red5
        screen.blit(self.blue_potion,(600,370))

    def item_eat_red2(self,screen,mouthOpen):
        item__=item(self)
        #red2 item
        self.rect.x=300
        self.rect.y=50
        #item과 player 충돌 검사
        hits_item=pygame.sprite.spritecollide(self,self.game.player_group,False,pygame.sprite.collide_mask)

        listLength=range(int(len(self.redItem)/2))

        if hits_item and mouthOpen:
            self.redItem=[50,530,850,100,600,280,800,400]#4
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))
        else:
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))

    def item_eat_red3(self,screen,mouthOpen):
        item__=item(self)
        self.rect.x=850
        self.rect.y=100
        #item과 player 충돌 검사
        hits_item=pygame.sprite.spritecollide(self,self.game.player_group,False,pygame.sprite.collide_mask)

        listLength=range(int(len(self.redItem)/2))

        if hits_item and mouthOpen:
            self.redItem=[50,530,600,280,800,400]#4
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))
        else:
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))

    def item_eat_red4(self,screen,mouthOpen):
        item__=item(self)
        self.rect.x=600
        self.rect.y=280
        #item과 player 충돌 검사
        hits_item=pygame.sprite.spritecollide(self,self.game.player_group,False,pygame.sprite.collide_mask)

        listLength=range(int(len(self.redItem)/2))

        if hits_item and mouthOpen:
            self.redItem=[850,100,800,400]#4
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))
        else:
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))

    def item_eat_red1(self,screen,mouthOpen):
        item__=item(self)
        self.rect.x=50
        self.rect.y=500
        #item과 player 충돌 검사
        hits_item=pygame.sprite.spritecollide(self,self.game.player_group,False,pygame.sprite.collide_mask)

        listLength=range(int(len(self.redItem)/2))

        if hits_item and mouthOpen:
            self.redItem=[]#4
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))
        else:
            for v in listLength:
                screen.blit(self.red_potion,(self.redItem[v],self.redItem[v+1]))
                v+=1
            screen.blit(self.blue_potion,(30,460))
            screen.blit(self.blue_potion,(400,150))
            screen.blit(self.blue_potion,(600,370))



















#
