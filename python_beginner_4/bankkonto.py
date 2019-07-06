class Bankkonto:
    
    def __init__(self,  id):
        self.kontostand = 0
        self.id = id
        
    def widthdraw(self, amount):
        self.kontostand -= amount
        
    def pay_in(self, amount):
        self.kontostand += amount
        
    def print_kontostand(self):
        print("Aktueller stand" + str(self.kontostand))
    
meine_bank = Bankkonto("12345")
meine_sparkonto = Bankkonto("12345_sparkonto")
meine_giro = Bankkonto("12345_giro")


meine_bank.widthdraw(100)
