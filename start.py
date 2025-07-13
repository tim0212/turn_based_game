import pygame
import screen, text

selected_index = 0


def update(events):
  global selected_index  # 선택된 메뉴 상태 유지

  menu_options = ["-> Start Game", "# Settings", "? Help", "X Exit"]

  pygame.draw.rect(screen.surface, (255, 255, 255), (200 + 1 * 60, 200 + 4 * 60))

  for event in events:
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      return "exit"
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        selected_index = (selected_index - 1) % len(menu_options)
      elif event.key == pygame.K_DOWN:
        selected_index = (selected_index + 1) % len(menu_options)
      elif event.key == pygame.K_RETURN:
        if selected_index == 0: return "main"
        elif selected_index == 1: return "setting"
        elif selected_index == 2: return "help"
        else: "exit"

  # 텍스트 출력 등 그리기
  screen.fill((20, 20, 50))
  for i, option in enumerate(menu_options):
    color = (255, 255, 0) if i == selected_index else (150, 150, 150)
    text.render((screen.cx, 200 + i * 60), option, True, color, centerpos="centertop")

  return "start_menu"
