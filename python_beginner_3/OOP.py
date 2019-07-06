class Bankkonto:
    
    def __init__(self, nummer, kontostand):
        self.nummer = nummer
        self.kontostand = kontostand
        
    def einzahlen(self, betrag):
        self.kontostand += betrag
        
    def auszahlen(self, betrag):
        self.kontostand -= betrag
        
    def info(self):
        print(self.nummer, "hat kontostand", self.kontostand)
        

mein_konto = Bankkonto("klsdjfljkadjklfkjfdkl", 1000)
mein_konto.einzahlen(10)
mein_konto.info()