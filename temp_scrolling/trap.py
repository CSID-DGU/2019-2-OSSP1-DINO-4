import pygame
import random

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

class bomb(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()

        #창의 넓이,높이
        self.game=game

        #fire image 불러옴
        self.image=pygame.image.load("tile/fire.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,20))

        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    #위에서 떨어지는 폭탄
    def bomb_draw(self,game,fire,speed):
        global GAME_OVER
        #좌표 = (fire[0],fire[1])
        self.rect.x=fire[0]
        self.rect.y=fire[1]

        #떨어지는 속도
        fire[1]+=speed

        #self와 배경의 땅과의 충돌 검사
        hits=pygame.sprite.spritecollide(self,game.world,False,pygame.sprite.collide_mask)
        #self와 캐릭터의 충돌 검사
        hits_character=pygame.sprite.spritecollide(self,self.game.player_sprite,False,pygame.sprite.collide_mask)

        if hits_character and not game.down:
            GAME_OVER=True
            return GAME_OVER

        #충돌했다면
        if hits:
            fire[0]=random.randrange(1800,2400)
            fire[1]=1200
            game.screen.blit(self.image,RelRect(fire[0],fire[1],20,20,game.camera))

        #충돌하지 않음
        else:
            if fire[1]>1440:
                fire[0]=random.randrange(1800,2400)
                fire[1]=1200
                game.screen.blit(self.image,RelRect(fire[0],fire[1],20,20,game.camera))

            else:
                game.screen.blit(self.image,RelRect(fire[0],fire[1],20,20,game.camera))

class arrow(pygame.sprite.Sprite):
    def __init__(self,game,x,y,flip):
        #flip 1이면 뒤집기, flip0이면 뒤집지 않음
        super().__init__()
        self.game=game

        if flip is 0:
            #arrow image 불러옴
            self.image=pygame.image.load("tile/platform_tile_064.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40,20))
        elif flip is 1:
            #arrow image 불러옴
            self.image=pygame.image.load("tile/platform_tile_064.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(40,20))
            self.image=pygame.transform.flip(self.image,False,True)
        #충돌 검사 위해 초기화
        self.rect = self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)

        self.rect.x=x
        self.rect.y=y


    def arrow_player_detect(self):
        global GAME_OVER
        hits=pygame.sprite.spritecollide(self.game.player,self.game.arrow_sprites,False,pygame.sprite.collide_mask)

        if hits:
            GAME_OVER=True
            return GAME_OVER

class following_fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #불의 초기위치 정하기 위함
        self.first=True

        #불 자연스럽게 움직이게 하기 위해서
        self.count=0

        #fire image 불러옴
        self.image=pygame.image.load("tile/fire.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,20))

        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def follow(self,game,x,y):
        global GAME_OVER

        if self.first is True or abs(game.player.rect.x-self.rect.x)>200:
            self.rect.x=game.player.rect.x+random.randrange(-80,-40)
            self.rect.y=game.player.rect.y+random.randrange(-10,10)
            self.first=False
        elif self.first is False and self.count is not 60:
            self.rect.x+=7.5
            self.rect.y+=random.randrange(-3,3)
        else:
            self.rect.x=game.player.rect.x+random.randrange(-80,-40)
            self.rect.y=game.player.rect.y+random.randrange(-10,10)
            self.count=0

        #self와 배경의 땅과의 충돌 검사
        hits=pygame.sprite.spritecollide(self,game.world,False,pygame.sprite.collide_mask)
        #self와 캐릭터의 충돌 검사
        hits_character=pygame.sprite.spritecollide(self,game.player_sprite,False,pygame.sprite.collide_mask)

        if hits:
            self.rect.x=game.player.rect.x+random.randrange(-80,-45)
            self.rect.y=game.player.rect.y+random.randrange(-20,20)
        else:
            game.screen.blit(self.image,RelRect(self.rect.x,self.rect.y,20,20,game.camera))

        if hits_character:
            GAME_OVER=True
            return GAME_OVER

class moving_arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #움직이는 창살
        self.arrow_up=pygame.image.load("tile/platform_tile_064_long.png").convert_alpha()
        self.arrow_up=pygame.transform.scale(self.arrow_up,(840,80))
        self.arrow_up_turn=pygame.transform.flip(self.arrow_up,True,True)

        #충돌 검사 위해 초기화
        self.rect = self.arrow_up_turn.get_rect()
        self.mask=pygame.mask.from_surface(self.arrow_up_turn)

        self.rect.x=160
        self.rect.y=40

    def moving_arrow_player_detect(self,game):
        global GAME_OVER
        self.arrow_up_turn=pygame.transform.scale(self.arrow_up_turn,(840,40+game.background_.cnt))
        self.mask=pygame.mask.from_surface(self.arrow_up_turn)

        hits=pygame.sprite.spritecollide(self,game.player_sprite,False,pygame.sprite.collide_mask)

        if hits and not game.down:
            GAME_OVER=True
            return GAME_OVER
