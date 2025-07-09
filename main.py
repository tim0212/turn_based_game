# main.py
import pygame
import sys
from start import start_menu

# from game_core import run_game  # 본편 연결 예정

def main():
    pygame.init()
    screen = pygame.display.set_mode((1250, 1250 * (9 / 16)))
    clock = pygame.time.Clock()

    result = start_menu(screen, clock)
    if result == "start":
        print("[본게임 진입]")
        # run_game(screen, clock) <- 나중에 게임 본편 함수 호출

if __name__ == "__main__":
    main()
