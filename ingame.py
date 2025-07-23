import pygame
import main_scene, main_scene, sprites
from battle_sys.battlesys import BattleDisplay
from setting import screen, text
import sprites.team

result = "battle"
scene = "battle"

team_info = sprites.team

team_info.check()
battle_display = BattleDisplay(team_info.team_group + team_info.enemy_group)
print("디버그 - 캐릭터 목록:", team_info.team_group + team_info.enemy_group)


def update(events):
  global result, scene

  screen.fill((10, 10, 20))

  for event in events:
    if event.type == pygame.QUIT:
      return "exit", result, None
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        scene = "main"
  #========================================battle_sys========================================
  # battle진입시 player에게 선공을 준다. star rail과 비슷하게 ATBsys로 사용 gauge가 100%에 도달시 행동포인트의 변화등을 조절 AIsys는 따른 파일에 만들어볼 예정
  battle_display.running()

  scene = main_scene.handle_battle_result(result)

  return scene, result, None