import pygame
import start, main_scene, ingame, setting_menu, help
from setting import screen

pygame.init()
screen.init()

scene = "start_menu"

while True:
  events = pygame.event.get()

  if scene == "start_menu":
    scene = start.update(events)
  elif scene == "main":
    scene = main_scene.update(events)
  elif scene == "setting":
    scene = setting_menu.update(events)
  elif scene == "help":
    scene = help.update(events)

  elif scene == "battle":
    scene, result, debug = ingame.update(events)
    if scene == "main":
      ingame.result = "battle"
      ingame.scene = "battle"
      main_scene.done = 0

  elif scene == "exit":
    screen.exit()

  screen.update()