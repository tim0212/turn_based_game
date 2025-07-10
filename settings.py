import pygame

x, y = 1250, 1250 * (9 / 16)

def init():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    clock = pygame.time.Clock()