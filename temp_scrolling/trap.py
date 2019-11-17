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
            fire[0]=random.randrange(1900,2400)
            fire[1]=1200
            game.screen.blit(self.image,RelRect(fire[0],fire[1],20,20,game.camera))
        
        #충돌하지 않음
        else:
            if fire[1]>1440:
                fire[0]=random.randrange(1900,2400)
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

