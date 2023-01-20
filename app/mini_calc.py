class MiniCalc:
    # CONSTRUCTOR
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # METHODS
    def adunare(self):
        return self.a + self.b

    def scadere(self):
        return self.a - self.b

    def inmultire(self):
        return self.a * self.b

    def impartire(self):
        return self.a / self.b