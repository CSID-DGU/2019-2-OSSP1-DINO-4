import pygame
from const import *

FRAME=0

class Dino(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        super().__init__()

        self.game=game
        self.user_position=[x,y]
        self.user_image=[]
        self.event_list=[False for i in range(2)]
        self.load_sprites()

        self.is_right=True
        self.walk_distance=x

        
    def load_sprites(self):
        #걷기
        path="dino/"
        walk_sprite=['dino-0'+str(i)+'.png' for i in range(1,8)]
        walk_right=[pygame.image.load(path+i).convert_alpha()
                         for i in walk_sprite]
        walk_right=[pygame.transform.scale(i,(80,80))
                        for i in walk_right]
        walk_left=[pygame.transform.flip(i,True,False)
                        for i in walk_right]

        self.user_image.append(walk_right)
        self.user_image.append(walk_left)

        

    def EventHandler(self):
        global FRAME
        FRAME+=0.3

        if self.is_right:
            if self.user_position[0]>self.walk_distance+20:
                self.is_right=False
            else:
                self.user_position[0] += 0.5

        else:
            if self.user_position[0]<self.walk_distance-20:
                self.is_right=True
            else:
                self.user_position[0] -= 0.5
            

    def update(self,screen):
        self.EventHandler()

        if self.is_right==True:
            screen.blit(self.user_image[0][int(FRAME)%7],self.user_position)
            self.rect=self.user_image[0][int(FRAME)%7].get_rect()
            self.mask=pygame.mask.from_surface(self.user_image[0][int(FRAME)%7])

        else:
            screen.blit(self.user_image[1][int(FRAME)%7],self.user_position)
            self.rect=self.user_image[1][int(FRAME)%7].get_rect()
            self.mask=pygame.mask.from_surface(self.user_image[1][int(FRAME)%7])