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
    scene = ingame.update(events)
    if scene == "main":
      main_scene.handle_battle_result(result=ingame.result)

  elif scene == "exit":
    screen.exit()

  screen.update()