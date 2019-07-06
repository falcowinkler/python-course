# Variablen sind ein weiterer wichtiger Bestandteil von Python - Programmen.
# Sie sind Platzhalter.
# Zum Beispiel können sie eine Zeichenkette oder Zahl als Wert enthalten.
# Werte von Variablen können sich mit der Zeit ändern.
# Sie werden mit der Schreibweise
# `platzhaltername = wert` deklariert.
# Variablennamen dürfen Buchstaben, Unterstriche und Zahlen enthalten
# (vobei das erste Zeichen des Variablennamens keine Zahl sein darf).

gruß = "Moin"
name = "World"

print(gruß)   # Aktueller wert ist 'Moin'
print(name)

gruß = "Hallo" # Wert des Platzhalters wird hier verändert

print(gruß) # Jetzt wird 'Hallo' ausgegeben
print(name)

# Variablen kann man genau so gut mit numerischen Literalen belegen
zahl = 42.0
print(zahl)

# Zahlen können auch von Zeichenketten überschrieben werden
zahl = "Dies ist eine Zeichenkette"

print(0.1 + 0.2)
print(zahl)
# Pro-Tipp: Zeichenketten können auch mit dem einfachen Apostroph abgegrenzt werden.
print('Wieder was gelernt')
print('Er sagte "hallo" ')