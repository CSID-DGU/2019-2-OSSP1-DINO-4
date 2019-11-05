import pygame
import face_recog
from background import *
from player import *
from const import *
from item import *
from trap import *
from shot import *
from button_detect import *
from dino import *
from gameover import *
import sys
import os
import dlib
import glob
from skimage import io
import numpy as np
from network import *
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

class platform_remove(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        super().__init__()
        self.image=pygame.image.load("tile/platform_tile_016.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,30))

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Game:
    def __init__(self):
        self.width=900
        self.height=600
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()
        self.fire_rect=[530,40]
        self.BUTTON_ON1=False
        self.DINO_alive=True
        self.left=False

    #key 입력에 따른 이벤트처리
    def event(self):
        self.player1.event_list = [False for i in range(EVENT)]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    bulletX=self.player1.rect.x
                    bulletY=self.player1.rect.y
                    self.shot_.shooting_setting(bulletX+30,bulletY+10)
                if event.key==pygame.K_UP:
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
        self.player1.user_position[0]=self.player1.rect.x
        self.player1.user_position[1]=self.player1.rect.y

    #network로 data 전송
    def send_data(self):
        """
        Send position to server
        :return: None
        """
        data = str(self.net.id) + ":" + str(self.player1.rect.x) + "," + str(self.player1.rect.y)
        reply = self.net.send(data)
        return reply

    #전송할 데이터를 parse하는 함수
    def parse_data(self,data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0

    def main(self):
        global FRAME
        global GAME_OVER,GAME_OVER_FIRE,GAME_OVER_ARROW
        global GAME_START
        #sprite 그룹 생성
        #충돌 검사를 위해
        self.all_sprites=pygame.sprite.Group()
        self.platforms=pygame.sprite.Group()
        self.remove_platform_=pygame.sprite.Group()
        self.player_group=pygame.sprite.Group()
        #self.button1=pygame.sprite.Group()
        self.dino_group=pygame.sprite.Group()
        self.arrow_sprites=pygame.sprite.Group()
        self.water_sprites=pygame.sprite.Group()

        pygame.init()

        #sprite 그룹에 추가할 sprite 선언
        self.player1=Player(self)
        self.player2=Player(self)# 추가
        self.net=Network()
        self.button1=button_image(self)
        self.dino_1=Dino(self,100,125) #100,125

        self.arrow_trap1=arrow(self,585,130)
        self.arrow_trap2=arrow(self,170,470)
        self.arrow_trap3=arrow(self,500,550)
        self.arrow_trap4=arrow(self,150,330)
        #self.water1=water(self,600,400)
        #self.water2=water(self,800,300)
        #self.water3=water(self,700,300)


        #sprite 그룹에 sprite 추가
        self.all_sprites.add(self.player1)
        self.player_group.add(self.player1)
        self.all_sprites.add(self.player2) #2추가
        self.player_group.add(self.player2) #2추가
        self.platforms.add(self.button1)
        self.dino_group.add(self.dino_1)
        self.arrow_sprites.add(self.arrow_trap1,self.arrow_trap2,self.arrow_trap3,self.arrow_trap4)
        #self.water_sprites.add(self.water1,self.water2,self.water3)

        #배경 벽 불러옴
        for plat in PlatformList:
            p=Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        for plat in remove_platform:
            p=platform_remove(*plat)
            self.remove_platform_.add(p)

        #선언 및 초기화
        teleport_=teleport(self)
        fire_trap=bomb(self)
        detect_button1=button_detect()
        background_=background(self.width,self.height)
        item_=item(self)
        self.shot_=shot(self.screen,self)
        item_.item_display(self.screen) #아이템은 사라질 수 있으므로 while 밖
        #face=face_recog.face(self)
        gameover_=gameover(self.screen,self.clock)
        n=Network()

        #2플레이어 게임 연결
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")

        while True:

            if GAME_OVER or GAME_OVER_FIRE or GAME_OVER_ARROW:
                gameover_.show_gameover_screen()

                #새로운 게임 시작 위해 다시 초기화
                self.all_sprites=pygame.sprite.Group()
                self.platforms=pygame.sprite.Group()
                self.remove_platform_=pygame.sprite.Group()
                self.player_group=pygame.sprite.Group()
                self.button1=pygame.sprite.Group()
                self.dino_group=pygame.sprite.Group()
                self.arrow_sprites=pygame.sprite.Group()
                self.water_sprites=pygame.sprite.Group()
                self.BUTTON_ON1=False

                self.player1=Player(self)
                self.button1=button_image(self)
                self.dino_1=Dino(self,100,125) #100,125
                self.arrow_trap1=arrow(self,585,130)
                self.arrow_trap2=arrow(self,170,470)
                self.arrow_trap3=arrow(self,500,550)
                self.arrow_trap4=arrow(self,150,330)
                #self.water1=water(self,600,400)
                #self.water2=water(self,800,300)
                #self.water3=water(self,700,300)

                self.all_sprites.add(self.player1)
                self.player_group.add(self.player1)
                self.all_sprites.add(self.player2)#p2
                self.player_group.add(self.player2)#p2
                self.platforms.add(self.button1)
                self.dino_group.add(self.dino_1)
                self.arrow_sprites.add(self.arrow_trap1,self.arrow_trap2,self.arrow_trap3,self.arrow_trap4)
                #self.water_sprites.add(self.water1,self.water2,self.water3)

                #배경 벽 불러옴
                for plat in PlatformList:
                    p=Platform(*plat)
                    self.all_sprites.add(p)
                    self.platforms.add(p)

                for plat in remove_platform:
                    p=platform_remove(*plat)
                    self.remove_platform_.add(p)
                GAME_OVER=False
                GAME_OVER_FIRE=False
                GAME_OVER_ARROW=False

            time=self.clock.tick(60)
            FRAME+=1
            self.screen.fill((255,193,158))

            #배경
            background_.background(self.screen)
            # trap1.trap_draw(self.screen,self.fire_rect)

            #폭탄제어
            GAME_OVER_FIRE=fire_trap.bomb_draw(self.screen,self.fire_rect)

            #버튼제어
            self.button1.button_draw(self.screen)
            detect_button1.detect(self.screen,self)

            #창살제어
            GAME_OVER_ARROW=self.arrow_trap1.arrow_player_detect()

            #공룡제어
            if self.DINO_alive==True:
                self.dino_1.update(self.screen)

            #공격제어
            self.shot_.shooting()
            self.shot_.shoot_dino(self)


            #순간이동
            teleport_.sprite_def(self,self.player1)
            if(teleport_.ready==True):
                teleport_.collide_detect(self)

            #플레이어가 창 밖으로 나가지 못하게
            if self.player1.rect.right>WIDTH:
                self.player1.rect.right=WIDTH
            if self.player1.rect.left<0:
                self.player1.rect.left=0

            self.player2.rect.x,self.player2.rect.y=self.parse_data(self.send_data())

            self.player2.update_sprite(self.screen,self)#추가ㄹ
            self.player2.update()
            self.player1.update_sprite(self.screen,self)
            self.all_sprites.update()

            self.all_sprites.draw(self.screen)
            if self.BUTTON_ON1==False:
                self.remove_platform_.draw(self.screen)

            #얼굴 인식
            #mouthOpen=face.face_recognition(self.screen)
            #item_.item_eat_red2(self.screen,mouthOpen)
            #item_.item_eat_red3(self.screen,mouthOpen)
            #item_.item_eat_red4(self.screen,mouthOpen)
            #item_.item_eat_red1(self.screen,mouthOpen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
