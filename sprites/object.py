import os, pygame

# 최적화용 캐시
tile_image_cache = {}
obstacle_image_cache = {}

class TileObject(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type, tile_code="x", test=False):
    super().__init__(groups)
    from sprites.settings import TILE_TYPES

    self.sprite_type = sprite_type

    if test:
      # 테스트 모드에서는 색상 기반 surface
      color = TILE_TYPES.get(tile_code, {"color": (150, 150, 150)})["color"]
      self.image = pygame.Surface((32, 32))
      self.image.fill(color)
    else:
      # 실제 이미지 로드
      if tile_code in tile_image_cache:
        self.image = tile_image_cache[tile_code]
      else:
        img_path = TILE_TYPES.get(tile_code, {}).get("img", None)
        if img_path and os.path.exists(img_path):
          image = pygame.image.load(img_path).convert_alpha()
          scaled_image = pygame.transform.scale(image, (32, 32))
          tile_image_cache[tile_code] = scaled_image
          self.image = scaled_image

        else:
          print(f"🚨 이미지가 없습니다: tile_code = '{tile_code}'")
          self.image = pygame.Surface((32, 32))
          self.image.fill((255, 0, 0))  # 빨간색으로 에러 표시

    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
class ObstacleObject(pygame.sprite.Sprite):
  def __init__(self, pos, groups, sprite_type, obstacle_code="w", test=False):
    super().__init__(groups)
    from sprites.settings import OBSTACLE_TYPE

    self.sprite_type = sprite_type

    if test:
      # 테스트 모드에서는 색상 기반 surface
      color = OBSTACLE_TYPE.get(obstacle_code, {"color": (150, 150, 150)})["color"]
      self.image = pygame.Surface((32, 32))
      self.image.fill(color)
    else:
      # 실제 이미지 로드
      if obstacle_code in obstacle_image_cache:
        self.image = obstacle_image_cache[obstacle_code]
      else:
        img_path = OBSTACLE_TYPE.get(obstacle_code, {}).get("img", None)
        if img_path and os.path.exists(img_path):
          image = pygame.image.load(img_path).convert_alpha()
          scaled_image = pygame.transform.scale(image, (32, 32))
          obstacle_image_cache[obstacle_code] = scaled_image
          self.image = scaled_image

        else:
          print(f"🚨 이미지가 없습니다: tile_code = '{obstacle_code}'")
          self.image = pygame.Surface((32, 32))
          self.image.fill((255, 0, 0))  # 빨간색으로 에러 표시

    self.rect = self.image.get_rect(topleft=pos)
    self.hitbox = self.rect.inflate(0, -10)
