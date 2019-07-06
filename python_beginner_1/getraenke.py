alter = 0
while alter < 25:
    alter += 1
    print("Alter " + str(alter) + " bekommt: ")
    if alter < 15:
        print("Orangensaft")
    elif alter < 18:
        print("Coca Cola")
    elif alter < 21:
        print("Bier")
    else:
        print("Whiskey")
