import pygame
from setting import screen, text

result = "exit"

def update(events):
  global result
  for event in events:
    if event.type == pygame.QUIT:
      return "exit"
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return "main"
  #========================================battle_sys========================================
  # battle진입시 player에게 선공을 준다. star rail과 비슷하게 ATBsys로 사용 gauge가 100%에 도달시 행동포인트의 변화등을 조절 AIsys는 따른 파일에 만들어볼 예정

  




  screen.fill((10, 10, 20))

  return "battle"