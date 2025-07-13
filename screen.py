import pygame, sys
import time

# 전역 변수 선언
clock = None

# 화면 관련 전역 설정
x = 1250
y = int(x * 9 / 16)
cx = x // 2
cy = y // 2
fps = 60

def init(width=1250, height=None, caption="Turn Game", fps_=60):
  global start_time
  start_time = time.time()
  """_summary_

  시작시에 화면 init

  Args:
      width (int, optional): . Defaults to 1250.
      height (_type_, optional): . Defaults to None.
      caption (str, optional): . Defaults to "Turn Game".
      fps_ (int, optional): . Defaults to 60.
  """
  global surface, clock, fps
  if height is None:
      height = int(width * (9 / 16))

  surface = pygame.display.set_mode((width, height))
  pygame.display.set_caption(caption)
  clock = pygame.time.Clock()
  fps = fps_

def update():
  """코드 활성화 (flip)"""
  pygame.display.flip()
  clock.tick(fps)

def exit():
    """저장 및 게임 종료"""
    print("save code will input here")
    end_time = time.time()
    running_time = start_time - end_time
    print("게임이 돌아간 시간 : {} ========================".format(running_time))
    pygame.quit()
    sys.exit()

def fill(top_color : tuple = (255, 255, 255), bottom_color : tuple = (0, 0, 0), fill : tuple = None):
  """_summary_

  단색은 fill = (0, 0, 0)식으로 적어라
  그라데이션은 top and bottom_color을 =로 사용

  Args:
      top_color (_type_): 가장 위의 색을 지정 ex) >>> (20, 20, 50)(남색)
      bottom_color (_type_): 가장 아래의 색을 지정 ex) >>> (0, 0, 0)(검은색)
      fill (bool): fill을 사용하고 싶으면 사용 ex) (0, 0, 0)(검은색)

  Examples:
    >>> draw_vertical_gradient(screen.screen, (20, 20, 50), (0, 0, 0))
    >>> screen.fill(fill = True, rgb = (0, 0, 0))
  """

  try:
    surface.fill(fill)
  except:
    height = surface.get_height()
    width = surface.get_width()
    for y in range(height):
      ratio = y / height
      r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
      g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
      b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
      pygame.draw.line(surface, (r, g, b), (0, y), (width, y))