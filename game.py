# game.py
import pygame
import screen
import text

def update(events):
  for event in events:
    if event.type == pygame.QUIT:
      return "quit"
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return "main"

  screen.fill((10, 10, 20))
  text.render((screen.cx, screen.cy), "BATTLE MODE", True, (255, 100, 100))

  return "battle"
