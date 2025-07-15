import pygame
from setting import screen, text

def update(events):
  for event in events:
    if event.type == pygame.QUIT:
      return "exit"
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return "start_menu"

  screen.fill((10, 10, 20))
  text.render((screen.cx, screen.cy), "setting", True, (255, 100, 100))

  return "setting"