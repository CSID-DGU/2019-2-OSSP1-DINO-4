import pygame
import background
from background import *
from player import *
from const import *

FRAME=0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game:
    def __init__(self):
        self.width=800
        self.height=600
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()

    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
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
        self.all_sprites=pygame.sprite.Group()
        self.platforms=pygame.sprite.Group()

        pygame.init()
        self.player1=Player((500,300),self)
        self.all_sprites.add(self.player1)

        for plat in PlatformList:
            p=Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        background_=background(self.width,self.height)

        while True:
            time=self.clock.tick(60)
            FRAME+=1
            self.screen.fill((255,193,158))
            background_.background(self.screen)

            self.event()
            self.all_sprites.update()
            if self.player1.rect.right>WIDTH:
                player1.rect.right=WIDTH
            
            if self.player1.rect.left<0:
                player1.rect.left=0

            self.all_sprites.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

