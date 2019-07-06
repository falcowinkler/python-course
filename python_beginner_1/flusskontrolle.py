# Häufig möchte man, dass sich ein Programm verschieden verhält je nachdem ob eine bestimmte Bedingung wahr ist,
# oder nicht. Eine Wahrheitsaussage wird in Python über einen besonderen Datentypen modelliert,
# den sogenannten 'Boolean' (benannt nach dem Mathematiker George Boole).
# Dieser Datentyp kann nur zwei Werte annehmen: True und False.

# Eine if-Anweisung nimmt einen Wahrheitswert entgegen,
# und führt den darauffolgenden eingerückten Code-Block nur aus,
# wenn dieser Wert True ist. In einer else - Anweisung kann der
#Codeblock angegeben werden, der alternativ ausgeführt werden soll.

es_ist_heiss = False

if es_ist_heiss:
    print("Sonne")
else:
    print("Schnee")

# Wahrheitswerte lassen sich auch aus Vorbedingungen berechnen.
# Zum Beispiel durch einen Zahlenvergleich.
# Angenommen, ihr möchtet in einem Programm eine Sonne anzeigen,
# wenn die Temperatur über 20 Grad ist. Ganz einfach:
    
temperatur = 30

if temperatur == 20:
    print("Ist gleich 20")
    
if temperatur != 20:
    print("Ist ungleich 20")    

if temperatur <= 0:
    print ("Schnee")

if temperatur > 0 and temperatur < 20:
    print("Regen")
    
if temperatur >= 20:
    print("Sonne")

# Es gibt noch weitere Operatoren zum Vergleichen von Zahlen: <, <=, >, >=, != und ==.
# Kleiner, kleiner gleich, größer, größer gleich und gleich.
# (Doppelt-gleich weil das einfache = für Variablenzuweisung belegt ist).

# Mit der elif Anweisung können wir beliebig viele Bedingungen hintereinander prüfen.
# So lässt sich das Temperatur-Beispiel von eben viel einfacher Aufschreiben.
# Detaillierte Erklärung dazu im Kurs!

temperatur = 8
if temperatur < 10:
    print("Temperatur ist kleiner als 10")
elif temperatur < 20:
    print("Temperatur ist kleiner als 20")
else:
    print("Temperatur ist größer oder gleich 20")
    
    
eingabe = 2

if eingabe == 2:
    print("Riegel")
elif eingabe < 2:
    print("zu wenig")
else:
    print("zu viel")



    
eingabe = 1

if eingabe == 2:
    print("Schokoriegel")
elif eingabe < 2:
    print("zu wenig")
else:
    print("zu viel")



