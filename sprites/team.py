import sprites.character_info.character as character
import sprites.character_info.player as player
 
traveler = player.Traveler()
entry = character.Entry()
enemy2 = character.Enemy2()

team_dict = {
  "여행객": traveler,
}

enemy_dict = {
  "앤트리": entry,
  "적2": enemy2,
}

team_info = ["여행객", None, None, None]
enemy_info = ["앤트리", "적2"]

team_group = []
enemy_group = []

def check():
  global team_group, enemy_group

  team_group = [team_dict[name] for name in team_info if name in team_dict]
  enemy_group = [enemy_dict[name] for name in enemy_info if name in enemy_dict]
