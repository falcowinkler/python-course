# Zahlen und Zeichenketten im Program zu haben ist ja schön und gut,
# aber was können wir damit anstellen?
# Mit Zahlen können wir rechnen, in der üblichen Schreibweise

# Hier ist es sehr Hilfreich mit dem Debugger von Thonny zu arbeiten.
# Mit "Step into" (zweiter Pfeil neben dem Käfer)
# könnt ihr euch ganz genau ansehen, wie die einzelnen Befehle ausgewertet werden.

x = 10
y = 20

print(x + y)

z = x + y

print(z + 2)      # Addition
print(2 * 2)      # Multiplikation 
print(5 - 2)      # Differenz
print(12 / 4)     # Division
print(12 // 4)    # Division und Abrunden
print(13 % 5)     # Modulo, mehr dazu im Kurs oder unter
                  # https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
print(4 ** 4)     # Potenz
print(0.1 + 0.2)  # Was passiert hier? Computer können Kommazahlen nur mit begrenzter
                  # Genauigkeit darstellen. Siehe http://0.30000000000000004.com

print(10 * (20 + 5)) # Ausdrücke können beliebig geklammert werden


# Eine gute Übung ist hier den obigen Code Zeile für Zeile durchzugehen und die Ausgabe zu verstehen. 
# Spielt auch mal mit den Zahlen herum und schaut, wie sich die Ausgabe verändert!

# Zeichenketten unterstützen übrigens auch die Operationen `*` und `+`.
# `*` Wiederholt eine Zeichenkette x-mal und `+` verkettet Zeichenketten.

name = "Jürgen"
print("moin " * 5 + name)

name = "Jürgen"
print("moin " + name)

# Funktioniert das `+` auch mit Zahlen und zeichenketten?
# Probiert das mal aus:

zahl = 42
zeichenkette="72"

print(zahl + int(zeichenkette))

print(zahl + int(zeichenkette))

print(str(zahl) + " " + zeichenkette)

# Was könnten gründe für das Ergebnis sein?