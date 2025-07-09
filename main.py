import pygame, sys

def start_init():
    global screen, clock, caption

    pygame.display.init()
    pygame.font.init()

    try:
      pygame.mixer.init()
      pygame.mixer.music.load("sound\Coin 1.mp3")
      pygame.mixer.music.play()
    except:
      print("사운드 로드 실패")

    screen = pygame.display.set_mode((1250, 1250 * (9 / 16)))
    clock = pygame.time.Clock()
    caption = pygame.display.set_caption("turn_game")

start_init()

key_actions = {
    pygame.K_0: lambda: print("0번 키 눌림"),
    pygame.K_1: lambda: print("1번 키 눌림"),
    pygame.K_2: lambda: print("2번 키 눌림"),
}

def keyboard_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit((lambda d: print(d))("was exited code by safty, later this will be made to save function"))

        if event.type == pygame.KEYDOWN:
            action = key_actions.get(event.key)
            if action:
                action()

while True:
    keyboard_event()

    pygame.display.flip()

    screen.fill((30, 30, 30))
    clock.tick(60)
