import pygame
import screen

def render(pos : tuple, texts : str, antialiased : bool, color : tuple):
  """_summary_

  Args:
      pos (tuple): _description_ (x, y)
      texts (str): _description_
      antialiased (bool): _description_ 
      color (tuple): _description_ it just use RGB (R, G, B)
  """
  global font, text, rect
  font = pygame.font.SysFont(None, 48)
  text = font.render(texts, antialiased, color)
  rect = text.get_rect(center=(pos))

  screen.screen.blit(text, rect)