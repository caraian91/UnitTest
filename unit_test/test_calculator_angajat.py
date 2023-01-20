from app.calculator_angajat import Angajat

class TestAngajat():
    def setup_method(self):
        print('It is executed at the beginning')
        self.angajat = Angajat('Cristi','Tanase',5000)

    def teardown_method(self):
        print('It is executed at the end')

    def test_descriere(self):
        assert self.angajat.descriere() == ['Cristi','Tanase',5000], 'Error, description does not work correctly!'

    def test_nume_complet(self):
        assert self.angajat.nume_complet() == 'Cristi Tanase', 'Error name complet not working or not matching!'

    def test_salar_lunar(self):
        assert self.angajat.salariu_lunar() == 5000, 'Error the monthly salary incorrect'

    def test_salar_anual(self):
        assert self.angajat.salariu_anual() == 60000, 'Error, incorrect annual salary'

    def test_marire_salariu(self):
        # the increase is done in percentages %
        self.angajat.marire_salariu(10)
        # we can check by verify directly the value of the attribute
        assert self.angajat.salar == 5500, 'Error the salary was not increased correctly - attribut'
        # we can check by verify with the method of descriere()
        assert self.angajat.descriere() == ['Cristi','Tanase',5500], 'Error the salary was not increased correctly - description'