import pygame
import random

FRAME=0

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

class Dino(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        super().__init__()

        self.game=game
        self.user_position=[x,y]
        self.user_image=[]
        self.event_list=[False for i in range(2)]
        self.load_sprites()

        self.is_right=True
        self.walk_distance=x

        
    def load_sprites(self):
        #걷기
        path="dino/"
        walk_sprite=['dino-0'+str(i)+'.png' for i in range(1,8)]
        walk_right=[pygame.image.load(path+i).convert_alpha()
                         for i in walk_sprite]
        walk_right=[pygame.transform.scale(i,(120,120))
                        for i in walk_right]
        walk_left=[pygame.transform.flip(i,True,False)
                        for i in walk_right]

        self.user_image.append(walk_right)
        self.user_image.append(walk_left)


    def EventHandler(self):
        global FRAME
        FRAME+=0.2

        distance=random.randrange(10,300)
        speed=random.randrange(0,5)
        if self.is_right:
            if self.user_position[0]>self.walk_distance+distance:
                self.is_right=False
            else:
                self.user_position[0] += speed

        else:
            if self.user_position[0]<self.walk_distance-distance:
                self.is_right=True
            else:
                self.user_position[0] -= speed
            

    def update(self,game):
        if game.box2_hit is False:
            self.image=pygame.image.load("dino/Dead (6).png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(120,120))
            self.rect=self.image.get_rect()
            self.mask=pygame.mask.from_surface(self.image)
            self.rect.x=self.user_position[0]
            self.rect.y=self.user_position[1]
            game.screen.blit(self.image,RelRect(self.user_position[0],self.user_position[1],120,120,game.camera))
        else:
            self.EventHandler()

        if game.box2_hit is True and self.is_right==True:
            game.screen.blit(self.user_image[0][int(FRAME)%7],RelRect(self.user_position[0],self.user_position[1],120,120,game.camera))
            self.rect=self.user_image[0][int(FRAME)%7].get_rect()
            self.mask=pygame.mask.from_surface(self.user_image[0][int(FRAME)%7])
            self.rect.x=self.user_position[0]
            self.rect.y=self.user_position[1]
        elif game.box2_hit is True and self.is_right==False:
            game.screen.blit(self.user_image[1][int(FRAME)%7],RelRect(self.user_position[0],self.user_position[1],120,120,game.camera))
            self.rect=self.user_image[1][int(FRAME)%7].get_rect()
            self.mask=pygame.mask.from_surface(self.user_image[1][int(FRAME)%7])
            self.rect.x=self.user_position[0]
            self.rect.y=self.user_position[1]