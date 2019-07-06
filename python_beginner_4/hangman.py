secret_word = "schnabeltier"

user_input = None
guesses = []
tries = 0
print(eval("tries < 10"))
while tries < 10:
    user_input = input("Rate einen Buchstaben: ")
    guesses.append(user_input)
    for character in secret_word:
        if character in guesses:
            print(character, end="")
        else:
            print("_", end="")
    print()
    tries += 1
    
print()
print("Alle Rateversuche aufgebraucht.")
guessed = input("Rate jetzt das wort: ")
if guessed == secret_word:
    print("gewonnen!")
else:
    print("falsch")
    