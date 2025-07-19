import os, pygame
from setting import screen, text

class CharactorBase:
  def __init__(self, name, hp, atk):
    self.name = name
    self.max_hp = hp
    self.hp = hp
    self.atk = atk

  def is_alive(self):
    return self.hp > 0

#최적화
enemy_image_cache = None

class Entry(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type):
    super().__init__(groups)
    self.sprite_type = sprite_type

    global enemy_image_cache

    if enemy_image_cache is None:
      try:
        image_path = os.path.join("image", "enemy.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        enemy_image_cache = pygame.transform.scale(raw_image, (32, 32))
      except:
        enemy_image_cache = pygame.Surface((32, 32))
        enemy_image_cache.fill((100, 100, 100))
      self.image = enemy_image_cache.copy()

    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)

    pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 2)  # 적 테두리 빨간색