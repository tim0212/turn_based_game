import os, pygame
import screen

class TileObject(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type, surface=None, player_rect = None):
    super().__init__(groups)

    try:
      self.image = pygame.image.load(os.path.join("image", "player.png")).convert_alpha()
    except:
      pygame.draw.rect(screen.surface, (0, 0, 255), player_rect)
    self.sprite_type = sprite_type
    self.image = surface if surface else pygame.Surface((64, 64))
    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
