import pygame
from item import *
from background import *
from player import *
from const import *

FRAME=0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h,case):
        super().__init__()
        if case==1:
            self.image=pygame.image.load("tile/platform_tile_002.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(100,30))
        elif case==2:
            self.image=pygame.image.load("tile/platform_tile_009.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(100,60))
        elif case==3:
            self.image=pygame.image.load("tile/platform_tile_032.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(100,20))
        elif case==4:
            self.image=pygame.image.load("tile/platform_tile_005.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(30,100))
        elif case==5:
            self.image=pygame.image.load("tile/platform_tile_021.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(70,70))
        elif case==6:
            self.image=pygame.image.load("tile/platform_tile_016.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(100,30))
        elif case==7:
            self.image=pygame.image.load("tile/platform_tile_038.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(30,30))
    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game:
    def __init__(self):
        self.width=900
        self.height=600
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()

    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    self.player1.jump()
                if event.key==pygame.K_LEFT:
                    self.player1.go_left()
                if event.key==pygame.K_RIGHT:
                    self.player1.go_right()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT and self.player1.vel[0]<0:
                    self.player1.stop()
                if event.key==pygame.K_RIGHT and self.player1.vel[0]>0:
                    self.player1.stop()

    def main(self):
        global FRAME
<<<<<<< HEAD
=======
        self.all_sprites=pygame.sprite.Group()
        self.platforms=pygame.sprite.Group()
>>>>>>> character

        pygame.init()
        self.player1=Player((self.width/2,self.height/2),self)
        self.all_sprites.add(self.player1)

        for plat in PlatformList:
            p=Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        background_=background(self.width,self.height)
        item_=item(self.width,self.height)
        #trap_=trap(self.width,self.height)

        while True:
            time=self.clock.tick(60)
            FRAME+=1
            self.screen.fill((255,193,158))
            background_.background(self.screen)
<<<<<<< HEAD
            item_.item(self.screen)
            #trap_.trap(self.screen)
=======

            self.event()
            self.all_sprites.update()
            if self.player1.rect.right>WIDTH:
                player1.rect.right=WIDTH
            
            if self.player1.rect.left<0:
                player1.rect.left=0

            self.all_sprites.draw(self.screen)
>>>>>>> character

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

