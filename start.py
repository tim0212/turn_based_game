import pygame
import screen, text

selected_index = 0


def update(events):
  global selected_index  # 선택된 메뉴 상태 유지

  menu_options = ["-> Start Game", "# Settings", "? Help", "X Exit"]

  for event in events:
    if event.type == pygame.QUIT:
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
    pos = (screen.cx, screen.cy + i * 60 - 30)

    # 텍스트 렌더링 및 위치 계산만 (화면 출력은 안함)
    rect = text.render(pos, option, True, color, centerpos="center", return_rect_only=True)

    # 사각형 테두리 그리기 (선택된 메뉴만)
    if i == selected_index:
      padding = 10
      bordered_rect = pygame.Rect(
        rect.left - padding,
        rect.top - padding,
        rect.width + padding * 2,
        rect.height + padding * 2
      )
      pygame.draw.rect(screen.surface, (255, 255, 0), bordered_rect, 3)  # 두께 3의 노란색 테두리

    text.render((screen.cx, screen.cy / 3), "Turn_based game", True, (255, 255, 255), centerpos="center")

    # 최종 텍스트 출력
    text.render(pos, option, True, color, centerpos="center")

  return "start_menu"