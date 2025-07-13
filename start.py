import pygame
import screen
import text

# 전역 상태
selected_index = 0
highlight_y = screen.cx  # 부드럽게 이동할 y 좌표 나중에 자연스레 만드아

#ㅏㅏㅏㅏㅏㅏㅏ 어려우럽ㄷ저레ㅐ베래ㅔㅐㅓㅔ댛뷷ㅍㅂ ㅓㅍ베ㅐㄷㄿㅂ더ㅜㅐㅍ ㅂㄹㄷ배ㅑㅈ ㅇ펭ㄹ

def update(events):
  global selected_index, highlight_y

  menu_options = ["-> Start Game", "# Settings", "? Help", "X Exit"]

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
        elif selected_index == 3: return "exit"

  # 화면 초기화
  screen.fill((20, 20, 50))

  # 타이틀
  text.render((screen.cx, screen.cy / 3), "Turn_based game", True, (255, 255, 255), centerpos="center")

  # 메뉴 좌표 기준
  base_y = screen.cy
  option_rects = []

  # 메뉴 텍스트 렌더링
  for i, option in enumerate(menu_options):
    color = (255, 255, 0) if i == selected_index else (150, 150, 150)
    pos = (screen.cx, base_y + i * 60 - 30)
    rect = text.render(pos, option, True, color, centerpos="center", return_rect_only=True)
    text.render(pos, option, True, color, centerpos="center")
    option_rects.append(rect)

  # 선택 박스 부드럽게 이동
  target_y = option_rects[selected_index].centery
  speed = 0.2
  highlight_y += (target_y - highlight_y) * speed

  # 노란색 강조 박스
  selected_rect = option_rects[selected_index]
  padding = 10
  bordered_rect = pygame.Rect(
    selected_rect.left - padding,
    highlight_y - selected_rect.height // 2 - padding,
    selected_rect.width + padding * 2,
    selected_rect.height + padding * 2
  )
  pygame.draw.rect(screen.surface, (255, 255, 0), bordered_rect, 3)

  # 전체 메뉴 박스 (흰색 테두리)
  menu_top = option_rects[0].top - 20
  menu_bottom = option_rects[-1].bottom + 20
  menu_height = menu_bottom - menu_top
  menu_width = 300
  menu_rect = pygame.Rect(
    screen.cx - menu_width // 2,
    menu_top,
    menu_width,
    menu_height
  )
  pygame.draw.rect(screen.surface, (255, 255, 255), menu_rect, 3)

  return "start_menu"
