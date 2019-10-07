import pygame
from const import *

FRAME=0
class Player:
    def __init__(self,path,position):
        self.user_position=[position[0],position[1]]
        self.user_image=[]
        self.load_sprites(path)    #path 경로 이미지 불러옴
        self.left=False #캐릭터가 왼쪽으로 움직이고 있는지 저장
        self.event_list=[False for i in range(EVENT)]

    def load_sprites(self,path):
        #서있음
        
        idle_stand_right=[pygame.image.load("girl/stand.png")]
        idle_stand_right=[pygame.transform.scale(i,(50,50))
                        for i in idle_stand_right]
        idle_stand_left=[pygame.transform.flip(idle_stand_right[0],True,False)]

        #걷기
        idle_walk_sprite=['girl-0'+str(i)+'.png' for i in range(10)]
        idle_walk_right=[pygame.image.load(path+i).convert_alpha()
                         for i in idle_walk_sprite]
        idle_walk_right=[pygame.transform.scale(i,(50,50))
                        for i in idle_walk_right]
        idle_walk_left=[pygame.transform.flip(i,True,False)
                        for i in idle_walk_right]

        self.user_image.append(idle_stand_right)
        self.user_image.append(idle_stand_left)
        self.user_image.append(idle_walk_right)
        self.user_image.append(idle_walk_left)
        #self.user_image.append(idle_jump)



    def EventHandler(self):
        pressed = pygame.key.get_pressed()
        self.event_list = [False for i in range(EVENT)]

        if pressed[pygame.K_RIGHT]:
            self.user_position[0] += 3
            self.event_list[WALKRIGHT] = True
            self.left = False

        elif pressed[pygame.K_LEFT]:
            self.user_position[0] -= 3
            self.event_list[WALKLEFT] = True
            self.left = True

        else:
            if self.left:
                self.event_list[LEFT] = True
                self.event_list[RIGHT] = False
            else:
                self.event_list[RIGHT] = True
                self.event_list[LEFT] = False



    def update(self, screen):
        global FRAME
        self.EventHandler()
        if self.event_list[RIGHT]:
            screen.blit(self.user_image[RIGHT][0],
                        self.user_position)
        elif self.event_list[LEFT]:
            screen.blit(self.user_image[LEFT][0],
                        self.user_position)
        elif self.event_list[WALKRIGHT]:
            FRAME+=1
            screen.blit(self.user_image[WALKRIGHT][int(FRAME/4) % 10],
                        self.user_position)
        elif self.event_list[WALKLEFT]:
            FRAME+=1
            screen.blit(self.user_image[WALKLEFT][int(FRAME/4) % 10],
                        self.user_position)

