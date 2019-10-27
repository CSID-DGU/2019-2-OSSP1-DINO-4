import pygame
from const import *

FRAME=0

class Player(pygame.sprite.Sprite):
    def __init__(self,position,game):
        #setting
        super().__init__()
        self.game=game

        #load image
        self.user_image_left=[]
        self.user_image_right=[]
        self.load_image()
        self.image=pygame.image.load("girl/girl-11.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))

        #self.mask
        self.mask=pygame.mask.from_surface(self.image)

        #self.rect
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=350

        #가속도[x의 가속도,y의 가속도]
        self.vel=[0,0]


    def load_image(self):
        idle_walk_sprite=['girl-0'+str(i)+'.png' for i in range(10)]
        idle_walk_right=[pygame.image.load('girl/'+i).convert_alpha()
                         for i in idle_walk_sprite]
        idle_walk_right=[pygame.transform.scale(i,(50,50))
                        for i in idle_walk_right]
        idle_walk_left=[pygame.transform.flip(i,True,False)
                        for i in idle_walk_right]

        self.user_image_left.append(idle_walk_left)
        self.user_image_right.append(idle_walk_right)

    def calc_gravity(self):
        if self.vel[1]==0:
            self.vel[1]=1
        else:
            self.vel[1]+=.35

        if self.rect[1]>=HEIGHT-self.rect.height and self.vel[1]>=0:
            self.vel[1]=0
            self.vel[1]=HEIGHT-self.rect.height

    def jump(self):
        #캐릭터와 배경과의 충돌 검사
        self.rect[1]+=2
        hit_list=pygame.sprite.spritecollide(self,self.game.platforms,False)
        self.rect[1]-=0.1

        if len(hit_list)>0 or self.rect.bottom>=HEIGHT:
            self.vel[1]-=10


    #왼쪽으로 움직인다(x의 가속도 -6)
    def go_left(self):
        #FRAME+=1
        #self.image=user_image_left[FRAME%10]
        self.vel[0]-=6

    #오른쪽으로 움직인다(x의 가속도 +6)
    def go_right(self):
        #self.image=user_image_right[FRAME%10]
        self.vel[0]+=6

    #멈춘다(x의 가속도 0)
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

        if self.game.BUTTON_ON==False:
            hit_list=pygame.sprite.spritecollide(self,self.game.remove_platform_,False)
            for block in hit_list:
                if self.vel[1]>0:
                    self.rect.bottom=block.rect.top
                elif self.vel[1]<0:
                    self.rect.top=block.rect.bottom

    #def teleport(self):
