import os, pygame
from .character import CharactorBase

class DummyTraveler(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type, surface=None):
    pygame.sprite.Sprite.__init__(self, groups)

    self.sprite_type = sprite_type

    if surface:
      # 외부에서 surface를 넘기면 강제로 크기 제한 나중에 지울예정 (아마도)
      self.image = pygame.transform.scale(surface, (32, 32))
    else:
      try:
        image_path = os.path.join("image", "player.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (32, 32))
      except:
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 255))

    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)

  def get_rect(self):
    return self.rect
class Traveler(CharactorBase):
  def __init__(self, name = "여행객", hp = 210, atk = 90, speed = 20):
    super().__init__(name, hp, atk, speed)

    