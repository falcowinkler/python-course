datei_1 = open("meine_kundendaten.txt", "r")
datei_2 = open("ausgabe.txt", "a")

for line in datei_1:
    datei_2.write(line)
    
datei_1.close()
datei_2.close()
