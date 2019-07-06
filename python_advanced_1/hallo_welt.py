print("Hello World")

temperatur = "42.0"
print(float(temperatur) + 10)
print(int("40") + 10)
print(str(10))

leeres_woerterbuch = dict()
leere_list = []
leere_menge = {}
print(leere_menge)

meine_menge = {1, 2, 3, 4, 4}
meine_liste = list(meine_menge)
meine_liste = ["hello", "world", 123, 456]
woerterbuch = dict(meine_liste)
ohne_duplikate = list(set(meine_liste))
mein_tuple = tuple(meine_liste)
mein_tupel = (1, 2, 3, "hello", "world")
print(mein_tupel[3])
meine_liste = list(mein_tupel)
meine_liste[0] = 5
woerterbuch = {"Augsburg": 20, "München": 15}
print(woerterbuch["Augsburg"])




