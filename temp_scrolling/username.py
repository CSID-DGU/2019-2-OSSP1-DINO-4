import pygame

from os import path
from background_platform import *
from background import *
from s3_transfer import *

SCREEN_WIDTH=1000
SCREEN_HEIGHT=700

validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

class username:
    def __init__(self,screen,clock,highscore):
        super().__init__()

        self.screen=screen
        self.clock=clock
        self.font_name=pygame.font.match_font('arial')
        self.WHITE=(255,255,255)
        self.BLACK=(0,0,0)
        self.ORANGE=(255,193,158)
        #self.textRect=self.textRect=self.text_objects("Instruction",FONT)
        self.highscore=highscore
        self.score=0

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

        self.text = ""
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render("Enter your name", False, [0, 0, 0])
        self.rect = self.image.get_rect()


    def add_chr(self, char):
        shiftDown=False
        if char in validChars and not shiftDown:
            self.text += char
        elif char in validChars and shiftDown:
            self.text += shiftChars[validChars.index(char)]
        self.update()

    def update(self):
        old_rect_pos = self.rect.center
        self.image = self.font.render(self.text, False, [0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_pos

    #화면에 글씨 쓰기
    def draw_text(self,surf,text,size,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,self.BLACK) #픽셀, TRUE는 ALIAS인지
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        surf.blit(text_surface,text_rect)

    def show_username_screen(self,score,dir):
        HS_FILE="highscore.txt"
        clock = pygame.time.Clock()
        self.score=str(score)
        textBox=username(self.screen,clock,0)
        shiftDown = False
        self.dir=dir
        textBox.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/7+300]
        #self.screen.fill((67,116,217))


        running = True
        while running:
          self.screen.fill([255, 255, 255])
          self.screen.blit(self.bg_sky,(0,0))
          self.screen.blit(textBox.image, textBox.rect)

          self.draw_text(self.screen,"Your Score:",80,SCREEN_WIDTH/2,SCREEN_HEIGHT/7)
          self.draw_text(self.screen,self.score,100,SCREEN_WIDTH/2,SCREEN_HEIGHT/7+70)
          pygame.display.flip()
          for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYUP:
                if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = False
            if e.type == pygame.KEYDOWN:
                textBox.add_chr(pygame.key.name(e.key))
                if e.key == pygame.K_SPACE:
                    textBox.text += " "
                    textBox.update()
                if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = True
                if e.key == pygame.K_BACKSPACE:
                    textBox.text = textBox.text[:-1]
                    textBox.update()
                if e.key == pygame.K_RETURN:
                    if len(textBox.text) > 0:
                        print (textBox.text)
                        running = False

        print("setl.txt해봄")
        print(self.text)
        with open(path.join(self.dir,HS_FILE),'w') as f:
            f.write(self.text)

        #aws s3 스토리지에 업로드
        upload_s3_now()

        return self.text
