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
        self.BUTTON_ON=False
        self.DINO_alive=True

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
        self.remove_platform_=pygame.sprite.Group()
        self.player_group=pygame.sprite.Group()
        self.button=pygame.sprite.Group()
        self.dino_group=pygame.sprite.Group()

        pygame.init()

        #sprite 그룹에 추가할 sprite 선언
        self.player1=Player((self.width/2,self.height/2),self)
        self.button_=button_image(self)
        self.dino_1=Dino(self,100,125)

        #sprite 그룹에 sprite 추가
        self.all_sprites.add(self.player1)
        self.player_group.add(self.player1)
        self.platforms.add(self.button_)
        self.dino_group.add(self.dino_1)

        #배경 벽 불러옴
        for plat in PlatformList:
            p=Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)


        #초기화
        trap1=trap(self)

        for plat in remove_platform:
            p=platform_remove(*plat)
            self.remove_platform_.add(p)

        #선언 및 초기화
        fire_trap=trap(self)
        detect_button=button_detect()

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

                #배경 blit
                background_.background(self.screen)#배경
            #    trap1.trap_draw(self.screen,self.fire_rect)
                self.shot_.shooting()

                fire_trap.bomb_draw(self.screen,self.fire_rect) #위에서 떨어지는 폭탄
                self.button_.button_draw(self.screen)   #버튼

            if self.DINO_alive==True:
                self.dino_1.update(self.screen)
            self.shot_.shooting()
            self.shot_.shoot_dino(self)
            self.event()
            self.all_sprites.update()
                #버튼 눌렸는지 확인
                detect_button.detect(self.screen,self)

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

