import os, pygame
from setting import screen, text
from setting.math import *

class CharactorBase:
  def __init__(self, name, hp, atk, speed):
    self.name = name
    self.max_hp = hp
    self.hp = hp
    self.atk = atk
    self.speed = speed
  def __hash__(self):
    return hash(id(self))
  def __eq__(self, other):
    return id(self) == id(other)
  def __repr__(self):
    return f"{self.name}(HP: {self.hp}, SPD: {self.speed})"

  def is_alive(self):
    return self.hp > 0

  #HP그림 HP게이지 바 P는 player E는 enemy
  def draw_hp_barP(self, pos, width=100, height=6):
    x, y = pos
    bar_x = x -120
    bar_y = y + 32

    pygame.draw.rect(screen.surface, (80, 80, 80), (bar_x, bar_y, width, height))

    # 체력 비율
    hp_ratio = self.hp / self.max_hp
    hp_width = int(width * hp_ratio)

    pygame.draw.rect(screen.surface, (0, 255, 0), (bar_x, bar_y, hp_width, height))
    text.render((pos[0] - 42, pos[1] + 20), str(limit(self.hp, 0, inf)), False, (255, 255, 255), centerpos= "topleft", size = 20)

  def draw_hp_barE(self, pos, width=100, height=6):
    x, y = pos
    bar_x = x + 55
    bar_y = y + 32

    pygame.draw.rect(screen.surface, (80, 80, 80), (bar_x, bar_y, width, height))

    # 체력 비율
    hp_ratio = self.hp / self.max_hp
    hp_width = int(width * hp_ratio)

    pygame.draw.rect(screen.surface, (0, 255, 0), (bar_x, bar_y, hp_width, height))
    text.render((pos[0] + 55, pos[1] + 20), str(limit(self.hp, 0, inf)), False, (255, 255, 255), centerpos= "topleft", size = 20)

dummyEntry_image_cache = None
class DummyEntry(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type):
    super().__init__(groups)
    self.sprite_type = sprite_type

    global dummyEntry_image_cache

    if dummyEntry_image_cache is None:
      try:
        image_path = os.path.join("image", "character_img", "enemy.png")
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
  def __init__(self, name = "Entry", hp = 300, atk = 20, speed = 15):
    super().__init__(name, hp, atk, speed)

    try:
      image_path = os.path.join("image", "character_img", "enemy.png")
      self.image = pygame.image.load(image_path).convert_alpha()
    except:
      self.image = pygame.Surface((32, 32))
      self.image.fill((255, 0, 0))

  def anime_update(self, event : str):
    pass

  def draw(self, pos):
    screen.surface.blit(self.image, pos)
    self.draw_hp_barE(pos)

dummyenemy2_image_cache = None
class DummyEnemy2(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type):
    super().__init__(groups)
    self.sprite_type = sprite_type

    global dummyenemy2_image_cache

    if dummyenemy2_image_cache is None:
      try:
        image_path = os.path.join("image", "character_img", "enemy.png")
        raw_image = pygame.image.load(image_path).convert_alpha()
        dummyenemy2_image_cache = pygame.transform.scale(raw_image, (32, 32))
      except:
        dummyenemy2_image_cache = pygame.Surface((32, 32))
        dummyenemy2_image_cache.fill((100, 100, 100))

    self.image = dummyenemy2_image_cache.copy()
    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
class Enemy2(CharactorBase):
  def __init__(self, name = "Enemy", hp = 300, atk = 20, speed = 10):
    super().__init__(name, hp, atk, speed)

    try:
      image_path = os.path.join("image", "character_img", "enemy.png")
      self.image = pygame.image.load(image_path).convert_alpha()
    except:
      self.image = pygame.Surface((32, 32))
      self.image.fill((255, 100, 0))

  def anime_update(self, event : str):
    pass

  def draw(self, pos):
    screen.surface.blit(self.image, pos)
    self.draw_hp_barE(pos)
