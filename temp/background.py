#background.py
import pygame

class background:

    def __init__(self,width,height):
        self.width=width #800
        self.height=height #600

    def __call__(self):
        print (" ")


    def background(self,screen):
        tile1=pygame.image.load("tile/platform_tile_002.png")
        tile1=pygame.transform.scale(tile1,(100,30))
        tile2=pygame.image.load("tile/platform_tile_009.png")
        tile2=pygame.transform.scale(tile2,(100,60))
        water=pygame.image.load("tile/platform_tile_032.png")
        water=pygame.transform.scale(water,(100,20))
        tileup=pygame.image.load("tile/platform_tile_005.png")
        tileup=pygame.transform.scale(tileup,(30,100))
        brick=pygame.image.load("tile/platform_tile_021.png")
        brick=pygame.transform.scale(brick,(70,70))
        gray=pygame.image.load("tile/platform_tile_016.png")
        gray=pygame.transform.scale(gray,(100,30))
        redButton=pygame.image.load("tile/platform_tile_038.png")
        redButton=pygame.transform.scale(redButton,(30,30))

        for x in range(self.width//tile1.get_width()+1):
            screen.blit(tile1,(x*100,0))
        for x in range(self.width//tile1.get_width()+1):
            screen.blit(tile1,(x*100,570))

        #수정완료
        screen.blit(tile1,(0,490))
        screen.blit(tile1,(100,490))
        screen.blit(tile1,(200,490))
        screen.blit(tile1,(300,470))
        screen.blit(tile1,(400,450))


        #수정 완료
        screen.blit(tile1,(700,480))
        screen.blit(tile1,(800,480))

        #수정완료
        screen.blit(tileup,(470,350))#
        screen.blit(tile1,(470,350))
        screen.blit(gray,(470,250))
        screen.blit(tileup,(540,250))

        #수정중
        screen.blit(tile1,(0,380))
        screen.blit(tile1,(100,350))
        screen.blit(tile1,(200,350))
        screen.blit(tileup,(270,250))
        screen.blit(tile1,(270,250))
        screen.blit(redButton,(0,350))
        screen.blit(brick,(300,275))
        screen.blit(tileup,(370,250))
        screen.blit(tile1,(370,250))

        #수정 완료
        screen.blit(tile1,(600,420))
        screen.blit(water,(600,400))


        #수정 완료
        screen.blit(tile1,(800,320))
        screen.blit(water,(800,300))
        screen.blit(tile1,(700,320))
        screen.blit(water,(700,300))
        screen.blit(tileup,(670,250))

        #수정완료
        screen.blit(tile1,(350,110))
        screen.blit(tile1,(250,110))
        screen.blit(tileup,(450,30))#
        screen.blit(tileup,(450,180))#
        screen.blit(tileup,(450,150))
        screen.blit(tileup,(450,50))
        screen.blit(tile1,(0,200))
        screen.blit(tile1,(100,200))

        #수정 완료
        screen.blit(tile1,(600,100))
        screen.blit(tile1,(700,100))
        screen.blit(redButton,(620,70))
        screen.blit(tile1,(520,180))
