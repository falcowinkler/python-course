



def increment(meine_zahl):
    meine_zahl += 1

print(increment(20))



def increment_liste(liste):
    for i, e in enumerate(liste):
        liste[i] += 1

meine_liste = [1, 2, 3]     
increment_liste(meine_liste)
print(meine_liste)

test_test = 2
increment(test_test)
print(test_test)

