from components import Engine, Shield


class CargoShip:
    def __init__(self):
        self.engine = Engine(400)
        self.shield = Shield(100)

    def travel(self):
        return self.engine.activate()