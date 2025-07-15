import pygame
import screen, start, main_scene, game, setting, help

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
    scene = setting.update(events)
  elif scene == "help":
    scene = help.update(events)

  elif scene == "battle":
    scene = game.update(events)
    if scene == "main":
      main_scene.knockback_from_enemy(main_scene.player_rect, main_scene.enemy_rect, distance=5)

  elif scene == "exit":
    screen.exit()

  screen.update()