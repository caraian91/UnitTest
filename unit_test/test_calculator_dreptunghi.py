from app.calculator_dreptunghi import Dreptunghi

class TestDrepunghi:

    def setup_method(self):
        print('It is executed at the beginning')
        self.dreptunghi = Dreptunghi(3, 2, 'pink')
        self.culoare_noua = [3, 2, 'blue']

    def teardown_method(self):
        print('It is executed at the end')

    def test_descriere(self):
        assert self.dreptunghi.descriere() == [3, 2, 'pink'], 'Error, description does not work correctly!'

    def test_aria(self):
        assert self.dreptunghi.aria() == 6, 'Error, area does not work correctly!'

    def test_perimetru(self):
        assert self.dreptunghi.perimetrul() == 10, 'Error, perimeter does not work correctly!'

    def test_schimba_culoare(self):
        self.dreptunghi.schimba_culoarea('blue')
        # we can check by verify directly the value of the attribute
        assert self.dreptunghi.culoare == 'blue', 'Error, color has not change - attrribut value'
        # we can check by verify with the method of descriere()
        assert self.dreptunghi.descriere() == [3, 2, 'blue'], 'Error, the color has not changed'