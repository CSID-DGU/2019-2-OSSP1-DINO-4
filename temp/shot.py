import pygame

from player import *

class shot(pygame.sprite.Sprite):
    def __init__(self,screen,game):
        #setting
        super().__init__()
        self.screen=screen
        self.game=game

        #image load
        self.shot_image=pygame.image.load("bullet.png").convert_alpha()
        self.shot_image=pygame.transform.scale(self.shot_image,(30,30))

        #ready : 준비
        #fire : 불 쏨
        self.bullet_state="ready"

        #날아가는 속도 : 5
        self.speed=5

        #충돌검사 위해
        self.rect=self.shot_image.get_rect()
        self.mask=pygame.mask.from_surface(self.shot_image)
    
    #총 좌표 초기화
    def shooting_setting(self,x,y):
        self.bullet_state="fire"
        self.rect.x=x
        self.rect.y=y

    #총알 날라감
    def shooting(self):

        hits=pygame.sprite.spritecollide(self,self.game.platforms,False)

        #총알 벽에 부딪히면 없어짐
        if hits:
            self.bullet_state="ready"
        else:
            #총알 창 밖으로 나가면 초기화
            if self.rect.x>=900:
                self.bullet_state="ready"
            #총알 날림
            if self.bullet_state is "fire":
                self.screen.blit(self.shot_image,(self.rect.x,self.rect.y))
                self.rect.x+=self.speed
        