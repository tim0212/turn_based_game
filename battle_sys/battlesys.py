import pygame
from setting import math
from setting import screen, text
from sprites import team

# battle진입시 player에게 선공을 준다. star rail과 비슷하게 ATBsys로 사용
# gauge가 100%에 도달시 행동포인트의 변화등을 조절
# AIsys는 따른 파일에 만들어볼 예정

#적 정보를 저장할때 ["name". "name2"]이런 식으로 하고 characters로 넣어버리면 사용 가능

game_sprites = pygame.sprite.Group()

class ATBSys:
  def __init__(self, characters):
    self.characters = characters
    self.key_press = False
    self.gauges = {char: 0 for char in self.characters}
    self.name = [char for char in self.characters]
    self.wait = [] # gauge가 100인 애들 모아두는 곳
    self.anime = False # 캐릭터 턴 진행 완료 표시

  # 게이지 활성화 코드
  def update(self, events):
    event = self.keyevent(events)

    for char in self.characters:
      self.gauges[char] = math.limit(self.gauges[char] + char.speed, 0, 100)
      if self.gauges[char] >= 100 and char not in self.wait:
        self.wait.append(char)

    if self.key_press and self.wait:
      self.key_press = False

      now_running = self.wait.pop(0)
      self.gauges[now_running] = 0
      print(f"now running :{now_running.name}") # 현재 이벤트를 반환하여 애니매이션을 해야하는 객체
      self.anime = False

      return now_running, event, None # 현재 턴과 이 턴에서 눌은 키의 eventkey를 반환 None은 debug용a

    return None, None, None

class BattleDisplay(ATBSys):
  def __init__(self, character, enemy):
    self.character = character
    self.enemy = enemy

    characters = character + enemy
    super().__init__(characters)

  #키 이벤드 "key".upper()문자열로 보내는 코드
  def keyevent(self, events):
    for event in events:
      if event.type == pygame.KEYDOWN and event.key in [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_LSHIFT]:
        print("스킬 입력됨")
        self.key_press = True
        key = pygame.key.name(event.key).upper()

        print(key)
        return key

  # 캐릭터 돌리는 코드
  def running(self, events):
    now_running, event, debug = self.update(events)

    if event == "0":
      now_running.hp -= 20 # hp 깍는 코드
      print("-20")

    # 캐릭터 그리기
    for i, char in enumerate(self.character, start=1):
      pos = team.position_dictP.get(i, (0, 0))
      char.draw(pos)

    for i, char in enumerate(self.enemy, start=1):
      pos = team.position_dictE.get(i, (0, 0))
      char.draw(pos)

    gauge_text = ", ".join([f"{char.name}: {self.gauges[char]}" for char in self.characters])
    now_turn = now_running.name if now_running else ""

    mouse_pos = pygame.mouse.get_pos()
    if event == "LEFT SHIFT":
      text.render(mouse_pos, str(mouse_pos), False, (255, 255, 255), centerpos="midbottom")
      print(mouse_pos)

    text.render((0, 0), gauge_text, False, (255, 255, 255), centerpos="topleft")
    text.render((0, 50), now_turn, False, (255, 255, 255), centerpos="topleft")


    pygame.display.flip()
    screen.clock.tick(screen.fps)

    if now_running and event:
      now_running.anime_update(event)



