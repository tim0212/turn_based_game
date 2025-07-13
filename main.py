import pygame
import screen, start, main_menu, game, setting, help

pygame.init()
screen.init()

scene = "start_menu"

while True:
  events = pygame.event.get()

  if scene == "start_menu":
    scene = start.update(events)
  elif scene == "main":
    scene = main_menu.update(events)
  elif scene == "setting":
    scene = setting.update(events)
  elif scene == "help":
    scene = help.update(events)

  elif scene == "battle":
    scene = game.update(events)

  elif scene == "exit":
    screen.exit()

  screen.update()