import pygame
from const import *

FRAME=0

WHITE=(255,255,255)

class Player(pygame.sprite.Sprite):
    def __init__(self,position,game):
        #setting
        super().__init__()
        self.image=pygame.Surface([player_width,player_height])
        self.image.fill(WHITE)

        self.game=game
        self.rect=self.image.get_rect()
        self.vel=[0,0]


    def calc_gravity(self):
        if self.vel[1]==0:
            self.vel[1]=1
        else:
            self.vel[1]+=.35

        if self.rect[1]>=HEIGHT-self.rect.height and self.vel[1]>=0:
            self.vel[1]=0
            self.vel[1]=HEIGHT-self.rect.height

    def jump(self):
        self.rect[1]+=2
        hit_list=pygame.sprite.spritecollide(self,self.game.platforms,False)
        self.rect[1]-=0.1

        if len(hit_list)>0 or self.rect.bottom>=HEIGHT:
            self.vel[1]-=10

    def go_left(self):
        self.vel[0]-=6

    def go_right(self):
        self.vel[0]+=6
    
    def stop(self):
        self.vel[0]=0

    def update(self):
        self.calc_gravity()

        self.rect.x+=self.vel[0]
        hit_list=pygame.sprite.spritecollide(self,self.game.platforms,False)
        for block in hit_list:
            if self.vel[0]>0:
                self.rect.right=block.rect.left
            elif self.vel[0]<0:
                self.rect.left=block.rect.right
        
        self.rect.y+=self.vel[1]
        hit_list=pygame.sprite.spritecollide(self,self.game.platforms,False)
        for block in hit_list:
            if self.vel[1]>0:
                self.rect.bottom=block.rect.top
            elif self.vel[1]<0:
                self.rect.top=block.rect.bottom

            self.vel[1]=0