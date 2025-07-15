# game.py
import pygame
import screen, text
from sprites.character import Charactor

# 캐릭터 생성
player = Charactor("Hero", 100, 20)
enemy = Charactor("Slime", 80, 10)
turn = "player"
action_log = ""

def update(events):
  global turn, action_log

  for event in events:
    if event.type == pygame.QUIT:
      return "exit"
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return "main"

      # 턴: 플레이어가 키 입력해야만 행동함
      if turn == "player":
        if event.key == pygame.K_a:  # A키로 공격
          enemy.hp -= player.atk
          action_log = f"{player.name}가 공격! {enemy.name}의 HP -{player.atk}"
          turn = "enemy"

  # 적 행동 자동 실행
  if turn == "enemy":
    player.hp -= enemy.atk
    action_log = f"{enemy.name}가 반격! {player.name}의 HP -{enemy.atk}"
    turn = "player"

  # 화면 표시
  screen.fill((10, 10, 30))
  text.render((screen.cx, screen.cy / 2 - 50), f"{player.name} HP: {player.hp}", True, (255, 255, 255))
  text.render((screen.cx, screen.cy / 2), f"{enemy.name} HP: {enemy.hp}", True, (255, 100, 100))
  text.render((screen.cx, screen.cy / 2 + 100), action_log, True, (255, 255, 0))

  return "battle"