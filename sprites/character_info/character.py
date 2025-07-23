import os, pygame
from setting import screen, text

class CharactorBase:
  def __init__(self, name, hp, atk, speed):
    self.name = name
    self.max_hp = hp
    self.hp = hp
    self.atk = atk
    self.speed = speed

  def is_alive(self):
    return self.hp > 0

#최적화
dummyEntry_image_cache = None

class DummyEntry(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type):
    super().__init__(groups)
    self.sprite_type = sprite_type

    global dummyEntry_image_cache

    if dummyEntry_image_cache is None:
      try:
        image_path = os.path.join("image", "enemy.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        dummyEntry_image_cache = pygame.transform.scale(raw_image, (32, 32))
      except:
        dummyEntry_image_cache = pygame.Surface((32, 32))
        dummyEntry_image_cache.fill((100, 100, 100))

    self.image = dummyEntry_image_cache.copy()
    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)

    pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 2)  # 적 테두리
class Entry(CharactorBase):
  def __init__(self, name = "앤트리", hp = 300, atk = 20, speed = 15):
    super().__init__(name, hp, atk, speed)

dummyenemy2_image_cache = None

class DummyEnemy2(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type):
    super().__init__(groups)
    self.sprite_type = sprite_type

    global dummyenemy2_image_cache

    if dummyenemy2_image_cache is None:
      try:
        image_path = os.path.join("image", "enemy.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        dummyenemy2_image_cache = pygame.transform.scale(raw_image, (32, 32))
      except:
        dummyenemy2_image_cache = pygame.Surface((32, 32))
        dummyenemy2_image_cache.fill((100, 100, 100))

    self.image = dummyenemy2_image_cache.copy()
    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
class Enemy2(CharactorBase):
  def __init__(self, name = "적2", hp = 300, atk = 20, speed = 10):
    super().__init__(name, hp, atk, speed)

