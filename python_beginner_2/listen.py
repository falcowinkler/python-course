# Listen enthalten Beliebige elemente mit einer festen Reihenfolge.
# Listenelemente haben einen Index (aufsteigend, beginnend bei 0)
# Mit dem wir uns auf sie beziehen können

meine_liste = ["abc", "Stein", "Wasser", 1, 2]

# Zugriff
print(meine_liste[1])

# Veränderung
meine_liste[1] = "Bla blubb"

# Am Ende der Liste anfügen
meine_liste.append("Udo")
print(meine_liste)
# Neues element an Index 2 einsetzen (alle Elemente danach rücken nach rechts)
meine_liste.insert(2, "Neues fancy element")
print(meine_liste)

# Löschen eines elements nach index
del meine_liste[2]
print(meine_liste)
# Löschen eines elementes nach gleichheit
meine_liste.remove("abc")

# Listen können auch aus Funktionen zurückgegeben werden
# Split erzeugt eine Liste von Strings aus einem grossen String anhand eines Trennzeichens
satz = "The brown fox jumps over the lazy dog"
woerter = satz.split(" ")
print(satz.split(" "))

