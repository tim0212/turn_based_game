import pygame

class Camera:
  def __init__(self, player_rect, screen_size):
    self.offset = pygame.Vector2(0, 0)
    self.player_rect = player_rect
    self.screen_center = pygame.Vector2(screen_size[0] // 2, screen_size[1] // 2)

  def update(self):
    player_center = pygame.Vector2(self.player_rect.center)
    self.offset = player_center - self.screen_center

  def apply(self, target_rect):
    """
    draw용 위치 계산
    target_rect: sprite.rect (월드 좌표)
    return: 화면에 그릴 위치
    """
    return pygame.Vector2(target_rect.topleft) - self.offset

  def draw_group(self, surface, sprite_group):
    for sprite in sprite_group:
      draw_pos = self.apply(sprite.rect)
      surface.blit(sprite.image, draw_pos)

  def draw_sprite(self, surface, sprite):
    draw_pos = self.apply(sprite.rect)
    surface.blit(sprite.image, draw_pos)
