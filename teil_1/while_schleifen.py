# Schleifen sind immer nützlich, wenn ihr sachen wiederholt tun wollt.
# Zum Beispiel wäre es ziemlich nervig eine Codezeile für jeden User zu schreiben, dem ihr eine E-Mail schicken wollt. Mit Schleifen ist sowas aber kein Problem.
# while- Schleifen führen einen Codeblock solange eine Bedingung wahr ist aus.


i = 1

while i <= 10: # während i kleiner ist als 10
    i += 1 # erhöht i um 1. Kurzschreibweise für i = i + 1
    print(i)



b = 1

while b <= 10:
    print(b)
    b += 2
    
# Animation hier: https://goo.gl/images/sdRMLZ

a = 1
while a < 7:
    if a % 2 == 0:
        print(a, "ist gerade")
    else:
        print(a, "ist ungerade")
    a += 1
    
# Animation hier: https://goo.gl/images/bE3Mpq