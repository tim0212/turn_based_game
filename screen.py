import pygame, sys

# 전역 변수 선언
screen = None
clock = None

# 화면 관련 전역 설정
x = 1250
y = int(x * 9 / 16)
cx = x // 2
cy = y // 2
fps = 60

def init(width=1250, height=None, caption="Turn Game", fps_=60):
  """_summary_

  시작시에 화면 init

  Args:
      width (int, optional): . Defaults to 1250.
      height (_type_, optional): . Defaults to None.
      caption (str, optional): . Defaults to "Turn Game".
      fps_ (int, optional): . Defaults to 60.
  """
  global screen, clock, fps
  if height is None:
      height = int(width * (9 / 16))

  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption(caption)
  clock = pygame.time.Clock()
  fps = fps_

def init_display():
  """scence로 화면을 이동시에 리셋하는 함수"""
  draw_vertical_gradient(screen, (20, 20, 50), (0, 0, 0))

def update():
  """코드 활성화 (flip)"""
  pygame.display.flip()
  clock.tick(fps)

def exit():
    """저장 및 게임 종료"""
    print("save code will input here")
    pygame.quit()
    sys.exit()

def draw_vertical_gradient(surface, top_color, bottom_color):
  """_summary_

  Args:
      surface (_type_): display를 정해야함 ex) >>> screen.screen
      top_color (_type_): 가장 위의 색을 지정 ex) >>> (20, 20, 50)
      bottom_color (_type_): 가장 아래의 색을 지정 ex) >>> (0, 0, 0)

  Examples:
    >>> draw_vertical_gradient(screen.screen, (20, 20, 50), (0, 0, 0))
  """
  height = surface.get_height()
  width = surface.get_width()
  for y in range(height):
    ratio = y / height
    r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
    g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
    b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
    pygame.draw.line(surface, (r, g, b), (0, y), (width, y))
