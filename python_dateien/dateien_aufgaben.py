datei_1 = open("meine_kundendaten.txt", "r")
datei_2 = open("ausgabe.txt", "a")


for line in datei_1:
    if line.startswith("hans"):
        datei_2.write("Säugetier: " + line)
    else:
        datei_2.write(line)
    
datei_1.close()
datei_2.close()
