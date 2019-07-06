# Ampelschaltung: Die variable `farbe` bekommt eine bestimmte Farbe als anfangswert
farbe = 'grün'
i = 0

# Um die jeweils nächste Farbe in der Ampel-Sequenz zu bekommen prüfen wir den aktuellen Wert der Variable
# Und weisen ihr den entsprechenden nächsten wert zu.
# Das ganze lässt sich natürlich prima in einer Schleife wiederholen
while i < 10:
    i += 1
    if farbe == 'grün':
        farbe = 'gelb'
    elif farbe == 'gelb':
        farbe = 'rot'
    else:
        farbe = 'grün'
    print(farbe)

# Für bestimmte Altersbereiche das passende Getränk ausgeben
# Man beachte dass nur jeweis eine Bedingung pro Altersbereich ausreicht,
# Da durch das zusammenhängende if-elif-else Konstrukt vorherige Bedingungen ausschließen
alter = 10
while alter < 25:
    alter += 1
    if alter < 14:
        print("Orangensaft")
    elif alter < 18:
        print("Cola")
    elif alter < 21:
        print("Bier")
    else:
        print("Whiskey")
