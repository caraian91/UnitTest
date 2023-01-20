class Dreptunghi:
    # CONSTRUCTOR
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # METHODS
    def descriere(self):
        self_lista_descriere = [self.lungime,self.latime,self.culoare]
        return self_lista_descriere

    def aria(self):
        aria_dreptunghi = self.lungime * self.latime
        return aria_dreptunghi

    def perimetrul(self):
        peri_dreptunghi = 2 * (self.lungime + self.latime)
        return peri_dreptunghi

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

