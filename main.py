import pygame
import screen, start

pygame.init()
screen.set_screen()

start.start_menu()

# 텍스트 출력 예시
font = pygame.font.SysFont(None, 48)
text = font.render("main", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen.cx, screen.cy))
screen.screen.blit(text, text_rect)

# 매 프레임 루프
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      exit()

    screen.update()