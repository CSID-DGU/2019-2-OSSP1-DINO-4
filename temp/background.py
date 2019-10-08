#background.py
import pygame

class background:

    def __init__(self,width,height):
        self.width=width
        self.height=height

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
            screen.blit(tile1,(x*100,609))


        screen.blit(tile1,(900,450))
        screen.blit(water,(900,43))
        screen.blit(tile1,(800,480))
        screen.blit(tile1,(800,480))
        screen.blit(tile1,(700,520))

        screen.blit(tile1,(0,530))
        screen.blit(tile1,(100,530))
        screen.blit(tile1,(200,490))
        screen.blit(tile1,(300,490))
        screen.blit(tile1,(300,490))
        screen.blit(tile1,(400,450))

        screen.blit(tileup,(470,350))
        screen.blit(tile1,(470,350))
        screen.blit(gray,(470,250))
        screen.blit(tileup,(550,250))

        screen.blit(tile1,(0,390))
        screen.blit(tile1,(100,360))
        screen.blit(tile1,(200,350))
        screen.blit(tileup,(270,250))
        screen.blit(tile1,(270,250))
        screen.blit(redButton,(0,360))
        screen.blit(brick,(300,275))
        screen.blit(tileup,(370,250))
        screen.blit(tile1,(370,250))

        screen.blit(tile1,(700,400))
        screen.blit(water,(700,380))

        screen.blit(tile1,(900,320))
        screen.blit(water,(900,300))
        screen.blit(tile1,(800,320))
        screen.blit(water,(800,300))
        screen.blit(tileup,(770,250))


        screen.blit(tile1,(350,150))
        screen.blit(tile1,(250,150))
        screen.blit(tileup,(450,50))
        screen.blit(tileup,(450,200))
        screen.blit(tileup,(450,150))
        screen.blit(tileup,(450,50))
        screen.blit(tile1,(0,230))
        screen.blit(tile1,(100,230))

        screen.blit(tile1,(600,100))
        screen.blit(tile1,(700,100))
        screen.blit(redButton,(620,70))
        screen.blit(tile1,(560,170))
