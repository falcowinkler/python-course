datei_1 = open("woerter_zaehlen.py", "r")

summe = 0
for line in datei_1:
    summe += len(line.split())
print(summe)

datei_1.close()
