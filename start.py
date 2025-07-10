import pygame, sys
import screen

def main(scence):
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      scence = "exit"
      return scence

  screen.update()