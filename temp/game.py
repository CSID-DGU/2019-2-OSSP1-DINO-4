import pygame
import background
from background import *
from player import *
from const import *

FRAME=0

class Game:
    def __init__(self):
        self.width=900
        self.height=600
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()

    def main(self):
        global FRAME
        pygame.init()

        rect=self.screen.get_rect()
        player1=Player("girl/",(100,520))
        background_=background(self.width,self.height)

        while True:
            time=self.clock.tick(60)
            FRAME+=1
            self.screen.fill((255,193,158))

            player1.update(self.screen)
            background_.background(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
