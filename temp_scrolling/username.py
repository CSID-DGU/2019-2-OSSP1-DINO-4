import pygame
import os

from db import *
from os import path
from background_platform import *
from background import *
from s3_transfer import *

SCREEN_WIDTH=1000
SCREEN_HEIGHT=700

validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

"""
class Score:
    def __init__(self):
        super().__init__()

    def get_high_scores(self,file_name):
        #메모장
        content = ""

        HS_FILE=file_name
        self.dir=path.dirname(__file__)

        if os.path.isfile(file_name):
            with open(path.join(self.dir,HS_FILE),'r') as f:
                content=f.read()
        else:
            with open(path.join(self.dir,HS_FILE),'w') as f:
                content = "first::0,second::0,third::0" #We also set content with the default values to avoid any errors in future code
                f.write(content) #write the contents to file
                f.close() #close the file

        content_list = content.split(',')
        to_return = {}

        for element in content_list: #For each element in list 
            l = element.split(':')
            to_return[l[0]] = [l[1], l[2]] 

        return to_return #return the dictionary

    def write_high_scores(self,file_name, scores):
        f = open(file_name, 'w') #open the file for writing
        to_write = "" #create an empty string to store the data we will write to our file
        #cycle through the different scores, writing the values in the correct format and adding them to the string 
        for name in ('first', 'second', 'third'): 
            to_write += name
            to_write += ':'
            to_write += str(scores.get(name)[0])
            to_write += ':'
            to_write += str(scores.get(name)[1])
            to_write += ','

        #print(to_write)
        to_write = to_write[:-1] #Remove the last character from the two_write string - this is an unnecessary comma created by our loop
        f.write(to_write) #write the string to the file
        f.close() #close the file

    def set_high_score(self,file_name, player_name, score):
    
    
        scores = self.get_high_scores(file_name) #get a dictionary of the current high scores
        print(scores['first'][1]+","+scores['second'][1]+","+scores['third'][1])
        print(int(score))
    #If we have a new high score, update the values in the dictionary
        if (int(score) >= int(scores.get('first')[1])): 
            #새로운 1등 생기면 나머지 뒤로 밀림
            print("1등")

            scores['third'][0] = scores['second'][0]
            scores['third'][1] = scores['second'][1]
            scores['second'][0] = scores['first'][0]
            scores['second'][1] = scores['first'][1]

            scores['first'][0] = player_name
            scores['first'][1] = score

    #Else if we have a new next highest score, update this value
        elif (int(score) >= int(scores.get('second')[1])):
            print("2등")

            scores['third'][0] = scores['second'][0]
            scores['third'][1] = scores['second'][1]

            scores['second'][0] = player_name
            scores['second'][1] = score

    #Else if our score is lower than anyone elses, update this value.
        elif (int(score) >= int(scores.get('third')[1])):
            print("3등  ")
            scores['third'][0] = player_name
            scores['third'][1] = score

        #self.write_high_scores(file_name, scores)
        #print(scores)

        return scores
"""



class username:
    def __init__(self,screen):
        super().__init__()

        self.screen=screen
        self.font_name=pygame.font.match_font('arial')
        self.WHITE=(255,255,255)
        self.BLACK=(0,0,0)
        self.ORANGE=(255,193,158)
        #self.textRect=self.textRect=self.text_objects("Instruction",FONT)
        #self.highscore=highscore
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

        self.old_rect_pos = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.text = ""
        self.font = pygame.font.Font(None,60)
        self.image = self.font.render("Enter your name", 0, [0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = self.old_rect_pos
        self.scores=None


        #self.score_=Score()


    def add_chr(self, char):
        shiftDown=False
        if char in validChars and not shiftDown:
            self.text += char
        elif char in validChars and shiftDown:
            self.text += shiftChars[validChars.index(char)]
        self.update()

    def update(self):
        self.image = self.font.render(self.text, False, [0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = self.old_rect_pos

    #화면에 글씨 쓰기
    def draw_text(self,surf,text,size,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,self.BLACK) #픽셀, TRUE는 ALIAS인지
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        surf.blit(text_surface,text_rect)

    def print_ranking(self):
        rank=show_ranking()
        self.draw_text(self.screen,"1st :"+str(rank[0][1])+"("+str(rank[0][2])+" seconds)",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3)
        self.draw_text(self.screen,"2nd :"+str(rank[1][1])+"("+str(rank[1][2])+" seconds)",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3+50)
        self.draw_text(self.screen,"3rd :"+str(rank[2][1])+"("+str(rank[2][2])+" seconds)",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3+100)

    def show_username_screen(self,score,dir):
        HS_FILE="highscore.txt"
        clock = pygame.time.Clock()
        self.score=str(score)
        textBox=username(self.screen)
        shiftDown = False
        self.dir=dir
        textBox.rect.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
        #self.screen.fill((67,116,217))


        running = True
        while running:
            self.screen.fill([255, 255, 255])
            self.screen.blit(self.bg_sky,(0,0))
            self.screen.blit(textBox.image, textBox.rect)

            self.draw_text(self.screen,"Your Score:",60,SCREEN_WIDTH/2,SCREEN_HEIGHT/10)
            self.draw_text(self.screen,self.score,60,SCREEN_WIDTH/2,SCREEN_HEIGHT/10+70)

            """
            if os.path.isfile(HS_FILE):
                self.draw_text(self.screen,"1st : ",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3)
                self.draw_text(self.screen,"2nd :",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3+50)
                self.draw_text(self.screen,"3rd :",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3+100)
            else:
                self.draw_text(self.screen,"1st :"+self.scores['first'][0]+"("+self.scores['first'][1]+" seconds)",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3)
                self.draw_text(self.screen,"2nd :"+self.scores['second'][0]+"("+self.scores['second'][1]+" seconds)",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3+50)
                self.draw_text(self.screen,"3rd :"+self.scores['third'][0]+"("+self.scores['third'][1]+" seconds)",40,SCREEN_WIDTH/2,(SCREEN_HEIGHT/5)*3+100)"""

            self.print_ranking()
            
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
                        #print (textBox.text)
                            running = False
                            insert_score(textBox.text,self.score)


        """
        print("setl.txt해봄")
        print(self.text)
        with open(path.join(self.dir,HS_FILE),'w') as f:
            f.write(self.text)"""

        #aws s3 스토리지에 업로드
        #upload_s3_now()

        return self.text
