geheime_zahl = 42

while True:
    user_input = int(input("Zahl eingeben:"))
    if user_input < geheime_zahl:
        print("zu klein")
    elif user_input > geheime_zahl:
        print("zu groß")
    else:
        print("richtig")
        break
    
