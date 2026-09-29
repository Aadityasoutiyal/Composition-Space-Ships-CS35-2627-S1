class Engine:
    def __init__(self, speed):
        self.speed = speed

    def activate(self):
        return self.speed


class Shield:
    def __init__(self, strength):
        self.strength = strength

    def activate(self):
        return self.strength


class Weapon:
    def __init__(self, power):
        self.power = power

    def fire(self):
        return self.power