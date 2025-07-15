class CharacterBase:
  def __init__(self, name, hp, atk):
    self.name = name
    self.hp = hp
    self.atk = atk
    self.alive = True

  def take_damage(self, amount):
    self.hp -= amount
    if self.hp <= 0:
      self.alive = False