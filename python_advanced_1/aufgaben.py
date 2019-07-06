n = 17

def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
            
class Container:
    
    def __init__(self, h, b, l):
        self.hoehe = h
        self.laenge = l
        self.breite = b
    
    def volumen(self):
        return self.hoehe * self.laenge * self.breite
    
mein_container = Container(10,20,30)
print(mein_container.volumen())

geheim = "schnabeltier"
guesses = []
tries = 0

while tries < 10:
    user_input = input("Bitte einen buchstaben raten: ")
    guesses.append(user_input)
    for buchstabe in geheim:
        if buchstabe in guesses:
            print(buchstabe, end="")
        else:
            print("_", end="")
    print()
    tries += 1

guess = input("Jetzt das wort raten: ")
if guess == geheim:
    print("gewonnen")