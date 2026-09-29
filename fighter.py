from components import Engine, Shield


class Fighter:
    def __init__(self):
        self.engine = Engine(900)
        self.shield = Shield(70)

    def fly(self):
        return self.engine.activate()