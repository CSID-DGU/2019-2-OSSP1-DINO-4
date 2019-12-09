import pygame

class box1(pygame.sprite.Sprite):
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


class box2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #초기화

        self.image=pygame.image.load("tile/platform_tile_023.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))

        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)

        self.rect.x=2080
        self.rect.y=410
    
    def collide_detect(self,game,background):
        hits=pygame.sprite.spritecollide(self,game.player_sprite,False,pygame.sprite.collide_mask)
        if hits:
            game.box2_hit=True

class box3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #초기화

        self.image=pygame.image.load("tile/platform_tile_023.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))

        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)

        self.rect.x=3160
        self.rect.y=420
    
    def collide_detect(self,game,background):
        hits=pygame.sprite.spritecollide(self,game.player_sprite,False,pygame.sprite.collide_mask)
        if hits:
            game.box3_hit=True