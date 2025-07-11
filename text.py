import pygame
import screen

def render(pos: tuple, texts: str, antialiased: bool, color: tuple, display_update=False, centerpos: str = "center"):
  """
  텍스트를 화면에 출력하는 함수

  Args:
      pos (tuple): 위치 좌표 (x, y)
      texts (str): 출력할 문자열
      antialiased (bool): 안티앨리어싱 적용 여부
      color (tuple): 텍스트 색상 (R, G, B)
      display_update (bool): True면 화면을 배경색으로 초기화
      centerpos (str): 'center', 'topleft', 'midtop' 등 텍스트 정렬 위치
  """
  font = pygame.font.SysFont(None, 48)
  text = font.render(texts, antialiased, color)
  rect = text.get_rect()

  # 정렬 방식 적용
  if hasattr(rect, centerpos):
    setattr(rect, centerpos, pos)
  else:
    rect.center = pos  # 기본값 fallback

  if display_update:
    screen.fill((20, 20, 50))  # 사용자 정의 fill 함수 사용

  screen.screen.blit(text, rect)
