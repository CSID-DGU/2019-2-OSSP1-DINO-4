import pygame
from game import *

def RelRect(x,y,w,h,camera):
    return pygame.Rect(x-camera.rect.x, y-camera.rect.y, w, h)

class item(pygame.sprite.Sprite):
    """Coins found in boxes and bricks"""
    def __init__(self,game):
        super().__init__()

        self.game=game



        #load gem image
        self.image=pygame.image.load("environment/props/gem-1.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(25,25))

        self.rect = self.image.get_rect()
        self.visible=True

        self.ate=False


    def draw_item(self,game,x,y,mouthOpen):
        self.rect.x=x
        self.rect.y=y
        #collision with player
        hits=pygame.sprite.spritecollide(self,self.game.player_sprite,False,pygame.sprite.collide_mask)

        if hits and mouthOpen:
            self.visible=False
            return
        elif self.visible==True:
            game.screen.blit(self.image,RelRect(x,y,25,25,game.camera))


    def item_blit(self,game):
        game.screen.blit(self.image,RelRect(52,113,40,40,game.camera))



'''
    def update(self, game_info, viewport):
        """Update the coin's behavior"""
        if self.state == c.SPIN:
            self.spinning()

    def spinning(self):
        """Action when the coin is in the SPIN state"""
        self.image = self.frames[self.frame_index]
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if (self.current_time - self.animation_timer) > 80:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0

            self.animation_timer = self.current_time

        if self.rect.bottom > self.initial_height:
            self.kill()
'''
