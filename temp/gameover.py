import pygame
import player
import const


SPRITE_SCALING=0.5
SCREEN_WIDTH=900
SCREEN_HEIGHT=600
SCREEN_TITLE="GAME OVER"


class gameover:
    def __init__(self,screen,clock):
        super().__init__()
        self.screen=screen
        self.clock=clock
        #글씨체
        self.font_name=pygame.font.match_font('arial')
        self.WHITE=(255,255,255)
        self.ORANGE=(255,193,158)

    #화면에 글씨 쓰기
    def draw_text(self,surf,text,size,x,y):
        font=pygame.font.Font(self.font_name,size)
        text_surface=font.render(text,True,self.WHITE) #픽셀, TRUE는 ALIAS인지
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        surf.blit(text_surface,text_rect)

    def show_start_screen(self):
        self.screen.fill(self.ORANGE)
        self.draw_text(self.screen,"DINO",64,SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        self.draw_text(self.screen,"Arrow keys move, Space to fire",22,SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.draw_text(self.screen,"Press a key to begin",18,SCREEN_WIDTH/2,SCREEN_HEIGHT*3/4)

        waiting=True
        while waiting:
            self.clock.tick(100000)
            for event in pygame.event.get():
                #quit X 누르면 종료
                if event.type==pygame.QUIT:
                    pygame.quit()
                #아무키나 둘러도 가능하도록
                if event.type==pygame.KEYUP:
                    waiting=False


    def show_gameover_screen(self):
        self.screen.fill(self.ORANGE)
        self.draw_text(self.screen,"GAME OVER",64,SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
        self.draw_text(self.screen,"Arrow keys move, Space to fire",22,SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.draw_text(self.screen,"Press a key to begin",18,SCREEN_WIDTH/2,SCREEN_HEIGHT*3/4)
        pygame.display.flip()

        waiting=True
        while waiting:
            self.clock.tick(100000)
            for event in pygame.event.get():
                #quit X 누르면 종료
                if event.type==pygame.QUIT:
                    pygame.quit()
                #아무키나 둘러도 가능하도록
                if event.type==pygame.KEYUP:
                    waiting=False
