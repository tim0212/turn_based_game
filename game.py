import pygame
import screen, text

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
    screen.screen.fill((10, 10, 20))
    text.render((screen.cx, screen.cy), "BATTLE MODE", True, (255, 100, 100))

    screen.update()