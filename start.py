# start.py
import pygame
import screen
import text

selected_index = 0  # ✅ 추가

def update(events):
  global selected_index
  font = pygame.font.SysFont(None, 48)
  menu_options = ["-> Start Game", "X Exit"]

  for event in events:
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      return "exit"
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        selected_index = (selected_index - 1) % len(menu_options)
      elif event.key == pygame.K_DOWN:
        selected_index = (selected_index + 1) % len(menu_options)
      elif event.key == pygame.K_RETURN:
        return "main" if selected_index == 0 else "exit"

  screen.fill((20, 20, 50))
  for i, option in enumerate(menu_options):
    color = (255, 255, 0) if i == selected_index else (150, 150, 150)
    text.render((screen.cx, screen.cy + i * 60), option, True, color)

  return "start_menu"
