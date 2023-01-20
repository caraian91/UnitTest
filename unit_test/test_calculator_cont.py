from app.calculator_cont import Cont

class TestCont():
    def setup_method(self):
        print('It is executed at the beginning')
        self.cont = Cont('ROBRD123K02','Andrei',500)

    def teardown_method(self):
        print('It is executed at the end')

    def test_afisare_sold(self):
        assert self.cont.afisare_sold() == ('ROBRD123K02','Andrei',500) , 'Error, balance display is wrong!'

    def test_debitare_cont(self):
        # we withdraw 100 lei from the account
        self.cont.debitare_cont(100)
        assert self.cont.sold == 400 , 'Error wrong debit from the account!'

    def test_creditare_cont(self):
        # we call the function to know how much was debited
        self.test_debitare_cont()
        # we charge the account with the amount of 200 lei
        self.cont.creditare_cont(200)
        assert self.cont.sold == 600, 'Error your account has not been funded'