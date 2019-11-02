import pygame
import random
from const import *

from const import *

class bomb(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()

        #창의 넓이,높이
        self.game=game
        self.width=WIDTH
        self.height=HEIGHT

        #fire image 불러옴
        self.image=pygame.image.load("tile/flame_frames.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,60))

    #위에서 떨어지는 폭탄
    def bomb_draw(self,screen,fire):

        self.mask=pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()

        #좌표 = (fire[0],fire[1])
        self.rect.x=fire[0]
        self.rect.y=fire[1]

        #y로 1.5만큼 떨어짐
        fire[1]+=1.5

        #self와 배경의 땅과의 충돌 검사
        hits=pygame.sprite.spritecollide(self,self.game.platforms,False)
        #self와 캐릭터의 충돌 검사
        hits_character=pygame.sprite.spritecollide(self,self.game.player_group,False,pygame.sprite.collide_mask)

        if hits_character:
            GAME_OVER=True
            return GAME_OVER

        #충돌했다면
        if hits:
            fire[0]=random.randrange(0,900)
            fire[1]=40
            screen.blit(self.image,(fire[0],fire[1]))

        else:
            if fire[1]>600:
                fire[0]=random.randrange(0,900)
                fire[1]=random.randrange(0,600)
                screen.blit(self.image,(fire[0],fire[1]))

            else:
                screen.blit(self.image,(fire[0],fire[1]))



        #screen.blit(self.saw_tooth,(700,260))

class water(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        super().__init__()

        self.game=game
        #water image 가져옴
        self.water=pygame.image.load("tile/platform_tile_005.png").convert_alpha()
        self.water=pygame.transform.scale(self.water,(100,20))

        #충돌 검사 위해 초기화
        self.rect = self.water.get_rect()
        self.mask=pygame.mask.from_surface(self.water)

        self.rect.x=x
        self.rect.y=y

    def water_player_detect(self):
        hits=pygame.sprite.spritecollide(self.game.player1,self.game.water_sprites,False,pygame.sprite.collide_mask)

        if hits:
            pygame.quit()

class arrow(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        super().__init__()
        self.game=game

        #arrow image 불러옴
        self.arrow=pygame.image.load("tile/platform_tile_064.png").convert_alpha()
        self.arrow=pygame.transform.scale(self.arrow,(60,20))

        #충돌 검사 위해 초기화
        self.rect = self.arrow.get_rect()
        self.mask=pygame.mask.from_surface(self.arrow)

        self.rect.x=x
        self.rect.y=y

    def arrow_player_detect(self):
        global GAME_OVER
        hits=pygame.sprite.spritecollide(self.game.player1,self.game.arrow_sprites,False,pygame.sprite.collide_mask)

        if hits:
            GAME_OVER=True
            return GAME_OVER

class teleport(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        #초기화
        self.game=game
        self.ready=False
        self.player_state=0
    
    #텔레포트 확인
    #한 class당 본인 sprite 하나라서 사용자 좌표 받아서 sprite 정함
    def sprite_def(self,game,player):
        #왼쪽 분홍색
        if player.rect.x>=200 and player.rect.x<=400 and player.rect.y==60:
            self.image=pygame.image.load("tile/pink_neon.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(110,60))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=300
            self.rect.y=10

            self.ready=True
            self.player_state=1
        #오른쪽 분홍색
        if player.rect.x>=18 and player.rect.x<=70 and player.rect.y==440:
            self.image=pygame.image.load("tile/pink_neon_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(60,100))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=0
            self.rect.y=400

            self.ready=True
            self.player_state=2
        #왼쪽 초록색
        if player.rect.x>=500 and player.rect.x<=650 and player.rect.y>100 and player.rect.y<250:
            self.image=pygame.image.load("tile/green_neon.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(110,60))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=565
            self.rect.y=280

            self.ready=True
            self.player_state=3

        #오른쪽 초록색
        if player.rect.x>=700 and player.rect.y>=150:
            self.image=pygame.image.load("tile/green_neon.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(110,60))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=780
            self.rect.y=230

            self.ready=True
            self.player_state=4

        #위쪽 빨간색
        if player.rect.x>=600 and player.rect.y<150:
            self.image=pygame.image.load("tile/red_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(60,100))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=850
            self.rect.y=15

            self.ready=True
            self.player_state=5
        #아래쪽 빨간색
        if player.rect.x>=700 and player.rect.y==430:
            self.image=pygame.image.load("tile/red_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(60,100))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=850
            self.rect.y=390

            self.ready=True
            self.player_state=6


        #오른쪽 파란색
        if player.rect.x>=400 and player.rect.y==520:
            self.image=pygame.image.load("tile/blue_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(60,100))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=700
            self.rect.y=495

            self.ready=True
            self.player_state=7

        #왼쪽 파란색
        if player.rect.x<400 and player.rect.y==520:
            self.image=pygame.image.load("tile/blue_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(60,100))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=50
            self.rect.y=500

            self.ready=True
            self.player_state=8
        

    def collide_detect(self,game):
        hits=pygame.sprite.spritecollide(self,self.game.player_group,False,pygame.sprite.collide_mask)

        if hits:
            #오른쪽 분홍색으로 들어가면 왼쪽 분홍색으로 나옴
            if self.player_state is 1:
                game.player1.rect.x=10
                game.player1.rect.y=415
            #왼쪽 분홍색으로 들어가면 오른쪽 분홍색으로 나옴
            elif self.player_state is 2 and game.player1.left is True:
                game.player1.rect.x=320
                game.player1.rect.y=30
            #왼쪽 초록색으로 들어가면 오른쪽 초록색으로 나옴
            elif self.player_state is 3:
                game.player1.rect.x=800
                game.player1.rect.y=200
                game.player1.go_up()
            #오른쪽 초록색으로 들어가면 왼쪽 초록색으로 나옴
            elif self.player_state is 4:
                game.player1.rect.x=575
                game.player1.rect.y=270
                game.player1.go_up()
            #위쪽 빨간색으로 들어가면 아래쪽 빨간색으로 나옴
            elif self.player_state is 5 and game.player1.left is False:
                game.player1.rect.x=850
                game.player1.rect.y=400
                game.player1.left=True
            #아래쪽 빨간색으로 들어가면 위쪽 빨간색으로 나옴
            elif self.player_state is 6 and game.player1.left is False:
                game.player1.rect.x=845
                game.player1.rect.y=30
                game.player1.left=True
            #오른쪽 파란색으로 들어가면 왼쪽 파란색으로 나옴
            elif self.player_state is 7 and game.player1.left is False:
                game.player1.rect.x=60
                game.player1.rect.y=520
            #왼쪽 파란색으로 들어가면 오른쪽 파란색으로 나옴
            elif self.player_state is 8 and game.player1.left is True:
                game.player1.rect.x=700
                game.player1.rect.y=520


