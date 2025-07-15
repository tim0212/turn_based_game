import os, pygame
from .character_base import CharacterBase

class Trailblazer(pygame.sprite.Sprite, CharacterBase):
  def __init__(self, pos, groups, sprite_type, surface=None):
    pygame.sprite.Sprite.__init__(self, groups)
    CharacterBase.__init__(self, name="Trailblazer", hp=100, atk=20)

    self.sprite_type = sprite_type

    if surface:
      # 외부에서 surface를 넘기면 강제로 크기 제한
      self.image = pygame.transform.scale(surface, (32, 32))
    else:
      try:
        image_path = os.path.join("image", "player.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (32, 32))
      except:
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 255))  # 파란색 기본 플레이어

    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)

  def ReturnTheRect(self):
    return self.rect
