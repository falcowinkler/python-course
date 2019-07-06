def increment(number):
    number += 1

meine_zahl = 1
increment(meine_zahl)
print(meine_zahl)

def increment_list(list_of_nums):
    for i in range(len(list_of_nums)):
        list_of_nums[i] += 1

meine_zahlen_liste = [1, 2, 3, 6, 27, 42, 3]
increment_list(meine_zahlen_liste)
print(meine_zahlen_liste)