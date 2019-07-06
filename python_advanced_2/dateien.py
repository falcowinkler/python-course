with open("wordcount.txt") as wordcount:
    


with open("kundendaten.txt", "a") as file_object:
    file_object.write("Herr Meier, 42, Angestellt\nHerr Müller, 32, Selbstständig")

file_object = open("dateien.py", "r") # read-mode
# Zeile für zeile in einer Schleife
for line in file_object:
    print(line)
    
with open("kundendaten.txt", "r") as file_object, open("ausgabe.txt", "a") as out:
    for line in file_object:
        out.write(line)
    