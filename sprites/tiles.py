import os, pygame
from setting import screen, text

class TileObject(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type, surface=None, player_rect=None):
    super().__init__(groups)
    self.sprite_type = sprite_type

    if surface:
      # surface가 외부에서 전달된 경우
      self.image = pygame.transform.scale(surface, (32, 32))
    else:
      try:
        # 이미지 파일 로드
        image_path = os.path.join("image", "tile.png")  # 타일 전용 이미지 추천
        raw_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (32, 32))
      except:
        # 이미지 로드 실패 시 임시 Surface
        self.image = pygame.Surface((32, 32))
        self.image.fill((100, 100, 100))  # 회색 임시 타일
        if player_rect:
          pygame.draw.rect(self.image, (0, 0, 255), player_rect)

    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
