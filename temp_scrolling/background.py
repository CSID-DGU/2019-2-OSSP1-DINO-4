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

    def background_blit(self,game):
        #neon warp door
        game.screen.blit(self.red_up,RelRect(3000,1160,40,80,game.camera))
        game.screen.blit(self.red_up,RelRect(1560,560,40,80,game.camera))
