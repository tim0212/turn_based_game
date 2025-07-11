import pygame
import screen

def battle(scence):
  while scence == "battle":
    screen.init_display()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return "quit"

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          return "main"

    # 예시: 전투 텍스트
    font = pygame.font.SysFont(None, 48)
    text = font.render("BATTLE MODE", True, (255, 100, 100)) #⚔️
    rect = text.get_rect(center=(screen.cx, screen.cy))
    screen.screen.fill((10, 10, 20))
    screen.screen.blit(text, rect)

    screen.update()
