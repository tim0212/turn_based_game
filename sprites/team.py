from sprites.character_info import character, player

position_dictP = {
  1 : (160, 250),
  2 : (160, 350),
  3 : (160, 450),
  4 : (160, 550)
}

position_dictE = {
  1 : (1250 - 600, 250),
  2 : (1250 - 600, 350),
  3 : (1250 - 600, 450),
  4 : (1250 - 600, 550)
}


traveler = player.Traveler()
entry = character.Entry()
enemy2 = character.Enemy2()

team_dict = {
  "Traveler": traveler,
}

enemy_dict = {
  "Entry": entry,
  "Enemy2": enemy2,
}

team_info = ["Traveler", None, None, None]
enemy_info = ["Entry", "Enemy2"]

team_group = []
enemy_group = []

def check():
  global team_group, enemy_group

  team_group = [team_dict[name] for name in team_info if name in team_dict]
  enemy_group = [enemy_dict[name] for name in enemy_info if name in enemy_dict]
