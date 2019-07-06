my_numbers = {1, 2, 3, 4, 5, 5, 6, 6}
print(my_numbers)


meine_userids = [123, 123, 1234]
print(list(set(meine_userids)))

A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B))

meine_zahlen = (1, 2, 3, 4, "test")
meine_zahlen[2] = "verändern"

def zwei_rueckgabewerte(parameter):
    return 2 * parameter, "Hallo"

eins, zwei = zwei_rueckgabewerte(5)







def combat(health, damage):
    return max(health - damage, 0)

result = combat(100, 20)


def abbrevName(name_list):
    result = []
    for name in name_list:
        parts = name.split(" ")
        result.append(parts[0][0].upper() + "." +  parts[1][0].upper())
    return result
