import pygame
import face_recog
from background import *
from player import *
from const import *
from item import *
from trap import *
from shot import *
import sys
import os
import dlib
import glob
from skimage import io
import numpy as np
import cv2



FRAME=0

#배경 벽 불러옴
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
        self.fire_rect=[530,40]

    #key 입력에 따른 이벤트처리
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    self.shot_.shooting_setting(self.player1.rect.x+30,self.player1.rect.y+10)
                if event.key==pygame.K_UP:
                    self.player1.jump()
                    print(2)
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
        #sprite 그룹 생성
        self.all_sprites=pygame.sprite.Group()
        self.platforms=pygame.sprite.Group()
        self.player_group=pygame.sprite.Group()

        pygame.init()

        #sprite 그룹에 sprite 추가
        self.player1=Player((self.width/2,self.height/2),self)
        self.all_sprites.add(self.player1)
        self.player_group.add(self.player1)


        #배경 벽 불러옴
        for plat in PlatformList:
            p=Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        #초기화
        trap1=trap(self)
        background_=background(self.width,self.height)
        item_=item(self)
        self.shot_=shot(self.screen,self)
        item_.item_display(self.screen) #아이템은 사라질 수 있으므로 while 밖
        face=face_recog.face(self)



        while True:
            while (face.cap.isOpened()):
                time=self.clock.tick(60)
                FRAME+=1
                self.screen.fill((255,193,158))

                #배경 그림
                background_.background(self.screen)
                trap1.trap_draw(self.screen,self.fire_rect)
                self.shot_.shooting()

                self.event()
                self.all_sprites.update()


                #플레이어가 창 밖으로 나가지 못하게
                if self.player1.rect.right>WIDTH:
                    self.player1.rect.right=WIDTH
                if self.player1.rect.left<0:
                    self.player1.rect.left=0

                self.all_sprites.draw(self.screen)
                mouthOpen=face.face_recognition(self.screen)
                item_.item_eat(self.screen,mouthOpen)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)
