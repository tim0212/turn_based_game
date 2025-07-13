class Charactor:
    def __init__(self, name, max_hp, atk):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0
