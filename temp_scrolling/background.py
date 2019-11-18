import pygame

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

class background:
    def __init__(self):
        #neon warp door
        self.blue_up=pygame.image.load("tile/blue_up.png").convert_alpha()
        self.blue_up=pygame.transform.scale(self.blue_up,(40,80))
        self.blue_down=pygame.image.load("tile/blue_neon_down.png").convert_alpha()
        self.blue_down=pygame.transform.scale(self.blue_down,(80,40))
        self.red_up=pygame.image.load("tile/red_up.png").convert_alpha()
        self.red_up=pygame.transform.scale(self.red_up,(40,80))
        self.pink_up=pygame.image.load("tile/pink_neon_up.png").convert_alpha()
        self.pink_up=pygame.transform.scale(self.pink_up,(40,80))
        self.pink_down=pygame.image.load("tile/pink_neon.png").convert_alpha()
        self.pink_down=pygame.transform.scale(self.pink_down,(80,40))
        self.green_down=pygame.image.load("tile/green_neon.png").convert_alpha()
        self.green_down=pygame.transform.scale(self.green_down,(80,40))

        #상자 치면 분홍색 네온 활성화
        self.ispink=False

        #background
        self.background_green=pygame.image.load("environment/layers/middle.png").convert_alpha()
        self.background_green=pygame.transform.scale(self.background_green,(300,800))

        self.background_dark=pygame.image.load("environment/tiles/tile-dark0.png").convert_alpha()

    def background_blit(self,game):
        #background
        #풀
        game.screen.blit(self.background_green,RelRect(520,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(820,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(1120,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(1420,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(1720,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(2020,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(2320,520,300,800,game.camera))
        game.screen.blit(self.background_green,RelRect(2620,520,300,800,game.camera))

        #지하 색깔
        self.background_dark=pygame.transform.scale(self.background_dark,(680,80))
        game.screen.blit(self.background_dark,RelRect(920,680,680,80,game.camera))

        self.background_dark=pygame.transform.scale(self.background_dark,(1080,320))
        game.screen.blit(self.background_dark,RelRect(1600,1120,680,80,game.camera))

        #neon warp door
        if self.ispink:
            game.screen.blit(self.pink_up,RelRect(1880,850,80,40,game.camera))
        game.screen.blit(self.pink_down,RelRect(1680,1415,80,40,game.camera))
        game.screen.blit(self.red_up,RelRect(2630,1160,40,80,game.camera))
        game.screen.blit(self.red_up,RelRect(1480,560,40,80,game.camera))
        

