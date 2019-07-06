alter = 5
while alter <= 25:
    if alter < 13:
        print("Orangensaft")
    elif alter < 18:
        print("Cola")
    elif alter < 21:
        print("Bier")
    else:
        print("Whisky")
    alter += 1
print(alter)
del alter
print(alter)
#print(getränk)