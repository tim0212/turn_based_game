import pygame, os
import sprites, sprites.character_info.player, sprites.object, sprites.character_info.character
from setting import screen

speed = 5

obstacle_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()

tile = None
player_rect = None
player = None
enemy_rect = None

tile_image_cache = sprites.object.tile_image_cache

done = 0
a = 0

def create_map():
  global player, enemy, checkpoint_position

  from sprites.settings import WORLD_MAP, tile_size

  for row_index, row in enumerate(WORLD_MAP):
    for col_index, cell in enumerate(row):
      x = col_index * tile_size
      y = row_index * tile_size
      pos = (x, y)

      items = cell if isinstance(cell, list) else [cell]

      for item in items:
        if item in ["x", "r"]:
          sprites.object.TileObject(pos, tile_sprites, "tile", item)
        elif item in ["w"]:
          sprites.object.ObstacleObject(pos, obstacle_sprites, "obstacle", item)

        elif item == "p":
          player = sprites.character_info.player.DummyTraveler(pos, character_sprites, "charactor")
          checkpoint_position = pos

        elif item == "e":
          enemy = sprites.character_info.character.DummyEntry(pos, character_sprites, "enemy")

def knockback_from_enemy(player_rect, enemy_rect, distance=10):
  original = player_rect.copy()
  if player_rect.centerx < enemy_rect.centerx:
    player_rect.x -= (enemy_rect.width + distance)
  else:
    player_rect.x += (enemy_rect.width + distance)

  if player_rect.centery < enemy_rect.centery:
    player_rect.y -= (enemy_rect.height + distance)
  else:
    player_rect.y += (enemy_rect.height + distance)

  if pygame.sprite.spritecollide(player, obstacle_sprites, False):
    player_rect = original

def handle_battle_result(result):
  if result in ["lose", "run"]:
    player.rect.topleft = checkpoint_position
    print(player_rect)
    return "main"
  elif result == "win":
    print(player_rect)
    knockback_from_enemy(player.rect, enemy.rect, distance=5)
    print(player_rect)
    return "main"
  else:
    return "battle"

def ObjectInit():
  global camera, a
  from camera import Camera

  if a == 0:
    create_map()
    a = 1
  camera = Camera(player.rect, screen.surface.get_size())

def update(events):
  global done, player_rect

  if done == 0:
    ObjectInit()

    done = 1

  enemy_rect = enemy.rect

  for event in events:
    if event.type == pygame.QUIT:
      return "exit"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      return "start_menu"


  keys = pygame.key.get_pressed()
  original_x = player.rect.x

  if keys[pygame.K_LEFT]:
    player.rect.x -= speed
  if keys[pygame.K_RIGHT]:
    player.rect.x += speed

  if pygame.sprite.spritecollide(player, obstacle_sprites, False):
    player.rect.x = original_x

  original_y = player.rect.y

  if keys[pygame.K_UP]:
    player.rect.y -= speed
  if keys[pygame.K_DOWN]:
    player.rect.y += speed

  if pygame.sprite.spritecollide(player, obstacle_sprites, False):
    player.rect.y = original_y

  if player.rect.colliderect(enemy_rect):
    return "battle"

  camera.update()
  screen.fill((0, 0, 0))
  camera.draw_group(screen.surface, tile_sprites)
  camera.draw_group(screen.surface, obstacle_sprites)
  camera.draw_group(screen.surface, character_sprites)

  return "main"

