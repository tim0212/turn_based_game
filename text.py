import pygame
import screen

def render(pos : tuple, texts : str, antialiased : bool, color : tuple):
  """_summary_

  Args:
      pos (tuple): _description_ (x, y)
      texts (str): _description_
      antialiased (bool): _description_ 부드럽게 만들어
      \n **픽셀의 "계단현상"**을 줄여주는 기술

        UI 텍스트나 제목, 메뉴에는 True 권장_
      \n
        매우 빈번하게 갱신되는 텍스트
      \n(ex. 숫자 카운터 등)는 False 써도 무방

      (White) (255, 255, 255) (Black)	(0, 0, 0) (Gray)	(128, 128, 128) (Red)	(255, 0, 0) (Green)	(0, 255, 0) (Blue)(0, 0, 255) (Yellow)	(255, 255, 0) (Cyan)	(0, 255, 255) (Magenta)	(255, 0, 255) (Brown)	(139, 69, 19) (Orange)	(255, 165, 0)(Lime)	(50, 205, 50) (Navy)	(0, 0, 128) (Purple)	(128, 0, 128) (Silver)	(192, 192, 192) (Gold)	(255, 215, 0)(Pink)	(255, 192, 203) (Peach)	(255, 218, 185) (SkyBlue)	(135, 206, 235) (Light Gray)	(211, 211, 211)
  """
  global font, text, rect
  font = pygame.font.SysFont(None, 48)
  text = font.render(texts, antialiased, color)
  rect = text.get_rect(center=(pos))

  screen.screen.blit(text, rect)