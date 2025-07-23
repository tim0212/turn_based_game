import pygame
from setting import screen, text
from sprites.character_info.character import *
from sprites.character_info.player import *

# battle진입시 player에게 선공을 준다. star rail과 비슷하게 ATBsys로 사용
# gauge가 100%에 도달시 행동포인트의 변화등을 조절
# AIsys는 따른 파일에 만들어볼 예정

#적 정보를 저장할때 ["name". "name2"]이런 식으로 하고 character로 넣어버리면 사용 가능

class ATBSys:
  def __init__(self, characters):
    self.characters = characters

    self.gauges = {char: 0 for char in self.characters}

  def update(self):
    for char in self.characters:
      self.gauges[char] += char.speed
      if self.gauges[char] >= 100:
        self.gauges[char] = 0
        print(f"{char.name}의 턴입니다!")

class BattleDisplay(ATBSys):
  def __init__(self, characters):
    super().__init__(characters)

  def keyevent(event):
    if event.key == pygame.K_q:
      print("1번 스킬")

    if event.key == pygame.K_w:
      print("2번 스킬")

    if event.key == pygame.K_e:
      print("궁")

    if event.key == pygame.K_r:
      print("특수능력?")

  def running(self):
    self.update()

    gauge_text = "\n".join([f"{char.name}: {self.gauges[char]}" for char in self.characters])

    text.render((0, 0), gauge_text, False, (255, 255, 255), centerpos="topleft")

    pygame.display.flip()
    screen.clock.tick(screen.fps)
