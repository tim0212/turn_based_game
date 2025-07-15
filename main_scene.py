import pygame
import screen, object

player_rect = pygame.Rect(screen.cx, screen.cy, 32, 32)
enemy_rect = pygame.Rect(300, 300, 32, 32)
speed = 5

obstacle_sprites = pygame.sprite.Group()

def knockback_from_enemy(player_rect, enemy_rect, distance=5):
  if player_rect.centerx < enemy_rect.centerx:
    player_rect.x -= (enemy_rect.width + distance)
  else:
    player_rect.x += (enemy_rect.width + distance)

  if player_rect.centery < enemy_rect.centery:
    player_rect.y -= (enemy_rect.height + distance)
  else:
    player_rect.y += (enemy_rect.height + distance)

def update(events):

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
    return "battle"

  # 화면 그리기
  screen.fill((0, 100, 0))  # 초록색 배경

  #pygame.draw.rect(screen.surface, (0, 0, 255), player_rect)  # 파란색 플레이어 나중에 캐릭터로 변환해야함
  object.tiles.TileObject((0, 0), obstacle_sprites, "tile", screen.surface, player_rect)
  pygame.draw.rect(screen.surface, (255, 0, 0), enemy_rect)   # 빨간색 적 나중에 class로 만들 예정

  return "main"
