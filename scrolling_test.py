import pygame
import sys
from pygame.locals import *

SCREEN_SIZE = (1280, 720)

global FPS
global clock
global time_spent

def RelRect(actor, camera):
    return pygame.Rect(actor.rect.x-camera.rect.x, actor.rect.y-camera.rect.y, actor.rect.w, actor.rect.h)

def tps(orologio,fps):
    temp = orologio.tick(fps)
    tps = temp / 1000.
    return tps

class Camera(object):
    '''Class for center screen on the player'''
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.center
        self.world_rect = pygame.Rect(0, 0, level_width, level_height)

    def update(self):
      if self.player.centerx > self.rect.centerx + 40:
          self.rect.centerx = self.player.centerx - 40
      if self.player.centerx < self.rect.centerx - 40:
          self.rect.centerx = self.player.centerx + 40
      if self.player.centery > self.rect.centery + 40:
          self.rect.centery = self.player.centery - 40
      if self.player.centery < self.rect.centery - 40:
          self.rect.centery = self.player.centery + 40
      self.rect.clamp_ip(self.world_rect)

    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, RelRect(s, self))

#배경 벽 불러옴
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h,case):
        super().__init__()
        if case==1:
            self.image=pygame.image.load("tile/platform_tile_021.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==2:
            self.image=pygame.image.load("tile/platform_tile_035.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==3:
            self.image=pygame.image.load("tile/platform_tile_009.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==4:
            self.image=pygame.image.load("tile/platform_tile_016.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==5:
            self.image=pygame.image.load("tile/platform_tile_021.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==6:
            self.image=pygame.image.load("tile/platform_tile_032.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==7:
            self.image=pygame.image.load("tile/platform_tile_038.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))

        self.rect = self.image.get_rect()
        self.rect.topleft=[x,y]

class Crashman(pygame.sprite.Sprite):
    def __init__(self,x,y):
        #setting
        super().__init__()

        self.x=x
        self.y=y
        self.movx=0
        self.movy=0
        self.vel=5  #가속도

        self.contact = False
        self.jump = False
        self.direction="right"
        self.frame=0

        self.image=pygame.image.load("girl_image/Walk0.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))

        #이미지 저장을 위한 변수 및 함수
        self.walk_image=["girl_image/Walk0.png","girl_image/Walk1.png","girl_image/Walk2.png","girl_image/Walk3.png",
                        "girl_image/Walk4.png","girl_image/Walk5.png","girl_image/Walk6.png","girl_image/Walk7.png",
                        "girl_image/Walk8.png","girl_image/Walk9.png","girl_image/Walk10.png","girl_image/Walk11.png"
                        ,"girl_image/Walk12.png","girl_image/Walk13.png","girl_image/Walk14.png","girl_image/Walk15.png",
                        "girl_image/Walk16.png","girl_image/Walk17.png","girl_image/Walk18.png","girl_image/Walk19.png"]

        #self.mask
        self.mask=pygame.mask.from_surface(self.image)

        #self.rect
        self.rect=self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

        
    def update(self, up, left, right):
        if up:
            if self.contact:
                if self.direction == "right":
                    self.image = pygame.image.load("girl_image/jump.png").convert_alpha()
                    self.image=pygame.transform.scale(self.image,(50,50))
                self.jump = True
                self.movy -= 20

        if left:
            self.direction = "left"
            self.movx = -self.vel
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.walk_image[self.frame]).convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))
                self.image=pygame.transform.flip(self.image,True,False)
                if self.frame==19: self.frame=0
            else:
                self.image = pygame.image.load("girl_image/jump.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))
                self.image=pygame.transform.flip(self.image,True,False)

        if right:
            self.direction = "right"
            self.movx = +self.vel
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.walk_image[self.frame]).convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))
                if self.frame==19: self.frame=0
            else:
                self.image = pygame.image.load("girl_image/jump.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))


        if not (left or right):
            self.movx = 0
        self.rect.x += self.movx

        self.collide(self.movx, 0, world)

        if not self.contact:
            self.movy += 0.3
            if self.movy > 10:
                self.movy = 10
            self.rect.y += self.movy

        if self.jump:
            self.movy += 2
            self.rect.y += self.movy
            if self.contact == True:
                self.jump = False

        self.contact = False
        self.collide(0, self.movy, world)

    def collide(self, movx, movy, world):
        self.contact = False
        for o in world:
            if self.rect.colliderect(o):
                if movx > 0:
                    self.rect.right = o.rect.left
                if movx < 0:
                    self.rect.left = o.rect.right
                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contact = True
                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0


class Level(object):
    '''Read a map and create a level'''
    def __init__(self, open_level):
        self.level1 = []
        self.world = []
        self.all_sprite = pygame.sprite.Group()
        self.level = open(open_level, "r")

    def create_level(self, x, y):
        for l in self.level:
            self.level1.append(l)

        for row in self.level1:
            for col in row:
                if col == "X":
                    platform = Platform(x, y,30,30,1)
                    self.world.append(platform)
                    self.all_sprite.add(self.world)
                if col == "P":
                    self.crashman = Crashman(x,y)
                    self.all_sprite.add(self.crashman)
                x += 25
            y += 25
            x = 0

    def get_size(self):
        lines = self.level1
        #line = lines[0]
        line = max(lines, key=len)
        self.width = (len(line))*25
        self.height = (len(lines))*25
        return (self.width, self.height)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()
background = pygame.image.load("tile/platform_tile_001.png").convert_alpha()
background_rect = background.get_rect()
level = Level("level1")
level.create_level(0,0)
world = level.world
crashman = level.crashman

camera = Camera(screen, crashman.rect, level.get_size()[0], level.get_size()[1])
all_sprite = level.all_sprite

FPS = 30
clock = pygame.time.Clock()

up = left = right = False
x, y = 0, 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                up=True
            if event.key==pygame.K_LEFT:
                left=True
            if event.key==pygame.K_RIGHT:
                right=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                up=False
            if event.key==pygame.K_LEFT:
                left=False
            if event.key==pygame.K_RIGHT:
                right=False

    asize = ((screen_rect.w // background_rect.w + 1) * background_rect.w, (screen_rect.h // background_rect.h + 1) * background_rect.h)
    bg = pygame.Surface(asize)

    for x in range(0, asize[0], background_rect.w):
        for y in range(0, asize[1], background_rect.h):
            screen.blit(background, (x, y))

    time_spent = tps(clock, FPS)
    camera.draw_sprites(screen, all_sprite)

    crashman.update(up, left, right)
    camera.update()
    pygame.display.flip()