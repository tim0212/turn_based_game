import pygame
import screen, start, game

pygame.init()
screen.set_screen()

# 텍스트 출력 예시
font = pygame.font.SysFont(None, 48)
text = font.render("main", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen.cx, screen.cy))
screen.screen.blit(text, text_rect)

# 초기 상태
scene = "start_menu"

# 매 프레임 루프
while True:
  if scene == "start_menu":
    result = start.start_menu(scene)
    if result == "start":
      scene = "main"

  if scene == "main":
    game.main(scene)

  if scene == "exit":
    screen.exit()

  screen.update()