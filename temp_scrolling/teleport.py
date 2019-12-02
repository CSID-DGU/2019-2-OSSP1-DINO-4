import pygame

from camera import *

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

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
        #아래 빨간색
        if player.rect.x>=2500 and player.rect.x<=3000 and player.rect.y>=1100 and player.rect.y<=1500:
            self.image=pygame.image.load("tile/red_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40,80))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=2630
            self.rect.y=1160

            self.ready=True
            self.player_state=1

        #위 빨간색
        if player.rect.x>=1900 and player.rect.x<=2200 and player.rect.y>=800 and player.rect.y<=900:
            self.image=pygame.image.load("tile/red_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40,80))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=2000
            self.rect.y=840

            self.ready=True
            self.player_state=2

        #위 분홍색
        if player.rect.x>=1600 and player.rect.x<=1900 and player.rect.y>=800 and player.rect.y<=1050:
            self.image=pygame.image.load("tile/pink_neon_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40,80))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=1880
            self.rect.y=850

            self.ready=True
            self.player_state=3

        #아래 분홍색
        if player.rect.x>=1600 and player.rect.x<=1900 and player.rect.y>=1200 and player.rect.y<=1400:
            self.image=pygame.image.load("tile/pink_neon.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(80,40))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=1680
            self.rect.y=1415

            self.ready=True
            self.player_state=4

        #지하 파란색
        if player.rect.x>=1600 and player.rect.x<=1900 and player.rect.y>=1100 and player.rect.y<=1200:
            self.image=pygame.image.load("tile/blue_neon_down.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(80,40))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=1680
            self.rect.y=1130

            self.ready=True
            self.player_state=5

        #위에 파란색
        if player.rect.x>=1700 and player.rect.x<=1845 and player.rect.y<=240:
            self.image=pygame.image.load("tile/blue_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40,80))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=1800
            self.rect.y=110

            self.ready=True
            self.player_state=6

        #초록색
        if player.rect.x>=2670 and player.rect.x<=3500 and player.rect.y>=500 and player.rect.y<=650:
            self.image=pygame.image.load("tile/green_neon.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(80,40))

            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)

            self.rect.x=3400
            self.rect.y=530

            self.ready=True
            self.player_state=7


    def collide_detect(self,game):
        hits=pygame.sprite.spritecollide(self,game.player_sprite,False,pygame.sprite.collide_mask)

        if hits:
            #아래 빨간색으로 들어가면 위 빨간색으로 나옴
            if self.player_state is 1 and game.player.direction is "right":
                game.player.rect.x=2010
                game.player.rect.y=840
                game.player.direction="left"
            #위쪽 빨간색으로 들어가면 아래 빨간색으로 나옴
            if self.player_state is 2 and game.player.direction is "left":
                game.player.rect.x=2630
                game.player.rect.y=1190
                game.player.direction="right"
            #위 분홍색으로 들어가면 아래 분홍색으로 나옴
            if game.background_.ispink is True and self.player_state is 3 and game.player.direction is "right":
                game.player.rect.x=1680
                game.player.rect.y=1400
                game.player.movy-=30
            #아래 분홍으로 들어가면 위쪽 분홍색으로 나옴
            if self.player_state is 4:
                game.player.rect.x=1860
                game.player.rect.y=850
                game.player.direction="left"
            #지하 파란색으로 들어가면 위쪽 파란색으로 나옴
            if self.player_state is 5:
                game.player.rect.x=1795
                game.player.rect.y=110
                game.player.direction="left"
            #위쪽 파란색으로 들어가면 지하 파란색으로 나옴
            if self.player_state is 6 and game.player.direction is "right":
                game.player.rect.x=1680
                game.player.rect.y=1135
                game.player.movy+=30
            if self.player_state is 7:
                game.player.movy-=27


class box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #초기화

        self.image=pygame.image.load("tile/platform_tile_023.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))

        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)

        self.rect.x=1880
        self.rect.y=960

    def collide_detect(self,game,background):
        hits=pygame.sprite.spritecollide(self,game.player_sprite,False,pygame.sprite.collide_mask)
        if hits:
            background.ispink=True
