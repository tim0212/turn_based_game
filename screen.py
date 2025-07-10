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

def set_screen(width=1250, height=None, caption="Turn Game", fps_=60):
    global screen, clock, fps
    if height is None:
        height = int(width * (9 / 16))

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    clock = pygame.time.Clock()
    fps = fps_

def update():
  pygame.display.flip()
  clock.tick(fps)

def exit():
    print("save code will input here")
    pygame.quit()
    sys.exit()