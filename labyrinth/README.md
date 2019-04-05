# Aufgaben für das Labyrinth

_Grundsätzlich gilt: Die folgenden Aufgaben kann man einfach lösen indem man die Blöcke und bewegungen einzeln explizit hinschreibt.
Das ist natürlich nicht ziel der Übung, ihr sollt also möglichst viele Schleifen/Funktionen verwenden und
euren Code möglichst wenig wiederholen._

### 1.1

Versucht zunächst das folgende Muster wie in dem Bild dargestellt mit den `block(x, y, "Wasser")` Befehl zu erstellen.

![alt text](labyrinth/muster_schräg.png)

### 1.2

Versucht dann euren Charakter mit den Befehlen `bewegung("Runter")`, `bewegung("Rechts")`, `bewegung("Links")` und `bewegung("Hoch")` 
auf kürzestem Wege zum Ziel zu navigieren.

### 1.3 

Dann könnt ihr mal versuchen ob ihr eine generelle Logik für die Bewegung eures charakters schreiben könnt, die das Labyrinth löst. 
Sowas wie "Wenn rechts von mir wasser ist gehe ich runter, ansonsten rechts" funktioniert hier zum Beispiel.

```python
x = 0
y = 0

while block_typ(x, y) != "Ziel":
    ... Hier block typen rechts prüfen und Bewegung auswählen
    ... X und Y updaten nicht vergessen!!!
```
# 2

Wenn ihr noch mehr üben wollt, dann versucht mal dieses etwas schwierigere Muster zu erstellen und zu lösen.

![alt text](labyrinth/muster_zacken.png)
