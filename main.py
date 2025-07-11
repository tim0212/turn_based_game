"""
git add .
git commit -m "set"
git push
"""
import pygame
import screen, start, game, main_menu

pygame.init()
screen.init()

# 초기 상태
scene = "start_menu"

# 매 프레임 루프
while True:
  if scene == "start_menu":
    result = start.start_menu(scene) # quit or start

    if result == "start":
      scene = "main"
  #
  if scene == "main":
    result = main_menu.main(scene) # battle or quit

    if result == "battle":
      scene = "battle"
    elif result == "quit":
      scene = "exit"
  #
  if scene == "battle":
    result = game.battle(scene) # main

    if result == "main":
      scene = "main"
    elif result == "quit":
      scene = "exit"
  #
  if scene == "exit": # exit game
    screen.exit()

  screen.update()