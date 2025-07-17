import pygame, os
import sprites.character
import sprites, sprites.trailblazer, sprites.object, sprites.character
from setting import screen

speed = 2

obstacle_sprites = pygame.sprite.Group()
tile_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()

tile = None
player_rect = None
player = None
enemy_rect = None

tile_image_cache = sprites.object.tile_image_cache

done = 0

def create_map():
  global player, enemy

  from sprites.settings import WORLD_MAP, tile_size, TILE_TYPES

  for row_index, row in enumerate(WORLD_MAP):
    for col_index, cell in enumerate(row):
      x = col_index * tile_size
      y = row_index * tile_size
      pos = (x, y)

      items = cell if isinstance(cell, list) else [cell]

      for item in items:
        if item in ["x", "r"]:
          sprites.object.TileObject(pos, tile_sprites, "tile", item)
        if item in ["w"]:
          sprites.object.ObstacleObject(pos, tile_sprites, "obstacle", item)

        if item == "p":
          player = sprites.trailblazer.Trailblazer(pos, character_sprites, "charactor")

        if item == ["e"]:
          enemy = sprites.character.Entry(pos, character_sprites, "enemy")

def knockback_from_enemy(player_rect, enemy_rect, distance=5):
  if player_rect.centerx < enemy_rect.centerx:
    player_rect.x -= (enemy_rect.width + distance)
  else:
    player_rect.x += (enemy_rect.width + distance)

  if player_rect.centery < enemy_rect.centery:
    player_rect.y -= (enemy_rect.height + distance)
  else:
    player_rect.y += (enemy_rect.height + distance)
  return "main"

def ObjectInit():
  create_map()

def update(events):
  global done, player_rect

  if done == 0:
    ObjectInit()

    done = 1

  enemy_rect = enemy.rect
  player_rect = player.rect

  for event in events:
    if event.type == pygame.QUIT:
      return "exit"
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      return "start_menu"

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player_rect.x -= speed
  if keys[pygame.K_RIGHT]:
    player_rect.x += speed
  if keys[pygame.K_UP]:
    player_rect.y -= speed
  if keys[pygame.K_DOWN]:
    player_rect.y += speed

  if player_rect.colliderect(enemy_rect):
    return "battle"

  screen.fill((0, 0, 0))
  tile_sprites.draw(screen.surface)
  obstacle_sprites.draw(screen.surface)
  character_sprites.draw(screen.surface)

  return "main"

