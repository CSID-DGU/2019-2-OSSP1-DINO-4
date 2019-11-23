import pygame
import sys
from pygame.locals import *

from camera import *
from background_platform import *
from player import *
from teleport import *
from background import *
from gameover import *
from trap import *
from shot import *
from item import *
from button_detect import *
from os import path

import time
import face_recog

global FPS
global clock
global time_spent

#shot.py에 #총알 창 밖으로 나가면 초기화부분 맵 최종결정난 후 수정 필요

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

class Game:
    def __init__(self):

        self.WIDTH=1000
        self.HEIGHT=700

        #캐릭터의 움직임
        self.up=False
        self.left=False
        self.right=False
        self.down=False

        #캐릭터 움직임(총알 방향 위해 필요)
        self.ex_left=False
        self.ex_right=False

        #버튼 눌렸는지 확인
        self.BUTTON_ON1=False

        self.screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.screen_rect=self.screen.get_rect()

        self.background=pygame.image.load("environment/layers/back.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(1000,700))
        self.background_rect = self.background.get_rect()

        self.load_data() #high score data load
        self.score=0
        self.start_time=0

        #불 폭탄 떨어지는 초기위치 설정
        self.fire_rect1=[1950,1200]
        self.fire_rect2=[2000,1200]
        self.fire_Rect3=[2100,1200]

        self.gameover=True

    #high score data load
    def load_data(self):
        HS_FILE="highscore.txt"
        self.dir=path.dirname(__file__)
        with open(path.join(self.dir,HS_FILE),'w') as f:
            try:
                self.highscore=int(f.read())
            except:
                self.highscore=0


    def tps(self,orologio,fps):
        temp = orologio.tick(fps)
        tps = temp / 1000.
        return tps

    #key event처리
    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.up=True
                if event.key==pygame.K_DOWN:
                    self.down=True
                if event.key==pygame.K_LEFT:
                    self.left=True
                if event.key==pygame.K_RIGHT:
                    self.right=True
                if event.key==pygame.K_SPACE and self.shot_.bullet_state is "ready":
                    bulletX=self.player.rect.x
                    bulletY=self.player.rect.y
                    self.shot_.shooting_setting(bulletX+30,bulletY+10)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.up=False
                if event.key==pygame.K_DOWN:
                    self.down=False
                if event.key==pygame.K_LEFT:
                    self.left=False
                    self.ex_left=True
                    self.ex_right=False
                if event.key==pygame.K_RIGHT:
                    self.right=False
                    self.ex_left=False
                    self.ex_right=True


    def main(self):
        global GAME_OVER_FIRE,GAME_OVER_ARROW
        #spite_group 정의
        self.all_sprite=pygame.sprite.Group()
        self.player_sprite=pygame.sprite.Group()
        self.arrow_sprites=pygame.sprite.Group()

        #초기화
        FPS=30
        clock = pygame.time.Clock()
        self.background_=background() #sprite 아닌 background
        teleport_=teleport(self) #teleport
        box_=box() #box
        fire_bomb1=bomb(self) #폭탄1
        fire_bomb2=bomb(self) #폭탄2
        fire_bomb3=bomb(self) #폭탄3
        self.shot_=shot(self) #총알


        #아이템
        item1=item(self)
        item2=item(self)
        item3=item(self)
        item4=item(self)
        item5=item(self)
        item6=item(self)
        item7=item(self)
        item8=item(self)
        item9=item(self)
        item10=item(self)
        item11=item(self)


        #창살
        self.arrow_trap1=arrow(self,360,620,0)
        self.arrow_trap2=arrow(self,1840,1420,0)
        self.arrow_trap3=arrow(self,1880,1420,0)
        self.arrow_trap4=arrow(self,1920,1420,0)
        self.arrow_trap5=arrow(self,1960,1420,0)
        self.arrow_trap6=arrow(self,2000,1420,0)
        self.arrow_trap7=arrow(self,2040,1420,0)
        self.arrow_trap8=arrow(self,2080,1420,0)
        self.arrow_trap9=arrow(self,2120,1420,0)
        self.arrow_trap10=arrow(self,2160,1420,0)
        self.arrow_trap11=arrow(self,2100,1420,0)
        self.arrow_trap12=arrow(self,2140,1420,0)
        self.arrow_trap13=arrow(self,2180,1420,0)
        self.arrow_trap14=arrow(self,2120,1420,0)

        #버튼
        self.button_detect_1=button_detect() #버튼 바꼈는지 확인
        self.button1=button_image(self) #버튼 눌렸을 때 이미지 바꿔줌

        #레벨,플레이어,배경sprite
        level = Level("level1")
        level.create_level(0,0,self)
        self.world = level.world
        self.player = level.player

        
        #sprite 그룹에 sprite 추가
        self.arrow_sprites.add(self.arrow_trap1,self.arrow_trap2,self.arrow_trap3,self.arrow_trap4,self.arrow_trap5,self.arrow_trap6,\
            self.arrow_trap7,self.arrow_trap8,self.arrow_trap9,self.arrow_trap10,self.arrow_trap11,self.arrow_trap12,self.arrow_trap13,self.arrow_trap14)
        self.world.append(self.button1)

        #함수정의
        pygame.init()

        self.camera = Camera(self.screen, self.player.rect, level.get_size()[0], level.get_size()[1])
        FONT = pygame.font.SysFont("Sans", 20)
        gameover_=gameover(self.screen,clock,self.highscore,FONT)
        face=face_recog.face(self)

        #시간 표시 글자색
        TEXT_COLOR=(0,0,0)
        BG_COLOR=(255,255,255)
        while True:
            #Gameover
            if self.gameover or GAME_OVER_FIRE or GAME_OVER_ARROW:
                gameover_.show_gameover_screen(self.score,self.dir)
                #재초기화
                self.up=False
                self.down=False
                self.right=False
                self.left=False

                self.BUTTON_ON1=False

                self.all_sprite=pygame.sprite.Group()
                self.player_sprite=pygame.sprite.Group()
                self.arrow_sprites=pygame.sprite.Group()


                #레벨,플레이어,배경sprite
                level.create_level(0,0,self)
                self.world = level.world
                self.player = level.player
                self.background_.ispink=False
                pygame.init()

                self.camera = Camera(self.screen, self.player.rect, level.get_size()[0], level.get_size()[1])

                #아이템
                item1=item(self)
                item2=item(self)
                item3=item(self)
                item4=item(self)
                item5=item(self)
                item6=item(self)
                item7=item(self)
                item8=item(self)
                item9=item(self)
                item10=item(self)
                item11=item(self)

                #sprite 그룹에 sprite 추가
                self.arrow_sprites.add(self.arrow_trap1,self.arrow_trap2,self.arrow_trap3,self.arrow_trap4,self.arrow_trap5,self.arrow_trap6,\
                    self.arrow_trap7,self.arrow_trap8,self.arrow_trap9,self.arrow_trap10,self.arrow_trap11,self.arrow_trap12,self.arrow_trap13,\
                        self.arrow_trap14)

                self.start_time=pygame.time.get_ticks()
                self.gameover=False
                GAME_OVER_FIRE=False

                GAME_OVER_ARROW=False

            #player 좌표 확인
            #print(self.player.rect.x,self.player.rect.y)
            self.event()

            #화면 이동
            asize = ((self.screen_rect.w // self.background_rect.w + 1) * self.background_rect.w, (self.screen_rect.h // self.background_rect.h + 1) * self.background_rect.h)
            bg = pygame.Surface(asize)


            for x in range(0, asize[0], self.background_rect.w):
                for y in range(0, asize[1], self.background_rect.h):
                    self.screen.blit(self.background, (x, y))

            #배경그림
            self.background_.background_blit(self)

            time_spent = self.tps(clock, FPS)
            self.camera.draw_sprites(self.screen, self.all_sprite)

            #순간이동
            teleport_.sprite_def(self,self.player)
            if(teleport_.ready==True):
                teleport_.collide_detect(self)

            #box제어
            box_.collide_detect(self,self.background_)

            #폭탄제어
            GAME_OVER_FIRE=fire_bomb1.bomb_draw(self,self.fire_rect1,3)
            GAME_OVER_FIRE=fire_bomb2.bomb_draw(self,self.fire_rect2,2.5)
            GAME_OVER_FIRE=fire_bomb3.bomb_draw(self,self.fire_Rect3,3.8)

            #버튼 제어
            self.button_detect_1.detect(self.screen,self)
            self.button1.button_draw(self)

            #공격제어
            self.shot_.shooting()

            #창살제어
            if self.BUTTON_ON1 is True:
                self.arrow_sprites.remove(self.arrow_trap3,self.arrow_trap4,self.arrow_trap5,self.arrow_trap6,self.arrow_trap8,self.arrow_trap9,\
                self.arrow_trap10,self.arrow_trap11)
            
            GAME_OVER_ARROW=self.arrow_trap1.arrow_player_detect()

            #점수 환산
            if self.start_time:
                time_since_enter=pygame.time.get_ticks()-self.start_time
                message='Score: '+str(time_since_enter)+'ms'
                self.screen.blit(FONT.render(message, True, TEXT_COLOR), (10, 10))
                self.score=time_since_enter

            #일시정지 버튼
            buttonPressed=gameover_.button("Pause",900,0,150,50,(103,153,255),(107,102,255),"paused")

            #PAUSE 버튼이 눌린 경우
            while buttonPressed==2:
                buttonPressed=gameover_.pausePressed()
                if buttonPressed==1:
                    self.gameover=True
                break

            #얼굴인식
            mouthOpen=face.face_recognition(self.screen)
            #아이템
            item1.draw_item(self,2400,1200,mouthOpen)
            item2.draw_item(self,400,600,mouthOpen)
            item3.draw_item(self,800,900,mouthOpen)
            item4.draw_item(self,800,700,mouthOpen)
            item5.draw_item(self,1050,800,mouthOpen)
            item6.draw_item(self,2390,1300,mouthOpen)
            item7.draw_item(self,1750,1390,mouthOpen)
            item8.draw_item(self,1950,1400,mouthOpen)
            item9.draw_item(self,1900,1419,mouthOpen)
            item10.draw_item(self,2210,1210,mouthOpen)
            item11.draw_item(self,2550,1350,mouthOpen)


            #print(mouthOpen)

            #배경 update
            self.player.update(self,self.up,self.down,self.left, self.right)
            self.camera.update()
            pygame.display.flip()
