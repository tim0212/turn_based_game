import pygame
import screen

def main(scene):
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      return "exit"

  # 화면 유지용
  font = pygame.font.SysFont(None, 48)
  text = font.render("main", True, (255, 255, 255))
  rect = text.get_rect(center=(screen.cx, screen.cy))
  screen.screen.blit(text, rect)

  screen.update()
  return scene  # 변경 없음이면 그대로 유지
