import pygame
import screen, start, main_menu, game

pygame.init()
screen.init()

scene = "start_menu"

while True:
  events = pygame.event.get()

  if scene == "start_menu":
    scene = start.update(events)
  elif scene == "main":
    scene = main_menu.update(events)
  elif scene == "battle":
    scene = game.update(events)
  elif scene == "exit":
    screen.exit()

  screen.update()