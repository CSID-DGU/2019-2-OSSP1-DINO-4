import pygame

from os import path
from background_platform import *
from background import *

SCREEN_WIDTH=1000
SCREEN_HEIGHT=700

class gameover:
    def __init__(self,screen,clock,highscore,FONT):
        super().__init__()

        self.screen=screen
        self.clock=clock
        self.font_name=pygame.font.match_font('arial')
        self.WHITE=(255,255,255)
        self.ORANGE=(255,193,158)
        self.textRect=self.textRect=self.text_objects("Instruction",FONT)
        self.highscore=highscore
        self.score=0
        self.numOfPressedButton=0

        self.bg_sky=pygame.image.load("tile/sky.png").convert_alpha()
        self.bg_sky=pygame.transform.scale(self.bg_sky,(1000,700))
        self.bg_middle=pygame.image.load("tile/middle.png").convert_alpha()
        self.bg_middle=pygame.transform.scale(self.bg_middle,(200,600))
        self.grass_tile1=pygame.image.load("tile/grasstile1.png").convert_alpha()
        self.grass_tile1=pygame.transform.scale(self.grass_tile1,(40,40))
        self.purple_stone=pygame.image.load("tile/purple_stone.png").convert_alpha()
        self.purple_stone=pygame.transform.scale(self.purple_stone,(40,40))
        self.purple_stones=pygame.image.load("tile/purple_stones.png").convert_alpha()
        self.purple_stones=pygame.transform.scale(self.purple_stones,(40,40))
        self.purple_tile=pygame.image.load("tile/purple_tile.png").convert_alpha()
        self.purple_tile=pygame.transform.scale(self.purple_tile,(40,40))
        self.dirt_tile=pygame.image.load("tile/dirt_tile.png").convert_alpha()
        self.dirt_tile=pygame.transform.scale(self.dirt_tile,(40,40))
        self.tree=pygame.image.load("tile/tree.png").convert_alpha()
        self.tree=pygame.transform.scale(self.tree,(140,180))
        self.bush=pygame.image.load("tile/bush.png").convert_alpha()
        self.bush=pygame.transform.scale(self.bush,(40,40))
        self.grass_left=pygame.image.load("tile/grass_left.png").convert_alpha()
        self.grass_left=pygame.transform.scale(self.grass_left,(50,60))
        self.house=pygame.image.load("tile/house.png").convert_alpha()
        self.house=pygame.transform.scale(self.house,(130,180))

    #화면에 글씨 쓰기
    def draw_text(self,surf,text,size,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,self.WHITE) #픽셀, TRUE는 ALIAS인지
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        surf.blit(text_surface,text_rect)

    def text_objects(self,text,font):
        textsurface=font.render(text,True,(0,123,0))
        return textsurface,textsurface.get_rect()


    #버튼 생성 action에 따라 버튼 클릭 시 행위 바뀜
    def button(self,msg,x,y,w,h,ic,ac,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(self.screen,ac,(x,y,w,h))
            if click[0]==1 and action!=None:
                if action=="restart":
                    self.numOfPressedButton=1
                elif action=="paused":
                    return 2
                elif action=="continue":
                    self.numOfPressedButton=3
                    return
                elif action=="quit":
                    pygame.quit()
                    quit()
                    sys.exit()

        else:
            pygame.draw.rect(self.screen,ic,(x,y,w,h))
            return 0
        smalltext=pygame.font.Font("freesansbold.ttf",20)
        textsurf=self.text_objects(msg,smalltext)
        textrect=self.text_objects(msg,smalltext)
        self.draw_text(self.screen,msg,35,x+60,y)

    def pausePressed(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            #self.screen.fill((255,193,158))
            self.screen.blit(self.bg_sky,(0,0))
            for x in range(SCREEN_WIDTH//self.bg_middle.get_width()+1):
                self.screen.blit(self.bg_middle,(x*200,200))

            largeText=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=self.text_objects("Paused",largeText)
            TextRect.center=((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
            self.screen.blit(TextSurf,TextRect)
            self.button("Continue",150,450,150,50,(134,199,127),(47,157,39),"continue")
            self.button("Restart",350,450,150,50,(103,153,255),(0,51,153),"restart")
            self.button("Quit",550,450,150,50,(241,95,95),(152,0,0),"quit")
            if self.numOfPressedButton!=0:
                if self.numOfPressedButton==1:
                    self.numOfPressedButton=0
                    return 1
                self.numOfPressedButton=0
                break

            pygame.display.update()
            self.clock.tick(30)

    def show_gameover_screen(self,score,dir):
        HS_FILE="highscore.txt"
        self.score=score
        self.dir=dir

        self.screen.blit(self.bg_sky,(0,0))
        #self.screen.fill((67,116,217))
        for x in range(4):
            self.screen.blit(self.bg_middle,(x*200,200))


        for x in range(SCREEN_WIDTH//self.bg_middle.get_width()+1):
            for y in range(SCREEN_HEIGHT//self.purple_tile.get_width()+1):
                self.screen.blit(self.purple_tile,(x*20-10,415+y*20-10))

        for y in range(SCREEN_HEIGHT//self.dirt_tile.get_width()+1):
            self.screen.blit(self.dirt_tile,(90,400+y*20))
        for x in range(SCREEN_WIDTH//self.bg_middle.get_width()+1):
            self.screen.blit(self.grass_tile1,(x*20-10,390))

        self.screen.blit(self.purple_stones,(40,500))
        self.screen.blit(self.purple_stones,(70,420))
        self.screen.blit(self.purple_stone,(20,600))
        self.screen.blit(self.purple_stone,(60,520))
        self.screen.blit(self.tree,(25,220))

        for x in range(SCREEN_WIDTH//self.grass_tile1.get_width()+1):
            self.screen.blit(self.grass_tile1,(400+x*20,390))

        self.screen.blit(self.grass_tile1,(130,390))
        self.screen.blit(self.grass_tile1,(350,390))
        self.screen.blit(self.grass_tile1,(300,450))
        self.screen.blit(self.grass_tile1,(200,500))
        self.screen.blit(self.grass_left,(925,370))
        self.screen.blit(self.grass_tile1,(960,390))
        self.screen.blit(self.bush,(690,355))
        self.screen.blit(self.house,(760,220))

        for x in range(1000):
            for y in range(700):
                self.screen.blit(self.purple_tile,(400+x*20,412+y*20))

        for y in range(SCREEN_HEIGHT//self.dirt_tile.get_width()+1):
            self.screen.blit(self.dirt_tile,(400,400+y*20))


        self.draw_text(self.screen,"DINO",100,SCREEN_WIDTH/2,SCREEN_HEIGHT/7)
        self.draw_text(self.screen,">Arrow keys move, Space to fire",22,SCREEN_WIDTH/2+55,SCREEN_HEIGHT/2+100)
        self.draw_text(self.screen,">Press a key to begin",22,SCREEN_WIDTH/2+15,SCREEN_HEIGHT*3/4)

        #SCORE 관련 표시하기
        if self.score>self.highscore:
            self.highscore=self.score
            self.draw_text(self.screen,"NEW HIGH SCORE!",22,SCREEN_WIDTH/2+200,SCREEN_HEIGHT/2+250)
            self.draw_text(self.screen,">Highest Score: "+str(self.score),22,SCREEN_WIDTH/2,SCREEN_HEIGHT/2+250)
            with open(path.join(self.dir,HS_FILE),'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text(self.screen,">Highest Score: "+str(self.highscore),22,SCREEN_WIDTH/2,SCREEN_HEIGHT/2+250)
        pygame.display.flip()

        #start_time=None #gameover이므로
        waiting=True
        while waiting:
            self.clock.tick(100000)
            for event in pygame.event.get():
                #quit X 누르면 종료
                if event.type==pygame.QUIT:
                    pygame.quit()
                #아무키나 둘러도 가능하도록
                if event.type==pygame.KEYUP:
                    waiting=False
