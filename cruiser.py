from components import Engine, Weapon


class Cruiser:
    def __init__(self):
        self.engine = Engine(600)
        self.weapon = Weapon(200)

    def attack(self):
        return self.weapon.fire()