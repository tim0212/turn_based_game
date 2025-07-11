import pygame
import screen

def render(pos : tuple, texts : str, antialiased : bool, color : tuple, display_update = False, centerpos : str="center"):
  """_summary_

  Args:
      pos (tuple): _description_ 위치 ex) (x, y)
      centerpos (str): _description_ pos가 나타나는 값 ex) center, topleft .ect

      texts (str): _description_
      antialiased (bool): _description_ 부드럽게 만들어 주는 값 ex) True r False
      color (tuple): _description_ RGB로 씀 ex) (0, 0, 0)(검은색)
      display_update (bool): _description_ 화면 뒷배경 칠하기. reset용도 ex) display_update=True
  """
  global font, text, rect
  font = pygame.font.SysFont(None, 48)
  text = font.render(texts, antialiased, color)
  rect = text.get_rect(centerpos = (pos))

  if display_update == True:
    screen.fill((20, 20, 50), (0, 0, 0))

  screen.screen.blit(text, rect)