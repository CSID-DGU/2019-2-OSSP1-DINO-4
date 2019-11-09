import pygame
import sys
from pygame.locals import *

from camera import *
from background_platform import *
from player import *

global FPS
global clock
global time_spent

class Game:
    def __init__(self):
        self.WIDTH=1280
        self.HEIGHT=720

        self.up=False
        self.left=False
        self.right=False

        self.screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.screen_rect=self.screen.get_rect()

        self.background=pygame.image.load("tile/background_image.png").convert_alpha()
        self.background_rect = self.background.get_rect()

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
                if event.key==pygame.K_LEFT:
                    self.left=True
                if event.key==pygame.K_RIGHT:
                    self.right=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.up=False
                if event.key==pygame.K_LEFT:
                    self.left=False
                if event.key==pygame.K_RIGHT:
                    self.right=False

    def main(self):
        self.all_sprite=pygame.sprite.Group()

        pygame.init()
        
        level = Level("level1")
        level.create_level(0,0,self)
        self.world = level.world
        self.player = level.player

        camera = Camera(self.screen, self.player.rect, level.get_size()[0], level.get_size()[1])

        FPS = 30
        clock = pygame.time.Clock()

        while True:
            
            self.event()
            asize = ((self.screen_rect.w // self.background_rect.w + 1) * self.background_rect.w, (self.screen_rect.h // self.background_rect.h + 1) * self.background_rect.h)
            bg = pygame.Surface(asize)

            for x in range(0, asize[0], self.background_rect.w):
                for y in range(0, asize[1], self.background_rect.h):
                    self.screen.blit(self.background, (x, y))

            time_spent = self.tps(clock, FPS)
            camera.draw_sprites(self.screen, self.all_sprite)

            self.player.update(self,self.up, self.left, self.right)
            camera.update()
            pygame.display.flip()