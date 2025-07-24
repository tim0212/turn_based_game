import pygame
from setting import screen, text
from sprites.character_info.character import *
from sprites.character_info.player import *

# battle진입시 player에게 선공을 준다. star rail과 비슷하게 ATBsys로 사용
# gauge가 100%에 도달시 행동포인트의 변화등을 조절
# AIsys는 따른 파일에 만들어볼 예정

#적 정보를 저장할때 ["name". "name2"]이런 식으로 하고 character로 넣어버리면 사용 가능

def limte(val, min_val: int, max_val: int):
  return max(min_val, min(val, max_val))

class ATBSys:
  def __init__(self, characters):
    self.characters = characters
    self.key_press = False
    self.gauges = {char: 0 for char in self.characters}
    self.wait = []

  def update(self):
    for char in self.characters:
      self.gauges[char] = limte(self.gauges[char] + char.speed, 0, 100)
      if self.gauges[char] >= 100 and char not in self.wait:
        self.wait.append(char)  # char 객체를 넣어야 함

    if self.key_press and self.wait:
      self.key_press = False
      now_turn = self.wait.pop(0)
      self.gauges[now_turn] = 0
      print(f"{now_turn.name}의 턴입니다!")

class BattleDisplay(ATBSys):
  def __init__(self, characters):
    super().__init__(characters)

  def keyevent(self, events):
    for event in events:
      if event.type == pygame.KEYDOWN: 
        if event.key in [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r]:
          print("스킬 입력됨")
          self.key_press = True

  def running(self, event):
    self.keyevent(event)

    self.update()
    gauge_text = "\n".join([f"{char.name}: {self.gauges[char]}" for char in self.characters])
    text.render((0, 0), gauge_text, False, (255, 255, 255), centerpos="topleft")
    pygame.display.flip()
    screen.clock.tick(screen.fps)
