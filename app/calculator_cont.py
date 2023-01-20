class Cont:
    # CONSTRUCTOR
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular = titular_cont
        self.sold = sold

    # METHODS
    def afisare_sold(self):
        return self.iban,self.titular,self.sold

    def debitare_cont(self,suma):
        if self.sold > 0:
            if self.sold >= suma > 0:
                self.sold -= suma
                print(f"Au fost retrasi din contul dvs suma de {suma} lei.Sold disponibil {self.sold} lei")
            elif suma <= 0:
                print("Introduceti un sold de retragere pozitiv sau mai mare ca 0!")
            else:
                print(f"Sold indisponibil! Tranzactie nereusita!")
        else:
            print("Debitati contul cu o suma (mai mare ca 0)")


    def creditare_cont(self,suma):
        self.sold += suma

