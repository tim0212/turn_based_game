# main.py
import pygame, sys
from settings import *
from start import start_menu

# from game_core import run_game  # 본편 연결 예정

class Main:
  def __init__(self):
    init() # in settings

  def run(self):
    result = start_menu(self.screen, self.clock)

    if result == "start":
      print("[본게임 진입]")
      # run_game(screen, clock) <- 나중에 게임 본편 함수 호출

if __name__ == "__main__":
    main = Main()
    main.run()