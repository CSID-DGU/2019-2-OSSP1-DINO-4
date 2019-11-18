import pygame

from player import *

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

#배경 벽 불러옴
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h,case):
        super().__init__()
        if case=="1": #땅 위에 풀있는거1
            self.image=pygame.image.load("environment/tiles/tile-grass-middle.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="2": #땅 위에 풀있는거 2
            self.image=pygame.image.load("environment/tiles/tile-grass-right.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="3": #땅 왼쪽
            self.image=pygame.image.load("environment/tiles/tile-03.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="4": #땅 채우는거
            self.image=pygame.image.load("environment/tiles/tile-02.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="5": #땅 채우는거 사이에 돌1
            self.image=pygame.image.load("environment/tiles/tile10.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="6": #땅 채우는거 사이에 돌2
            self.image=pygame.image.load("environment/tiles/tile11.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="7": #땅 오른쪽
            self.image=pygame.image.load("environment/tiles/tile-01.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="8": #안에 땅 왼쪽아래
            self.image=pygame.image.load("environment/tiles/tile-in-lb.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="9": #안에 땅 오른쪽아래
            self.image=pygame.image.load("environment/tiles/tile-in-rb.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="A": #안에 땅 가운데아래
            self.image=pygame.image.load("environment/tiles/tile-in-mb.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="B": #안에 땅 왼쪽위
            self.image=pygame.image.load("environment/tiles/tile-in-lt.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="C": #안에 땅 오른쪽위
            self.image=pygame.image.load("environment/tiles/tile-in-rt.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="D": #안에 땅 가운데위
            self.image=pygame.image.load("environment/tiles/tile-in-mt.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="E": #돌맹이
            self.image=pygame.image.load("environment/props/rock.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="F": #왼쪽길게나온거
            self.image=pygame.image.load("environment/tiles/tile23.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="G": #박스
            self.image=pygame.image.load("environment/props/big-crate.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="H": #나무
            self.image=pygame.image.load("environment/props/tree.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case=="I": #상자
            self.image=pygame.image.load("tile/platform_tile_023.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))


        self.rect = self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.topleft=[x,y]

        
class Level(object):
    '''Read a map and create a level'''
    def __init__(self, open_level):
        self.level1 = []
        self.world = []
        self.level = open(open_level, "r")

    def create_level(self, x, y, game):
        for l in self.level:
            self.level1.append(l)

        for row in self.level1:
            for col in row:
                #초록땅
                if col == "1" or col=="2" or col=="3" or col=="4" or col=="5" or col=="6"or col=="7"\
                    or col=="8"or col=="9"or col=="A"or col=="B"or col=="C"or col=="D" or col=="E"\
                    or col=="G" or col=="I":
                    platform = Platform(x, y,40,40,col)
                    self.world.append(platform)
                    game.all_sprite.add(self.world)
                if col=="F":
                    platform = Platform(x, y,80,40,col)
                    self.world.append(platform)
                    game.all_sprite.add(self.world)
                if col=="H":
                    platform = Platform(x, y,160,280,col)
                    self.world.append(platform)
                    game.all_sprite.add(self.world)
                elif col == "P":
                    self.player= player(x,y)
                    game.player_sprite.add(self.player)
                    game.all_sprite.add(self.player)
                    
                x += 40
            y += 40
            x = 0


    def get_size(self):
        lines = self.level1
        line = max(lines, key=len)
        self.width = (len(line))*40
        self.height = (len(lines))*40
        return (self.width, self.height)