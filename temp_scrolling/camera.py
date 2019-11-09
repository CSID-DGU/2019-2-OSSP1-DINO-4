import pygame

def RelRect(actor, camera):
    return pygame.Rect(actor.rect.x-camera.rect.x, actor.rect.y-camera.rect.y, actor.rect.w, actor.rect.h)

class Camera(object):
    '''Class for center screen on the player'''
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.center
        self.world_rect = pygame.Rect(0, 0, level_width, level_height)

    def update(self):
      if self.player.centerx > self.rect.centerx + 40:
          self.rect.centerx = self.player.centerx - 40
      if self.player.centerx < self.rect.centerx - 40:
          self.rect.centerx = self.player.centerx + 40
      if self.player.centery > self.rect.centery + 40:
          self.rect.centery = self.player.centery - 40
      if self.player.centery < self.rect.centery - 40:
          self.rect.centery = self.player.centery + 40
      self.rect.clamp_ip(self.world_rect)

    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, RelRect(s, self))