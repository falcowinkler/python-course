# In dieser Übung wiederholt Ihr `while` - Schleifen, den Modulo - Operator `%` und Variablen.
# Aufgabe: Es soll eine gif - Animation mit einer Schleife programmiert werden. 
# Dafür habe ich euch eine Funktion `add_frame(i)` geschrieben. Diese zeigt das `i`-te Frame einer Animation an.
# Ihr sollt eine Animation mit 12 Frames in einer Endlosschleife abspielen. Dafür: 

# - Definiert euch eine Zählervariable i mit Anfangswert 0.
# - Schreibt eine `while` - Schleife, die abbrechen soll, wenn i den Wert 100 erreicht hat. (Bedingung: i ist kleiner 100)
# - In der Schleife sollen zwei Befehle stehen. 
#     - Einmal soll `add_frame()` mit dem richtigen Wert in der Klammer aufgerufen werden. Wir iterieren ja endlos von 0 bis 12 durch die Bilder. Hier können wir den Modulo - Operator verwenden um die Zählvariable `i` (die von 1 bis 1000 läuft) auf 0 bis 12 zu beschränken. 
#     - Die Zählvariable i muss um 1 erhöht werden

# Wenn ihr alles richtig gemacht habt, seht ihr eine Katze, die endlos aus einer Box springt.

# Dieser Befehl gibt euch die funktionen add_frame und start,
# Die ich für euch geschrieben habe um Bilder anzuzeigen.

from show_images import *

## Hier euer code, der add_frame(<gif-sequenznummer>) aufruft

start(repeat=True)
