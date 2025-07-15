import pygame
import sprites
from setting import screen

enemy_rect = pygame.Rect(300, 300, 32, 32)
speed = 5

obstacle_sprites = pygame.sprite.Group()
visible_sprites = pygame.sprite.Group()

tile = None
trailblazer = None
player_rect = None

done = 0

def ObjectInit():
  global player_rect, trailblazer, tile
  if tile == None:
    tile = sprites.tiles.TileObject((screen.cx, screen.cy), obstacle_sprites, "tile")

  if trailblazer == None:
    trailblazer = sprites.trailblazer.Trailblazer((screen.cx, screen.cy), (visible_sprites), "charactor")
    player_rect = trailblazer.ReturnTheRect()

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

def update(events):
  global done, trailblazer

  if done == 0:
    ObjectInit()
    done = 1

  player_rect = trailblazer.rect

  for event in events:
    if event.type == pygame.QUIT:
      return "exit"

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
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

  # 충돌 체크
  if player_rect.colliderect(enemy_rect):
    print(player_rect)
    print(enemy_rect)
    print("was colliderected")
    return "battle"

  # 화면 그리기
  screen.fill((0, 100, 0))  # 초록색 배경

  #pygame.draw.rect(screen.surface, (0, 0, 255), player_rect) # 플레이어 더미
  pygame.draw.rect(screen.surface, (255, 0, 0), enemy_rect)   # 빨간색 적 나중에 class로 만들 예정
  obstacle_sprites.draw(screen.surface)
  visible_sprites.draw(screen.surface)

  return "main"
