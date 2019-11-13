import pygame

class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        #setting
        super().__init__()

        #position
        self.x=x
        self.y=y

        #move
        self.movx=0
        self.movy=0

        self.vel=10 #가속도

        #땅과 충돌검사
        self.contact = False

        #애니메이션 효과 위하여
        self.jump = False
        self.direction="Right"
        self.frame=0

        self.image=pygame.image.load("girl_image/Stand.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))

        #이미지 저장을 위한 변수 및 함수
        self.walk_image=["girl_image/Walk0.png","girl_image/Walk1.png","girl_image/Walk2.png","girl_image/Walk3.png",
                        "girl_image/Walk4.png","girl_image/Walk5.png","girl_image/Walk6.png","girl_image/Walk7.png",
                        "girl_image/Walk8.png","girl_image/Walk9.png","girl_image/Walk10.png","girl_image/Walk11.png"
                        ,"girl_image/Walk12.png","girl_image/Walk13.png","girl_image/Walk14.png","girl_image/Walk15.png",
                        "girl_image/Walk16.png","girl_image/Walk17.png","girl_image/Walk18.png"]

        #self.mask
        self.mask=pygame.mask.from_surface(self.image)

        #self.rect
        self.rect=self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

    #애니메이션 효과
    def update(self,game,up, left, right):
        if up:
            if self.contact:
                if self.direction == "right":
                    self.image = pygame.image.load("girl_image/jump.png").convert_alpha()
                    self.image=pygame.transform.scale(self.image,(50,50))
                self.jump = True
                self.movy -= 20

        if left:
            self.direction = "left"
            self.movx = -self.vel
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.walk_image[self.frame]).convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))
                self.image=pygame.transform.flip(self.image,True,False)
                if self.frame==18: self.frame=0
            else:
                self.image = pygame.image.load("girl_image/jump.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))
                self.image=pygame.transform.flip(self.image,True,False)

        if right:
            self.direction = "right"
            self.movx = +self.vel
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.walk_image[self.frame]).convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))
                if self.frame==18: self.frame=0
            else:
                self.image = pygame.image.load("girl_image/jump.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,(50,50))

        if not (left or right) and self.direction=="right":
            self.movx = 0
            self.image=pygame.image.load("girl_image/stand.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(50,50))
        if not (left or right) and self.direction=="left":
            self.movx = 0
            self.image=pygame.image.load("girl_image/stand.png").convert_alpha()
            self.image=pygame.transform.scale(self.image,(50,50))
            self.image=pygame.transform.flip(self.image,True,False)
        self.rect.x += self.movx

        self.collide(self.movx, 0, game)

        if not self.contact:
            self.movy += 0.3
            if self.movy > 10:
                self.movy = 10
            self.rect.y += self.movy

        if self.jump:
            self.movy += 2.5
            self.rect.y += self.movy
            if self.contact == True:
                self.jump = False

        self.contact = False
        self.collide(0, self.movy, game)

    #배경과 충돌검사
    def collide(self, movx, movy, game):
        self.contact = False
        hit=pygame.sprite.spritecollide(self,game.world,False,pygame.sprite.collide_mask)
        for block in hit:
            if movx>0:
                self.rect.right=block.rect.left
            if movx<0:
                self.rect.left=block.rect.right
            if movy>0:
                self.rect.bottom=block.rect.top
                self.movy=0
                self.contact=True
            if movy<0:
                self.rect.top=block.rect.bottom
                self.movy
