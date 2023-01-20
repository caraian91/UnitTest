from app.calculator_cerc import Cerc

class TestCerc():
    def setup_method(self):
        print('It is executed at the beginning')
        self.cerc = Cerc(3, 'black')

    def teardown_method(self):
        print('It is executed at the end')

    def test_descriere(self):
        assert self.cerc.descriere() == [3, 'black'], 'Error, description does not work correctly!'

    def test_aria(self):
        assert self.cerc.aria() == 28.26, 'Error, area does not work correctly!'

    def test_diametru(self):
        assert self.cerc.diametru() == 6, 'Error, diameter does not work correctly!'

    def test_circumferita(self):
        assert self.cerc.circumferinta() == 18.84, 'Error, circumference does not work correctly!'

    def test_schimba_culoare(self):
        self.cerc.schimba_culoarea('red')
        assert self.cerc.culoare == 'red', 'Error, color has not change - attrribut value'