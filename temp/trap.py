import pygame
import random

class trap:
    def __init__(self,width,height):
        self.width=width #900
        self.height=height #600

    def __call__(self):
        print(" ")

    def trap(self,screen):

        #global fires
        fires=[] # fire 그림 1개가 든 배열

        trap=pygame.image.load("tile/platform_tile_062.png")
        trap=pygame.transform.scale(trap,(100,30))
        saw_tooth=pygame.image.load("tile/platform_tile_072.png")
        saw_tooth=pygame.transform.scale(saw_tooth,(40,40))
        fire1=pygame.image.load("tile/flame_frames.png")
        fire1=pygame.transform.scale(fire1,(100,100))
        fires.append(fire1) #배열에 fire 그림 추가

        for i in range(2): #배열의 나머지 부분에 none 대입
            fires.append(None)
         #--------------------------------------------
        fire_x=500 #변화할 fire의 x 좌표
        fire_y=15 #변화할 fire의 y좌표
        random.shuffle(fires)
        fire=fires[0] #fire변수에 fires 변수의 0번째 값 대입.

        #----------------------



        if fire!=None: #fire배열에 non이면
            fire_y-=7 #불 안나오는 시간
        else:
            fire_y+=30 #fire그림이 들어있어도 x값 당긴다
        if fire_x<=0: #fire의 x값이 음수면
            fire_x=self.width #다시 값을 맨 오른쪽을 w,h 변환
            fire_y=self.height
            fire=fires[0] # 다음 fire의 값을 처음으로 가져다 놓음
        if fire!=None: #none 아닐때에 보임
            screen.blit(fire,(fire_x,fire_y)) #화면에 보임.
        pygame.display.update()



        screen.blit(saw_tooth,(700,260))
        #screen.blit(fire,(500,15))
        #screen.blit(fire,(120,190))
