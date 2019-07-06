test_string = "Ich bin hier, Du bist hier, Schnabeltier.".title()

# Title wandelt alle Anfangsbuchstaben in Großbuchstaben
# Mit replace könnt ihr suchen und ersetzen
test_string = test_string.title().replace(",", ";")

print(test_string)
# Anzahl an Zeichen im String
print(len(test_string))
# Vorkommen eines Wortes zählen
print(test_string.count("Schnabeltier"))

lange_zeichenkette = "The brown fox jumps over the lazy dog. The brown fox jumps over the lazy dog."
print(len(lange_zeichenkette))
print(lange_zeichenkette.count("fox"))

# An welcher stelle steht ein Teil-String in der Zeichenkette?
print("abc123".find("c"))