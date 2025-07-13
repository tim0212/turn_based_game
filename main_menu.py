# main_menu.py
import pygame
import screen
import text

def update(events):
  for event in events:
    if event.type == pygame.QUIT:
      return "quit"

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return "start_menu"
      if event.key == pygame.K_1:
        return "battle"

  screen.fill((20, 20, 50))
  text.render((screen.cx, screen.cy), "main", True, (255, 255, 255))

  return "main"