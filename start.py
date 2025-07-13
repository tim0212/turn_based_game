import pygame
import screen, text

selected_index = 0
highlight_y = 0  # 강조 박스 y위치 (부드럽게 이동할 대상)

def update(events):
  global selected_index, highlight_y

  # 매 프레임 목표 위치 계산
  target_y = screen.cy + selected_index * 60 - 30

  # 부드럽게 이동 (선형 보간)
  speed = 0.2  # 낮을수록 더 부드럽게
  highlight_y += (target_y - highlight_y) * speed


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
        elif selected_index == 3: return"exit"

  # 텍스트 출력 등 그리기
  screen.fill((20, 20, 50))

  main_rect = pygame.Rect(screen.cx - 150, screen.cy - 100, 300, 350)
  pygame.draw.rect(screen.surface, (255, 255, 255), main_rect, 3)

  for i, option in enumerate(menu_options):
    color = (255, 255, 0) if i == selected_index else (150, 150, 150)
    pos = (screen.cx, screen.cy + i * 60 - 10)

    # 텍스트 렌더링 및 위치 계산만 (화면 출력은 안함)
    rect = text.render(pos, option, True, color, centerpos="center", return_rect_only=True)

    # 사각형 테두리 그리기 (선택된 메뉴만)
    if i == selected_index:
      padding = 10
      bordered_rect = pygame.Rect(
        rect.left - padding,
        highlight_y - rect.height // 2 - padding,
        rect.width + padding * 2,
        rect.height + padding * 2
      )
    pygame.draw.rect(screen.surface, (255, 255, 0), bordered_rect, 3)

    pygame.draw.rect(screen.surface, (255, 255, 0), bordered_rect, 3)  # 두께 3의 노란색 테두리

    text.render((screen.cx, screen.cy / 3), "Turn_based game", True, (255, 255, 255), centerpos="center")

    # 최종 텍스트 출력
    text.render(pos, option, True, color, centerpos="center")

    # target 위치 계산 + 부드럽게 이동
    target_y = screen.cy + selected_index * 60 - 30
    speed = 0.2
    highlight_y += (target_y - highlight_y) * speed

  return "start_menu"