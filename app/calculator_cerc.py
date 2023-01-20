class Cerc():
    # ATTRIBUTES
    PI = 3.14

    # CONSTRUCTOR
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # METHODS
    def descriere(self):
        self.lista_descriere = [self.raza,self.culoare]
        return self.lista_descriere

    def aria(self):
        aria_cercului = self.PI * self.raza ** 2
        return aria_cercului

    def diametru(self):
        diam_cerc = 2 * self.raza
        return diam_cerc

    def circumferinta(self):
        circumf_cerc = self.PI * self.diametru()
        return circumf_cerc

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare