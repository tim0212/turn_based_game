import pygame
import screen, text

def main(scence):
  screen.init_display()
  while scence == "main":

    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return "quit"

      if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
        return "battle"

    # 화면 유지용
    text.render((screen.cx, screen.cy), "main", True, (255, 255, 255))

    screen.update()