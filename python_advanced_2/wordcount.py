with open("wordcount.txt","r") as meine_datei:
    counter = 0
    for line in meine_datei:
        woerter = line.split(" ")
        counter += len(line)
    print(counter)