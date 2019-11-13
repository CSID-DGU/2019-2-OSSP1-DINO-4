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
from os import path
import time

global FPS
global clock
global time_spent

class Game:
    def __init__(self):

        self.WIDTH=1000
        self.HEIGHT=700

        self.up=False
        self.left=False
        self.right=False
        self.down=False

        self.screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.screen_rect=self.screen.get_rect()

        self.background=pygame.image.load("environment/layers/back.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(1000,700))
        self.background_rect = self.background.get_rect()

        self.load_data() #high score data load
        self.score=0
        self.start_time=0

        #불 폭탄 떨어지는 초기위치 설정
        self.fire_rect1=[1800,1200]
        self.fire_rect2=[1900,1200]

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
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.up=False
                if event.key==pygame.K_DOWN:
                    self.down=False
                if event.key==pygame.K_LEFT:
                    self.left=False
                if event.key==pygame.K_RIGHT:
                    self.right=False


    def main(self):
        global GAME_OVER_FIRE
        #spite_group 정의
        self.all_sprite=pygame.sprite.Group()
        self.player_sprite=pygame.sprite.Group()

        #초기화
        FPS=30
        clock = pygame.time.Clock()
        background_=background() #sprite 아닌 background
        teleport_=teleport(self) #teleport
        box_=box() #box
        fire_bomb1=bomb(self) #폭탄1
        fire_bomb2=bomb(self) #폭탄2

        #레벨,플레이어,배경sprite
        level = Level("level1")
        level.create_level(0,0,self)
        self.world = level.world
        self.player = level.player


        #함수정의
        pygame.init()

        self.camera = Camera(self.screen, self.player.rect, level.get_size()[0], level.get_size()[1])
        FONT = pygame.font.SysFont("Sans", 20)
        gameover_=gameover(self.screen,clock,self.highscore,FONT)

        #시간 표시 글자색
        TEXT_COLOR=(0,0,0)
        BG_COLOR=(255,255,255)


        while True:
            #Gameover
            if self.gameover or GAME_OVER_FIRE:
                gameover_.show_gameover_screen(self.score,self.dir)
                #재초기화
                self.up=False
                self.down=False
                self.right=False
                self.left=False

                self.all_sprite=pygame.sprite.Group()
                self.player_sprite=pygame.sprite.Group()

                #레벨,플레이어,배경sprite
                level.create_level(0,0,self)
                self.world = level.world
                self.player = level.player
                background_.ispink=False
                pygame.init()

                self.camera = Camera(self.screen, self.player.rect, level.get_size()[0], level.get_size()[1])

                self.start_time=pygame.time.get_ticks()
                self.gameover=False
                GAME_OVER_FIRE=False

            #print(self.player.rect.x,self.player.rect.y)
            self.event()

            #화면 이동
            asize = ((self.screen_rect.w // self.background_rect.w + 1) * self.background_rect.w, (self.screen_rect.h // self.background_rect.h + 1) * self.background_rect.h)
            bg = pygame.Surface(asize)


            for x in range(0, asize[0], self.background_rect.w):
                for y in range(0, asize[1], self.background_rect.h):
                    self.screen.blit(self.background, (x, y))

            #배경그림
            background_.background_blit(self)

            time_spent = self.tps(clock, FPS)
            self.camera.draw_sprites(self.screen, self.all_sprite)

            #순간이동
            teleport_.sprite_def(self,self.player)
            if(teleport_.ready==True):
                teleport_.collide_detect(self)

            #box
            box_.collide_detect(self,background_)

            #폭탄
            GAME_OVER_FIRE=fire_bomb1.bomb_draw(self,self.fire_rect1)
            GAME_OVER_FIRE=fire_bomb2.bomb_draw(self,self.fire_rect2)

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
                    print("gameover buttonPressed들어옴")
                    self.gameover=True
                break


            #배경 update
            self.player.update(self,self.up,self.down,self.left, self.right)
            self.camera.update()
            pygame.display.flip()
