import pygame

from player import *

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
            self.image=pygame.image.load("tile/red_up.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(w,h))
        elif case==4:
            self.image=pygame.image.load("tile/black.png").convert_alpha()
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
                if col == "X":
                    platform = Platform(x, y,40,40,1)
                    self.world.append(platform)
                    game.all_sprite.add(self.world)
                elif col=="F":
                    platform=Platform(x, y,40,40,2)
                    self.world.append(platform)
                    game.all_sprite.add(self.world)
                elif col=="A":
                    platform=Platform(x, y,40,80,3)
                    self.world.append(platform)
                    game.all_sprite.add(self.world)
                elif col=="D":
                    platform=Platform(x, y,40,40,4)
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