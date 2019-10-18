#background.py
import pygame

class background:

    def __init__(self,width,height):
        self.width=width #800
        self.height=height #600

    def __call__(self):
        print (" ")

    def background(self,screen):
        tile1=pygame.image.load("tile/platform_tile_002.png").convert_alpha()
        tile1=pygame.transform.scale(tile1,(100,30))
        tile2=pygame.image.load("tile/platform_tile_009.png").convert_alpha()
        tile2=pygame.transform.scale(tile2,(100,60))
        water=pygame.image.load("tile/platform_tile_032.png").convert_alpha()
        water=pygame.transform.scale(water,(100,20))
        tileup=pygame.image.load("tile/platform_tile_005.png").convert_alpha()
        tileup=pygame.transform.scale(tileup,(30,100))
        brick=pygame.image.load("tile/platform_tile_021.png").convert_alpha()
        brick=pygame.transform.scale(brick,(70,70))
        gray=pygame.image.load("tile/platform_tile_016.png").convert_alpha()
        gray=pygame.transform.scale(gray,(100,30))
        redButton=pygame.image.load("tile/platform_tile_038.png").convert_alpha()
        redButton=pygame.transform.scale(redButton,(30,30))
        door=pygame.image.load("tile/New Piskel (1) (1).png").convert_alpha()
        door=pygame.transform.scale(door,(100,100))
        door2=pygame.image.load("tile/New Piskel (1) (2).png").convert_alpha()
        door2=pygame.transform.scale(door2,(100,100))
        arrow=pygame.image.load("tile/platform_tile_064.png").convert_alpha()
        arrow=pygame.transform.scale(arrow,(60,20))
        #neon warp door
        blue_up=pygame.image.load("tile/blue_up.png").convert_alpha()
        blue_up=pygame.transform.scale(blue_up,(60,100))
        blue_down=pygame.image.load("tile/blue_neon_down.png").convert_alpha()
        blue_down=pygame.transform.scale(blue_down,(100,60))
        red_up=pygame.image.load("tile/red_up.png").convert_alpha()
        red_up=pygame.transform.scale(red_up,(60,100))
        pink_up=pygame.image.load("tile/pink_neon_up.png").convert_alpha()
        pink_up=pygame.transform.scale(pink_up,(60,100))
        pink_down=pygame.image.load("tile/pink_neon.png").convert_alpha()
        pink_down=pygame.transform.scale(pink_down,(110,60))
        green_down=pygame.image.load("tile/green_neon.png").convert_alpha()
        green_down=pygame.transform.scale(green_down,(110,60))


        for x in range(self.width//tile1.get_width()+1):
            screen.blit(tile1,(x*100,0))
        for x in range(self.width//tile1.get_width()+1):
            screen.blit(tile1,(x*100,570))
            
        #screen.blit(tile1,(0,490))
        #screen.blit(tile1,(100,490))
        #screen.blit(tile1,(200,490))
        #screen.blit(tile1,(300,470))
        #screen.blit(tile1,(400,450))

        #screen.blit(tile1,(700,480))
        #screen.blit(tile1,(800,480))

        #screen.blit(tileup,(470,350))
        #screen.blit(tile1,(470,350))
        #screen.blit(gray,(470,250))
        #screen.blit(tileup,(540,250))

        #screen.blit(tile1,(0,380))
        #screen.blit(tile1,(100,350))
        #screen.blit(tile1,(200,350))
        #screen.blit(tileup,(270,250))
        #screen.blit(tile1,(270,250))
        #screen.blit(redButton,(10,350))
        #screen.blit(brick,(300,275))
        #screen.blit(tileup,(370,250))
        #screen.blit(tile1,(370,250))

        #screen.blit(tile1,(600,420))
        #screen.blit(water,(600,400))

        #screen.blit(tile1,(800,320))
        #screen.blit(water,(800,300))
        #screen.blit(tile1,(700,320))
        #screen.blit(water,(700,300))
        #screen.blit(tileup,(670,250))

        #screen.blit(tile1,(350,110))
        #screen.blit(tile1,(250,110))
        #screen.blit(tileup,(450,30))
        #screen.blit(tileup,(450,180))
        #screen.blit(tileup,(450,150))
        #screen.blit(tileup,(450,50))
        #screen.blit(tile1,(0,200))
        #screen.blit(tile1,(100,200))

        #screen.blit(tile1,(600,100))
        #screen.blit(tile1,(700,100))
        #screen.blit(redButton,(620,70))
        #screen.blit(tile1,(520,180))

        #screen.blit(door,(825,490))
        #screen.blit(door,(765,490))

        #arrow
        screen.blit(arrow,(700,80))
        screen.blit(arrow,(100,470))
        screen.blit(arrow,(500,550))
        screen.blit(arrow,(150,330))
        screen.blit(arrow,(300,450))

        #neon warp door
        screen.blit(blue_up,(150,500))
        screen.blit(blue_up,(700,495))
        screen.blit(red_up,(850,15))
        screen.blit(red_up,(850,390))
        screen.blit(pink_down,(300,10))
        screen.blit(pink_up,(0,400))
        screen.blit(green_down,(780,230))
        screen.blit(green_down,(565,280))
