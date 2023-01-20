class Angajat:
    # CONSTRUCTOR
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salar = salariu

    # METHODS
    def descriere(self):
        self.lista_angajat = [self.nume,self.prenume,self.salar]
        return self.lista_angajat

    def nume_complet(self):
        # self.nume_prenume = [self.nume + self.prenume]
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salar

    def salariu_anual(self):
        salar_anual = self.salar * 12
        return salar_anual

    def marire_salariu(self,procente):
        self.salar = int((self.salar * (procente/100)) + self.salar)