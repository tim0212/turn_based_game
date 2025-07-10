import pygame
import screen, start, game

pygame.init()
screen.init()

# 초기 상태
scene = "start_menu"

# 매 프레임 루프
while True:
  if scene == "start_menu":
    result = start.start_menu(scene) # exit or start

    if result == "start":
      scene = "main"
  #
  if scene == "main":
    result = game.main(scene) # battle or quit

    if result == "battle":
      scene = "battle"
    elif result == "quit":
      scene = "exit"
  #
  if scene == "battle":
    result = game.battle(scene) # main or quit

    if result == "main":
      scene = "main"
    elif result == "quit":
      scene = "exit"
  #
  if scene == "exit": # exit game
    screen.exit()

  screen.update()