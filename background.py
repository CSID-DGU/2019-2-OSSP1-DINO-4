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
        #풀
        self.background_green=pygame.image.load("environment/layers/middle.png").convert_alpha()
        self.background_green=pygame.transform.scale(self.background_green,(300,800))

        self.background_dark=pygame.image.load("environment/tiles/tile-dark0.png").convert_alpha()

        #창살
        self.arrow=pygame.image.load("tile/platform_tile_064.png").convert_alpha()
        self.arrow=pygame.transform.scale(self.arrow,(40,20))

        self.arrow_turn=pygame.image.load("tile/platform_tile_064.png").convert_alpha()
        self.arrow_turn=pygame.transform.scale(self.arrow_turn,(40,20))
        self.arrow_turn=pygame.transform.flip(self.arrow_turn,True,True)

        #박스
        self.box=pygame.image.load("tile/box_make.png").convert_alpha()
        self.box=pygame.transform.scale(self.box,(320,200))

        #바닥 불
        self.water=pygame.image.load("tile/fire-flames.png").convert_alpha()
        self.water=pygame.transform.scale(self.water,(40,40))

        #움직이는 창살
        self.arrow_up=pygame.image.load("tile/platform_tile_064_long.png").convert_alpha()
        self.arrow_up=pygame.transform.scale(self.arrow_up,(840,80))
        self.arrow_up_turn=pygame.transform.flip(self.arrow_up,True,True)

        #문
        self.door=pygame.image.load("tile/New Piskel (1) (1).png").convert_alpha()
        self.door=pygame.transform.scale(self.door,(80,80))

        #창살 움직이는거 제어
        self.cnt=0
        self.growing=True

        #문 열리는거 제어
        self.timer=0

    def background_blit(self,game):
        #background
        #1
        game.screen.blit(self.background_green,RelRect(520,520,300,1000,game.camera))
        game.screen.blit(self.background_green,RelRect(820,520,300,1000,game.camera))
        game.screen.blit(self.background_green,RelRect(1120,520,300,1000,game.camera))
        game.screen.blit(self.background_green,RelRect(1420,520,300,1000,game.camera))
        game.screen.blit(self.background_green,RelRect(1720,520,300,1000,game.camera))
        game.screen.blit(self.background_green,RelRect(2020,520,300,1500,game.camera))
        game.screen.blit(self.background_green,RelRect(2320,520,300,1500,game.camera))
        game.screen.blit(self.background_green,RelRect(2620,520,300,1500,game.camera))
        game.screen.blit(self.background_green,RelRect(2920,520,300,1500,game.camera))
        game.screen.blit(self.background_green,RelRect(3220,520,300,1500,game.camera))
        game.screen.blit(self.background_green,RelRect(3520,520,300,1500,game.camera))

        #지하 색깔
        self.background_dark=pygame.transform.scale(self.background_dark,(680,80))
        game.screen.blit(self.background_dark,RelRect(920,680,680,80,game.camera))

        self.background_dark=pygame.transform.scale(self.background_dark,(1080,320))
        game.screen.blit(self.background_dark,RelRect(1600,1120,680,80,game.camera))

        self.background_dark=pygame.transform.scale(self.background_dark,(1480,360))
        game.screen.blit(self.background_dark,RelRect(2000,560,1480,360,game.camera))

        #창살
        game.screen.blit(self.arrow,RelRect(360,620,40,20,game.camera))

        if game.BUTTON_ON1 is False:
            for i in range (0,13):
                game.screen.blit(self.arrow,RelRect(1840+(40*i),1420,40,20,game.camera))
        else:
            for i in range (0,3):
                game.screen.blit(self.arrow,RelRect(1840+(200*i),1420,40,20,game.camera))


        for i in range(0,28):
            game.screen.blit(self.water,RelRect(2240+(i*40),880,1120,20,game.camera))

        #문
        game.screen.blit(self.door,RelRect(3400,40,80,80,game.camera))


        game.screen.blit(self.arrow_turn,RelRect(2320,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+40,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+160,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+440,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+480,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+800,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+840,840,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+880,840,40,20,game.camera))

        game.screen.blit(self.arrow_turn,RelRect(2320+280,760,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+320,760,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+(14*40),760,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+(15*40),760,40,20,game.camera))

        game.screen.blit(self.arrow_turn,RelRect(2320+(40*1),720,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+(40*2),720,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+(40*16),720,40,20,game.camera))
        game.screen.blit(self.arrow_turn,RelRect(2320+(40*17),720,40,20,game.camera))


        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))
        game.screen.blit(self.arrow,RelRect(1840,1420,40,20,game.camera))

        #창살 제어
        if self.growing==True:
            self.cnt+=15
            self.arrow_up_turn=pygame.transform.scale(self.arrow_up_turn,(840,40+self.cnt))
            game.screen.blit(self.arrow_up_turn,RelRect(160,40,840,40+self.cnt,game.camera))
            if self.cnt==180:
                self.growing=False
        elif self.growing==False:
            self.cnt-=15
            self.arrow_up_turn=pygame.transform.scale(self.arrow_up_turn,(840,40+self.cnt))
            game.screen.blit(self.arrow_up_turn,RelRect(160,40,840,40+self.cnt,game.camera))
            if self.cnt==0:
                self.growing=True


        #박스
        if game.BUTTON_ON1==True:
            game.screen.blit(self.box,RelRect(2360,1240,320,200,game.camera))


        #neon warp door
        if self.ispink:
            game.screen.blit(self.pink_up,RelRect(1880,850,80,40,game.camera))
        game.screen.blit(self.pink_down,RelRect(1680,1415,80,40,game.camera))
        game.screen.blit(self.red_up,RelRect(2630,1160,40,80,game.camera))
        game.screen.blit(self.red_up,RelRect(2000,840,40,80,game.camera))
        game.screen.blit(self.blue_up,RelRect(1800,80,40,80,game.camera))
        game.screen.blit(self.blue_down,RelRect(1680,1130,40,80,game.camera))
        game.screen.blit(self.green_down,RelRect(3400,530,80,40,game.camera))

    def door_open(self,game):
        global GAME_OVER
        if(game.player.rect.x>=3410 and game.player.rect.x<=3430 and game.player.rect.y==70):
            self.timer+=0.5

        if self.timer==5:
            GAME_OVER=True
            return GAME_OVER
