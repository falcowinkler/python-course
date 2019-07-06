

woerterbuch = {"cat": "Katze", "platypus": "Schnabeltier", "rain" : "Regen"}

while False:
    user_eingabe = input("Bitte wort eingben:")
    if user_eingabe == "quit":
        break
    if user_eingabe in woerterbuch:
        print(woerterbuch[user_eingabe])
    else:
        print("Fehler")
        
        
geheime_zahl = 42

while True:
    user_eingabe = input("Bitte zahl raten:")
 
    try:
        user_eingabe = int(user_eingabe)
    except:
        print("Ungültige eingabe")
        continue
    
    if user_eingabe < geheime_zahl:
        print("Zu klein geraten")
    elif user_eingabe > geheime_zahl:
        print("Zu groß geraten")
    else:
        print("Richtig")
        break


