## Output File erstellen

### Problem
Der fertig bearbeitete Graph muss nun in ein vom Simulator "LT-Spice" verständliches Format umgewandelt werden.

### Idee
Das Format indem LT-Spice Schaltungen gespeichert werden ist ein einfaches ASCII-Format. Kann also relativ einfach erstellt werden. Für mehr Information über die Syntax des Files, siehe LT-Spice Syntax

### LT-Spice Syntax  

Generelle Informationen über die Version und der Größe des LT-Spice Files
```
Version 4
SHEET 1 1000 1000
```


Beispiel für die Platzierung eines Bauteils samt Beschriftung
<bauteil> -> art des Bauteils ("cap","resistor",...)
<R90/R0> -> Die Drehung des Bauteils. Entweder R0 oder R90
<name>  -> Sichtbarer Name des Bauteils
```
SYMBOL <bauteil> <x-pos> <y-pos> <R90/R0>
SYMATTR InstName <name>
```


Platzierung eines Ground Symbols
```
FLAG <x-pos> <y-pos> 0
```

Platzierung eines Kabels um Bauteile zu verbinden
```
WIRE <x-pos-von> <y-pos-von> <x-pos-to> <y-pos-to>
```
\newpage
### Umsetzung

Für jedes Bauteil muss festgestellt werden an welchen Koordinaten es mit den Bauteil verbunden ist.

![Die zwei Möglichkeiten ein Bauteil anzuschließen](.\Dateien\2MöglichkeitenAnzuschließen.png){width=60%}

Als erstes bekommt dabei jeder Anschluss eine Nummer zugeordnet.

![Nummerierte Anschlüsse an dem Widerstand](.\Dateien\NummerierteAnschlüsse.png){width=40%}

Die Reihenfolge wird dabei bestimmt durch den Abstand der linken oberen Ecke zu dem jeweiligen Anschluss.

![Abstand, kleinster zu größter aufsteigend](.\Dateien\NummerierteAnschlüsse2.png){width=40%}

Das Selbe wird mit der gezeichneten Schaltung gemacht.

![Abstand, kleinster zu größter aufsteigend](.\Dateien\NummerierteAnschlüsse3.png){width=40%}

Durch diese Information können dann selbe Nummern zusammen geordnet werden und richtig verbunden werden.
Speichere diese Information in die einzelnen Bauteil Vertices.



---
