import pygame
import screen

def main(scence):
  while scence == "main":
    screen.init_display()

    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return "quit"

      if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
        return "battle"

    # 화면 유지용
    font = pygame.font.SysFont(None, 48)
    text = font.render("main", True, (255, 255, 255))
    rect = text.get_rect(center=(screen.cx, screen.cy))
    screen.screen.blit(text, rect)

    screen.update()