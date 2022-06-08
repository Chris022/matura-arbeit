# Output File erstellen

## Problem
Der fertig bearbeitete Graph muss nun in ein vom Simulator "LT-Spice" verständliches Format umgewandelt werden.

## Idee
Das Format, indem LT-Spice Schaltungen gespeichert werden, ist ein einfaches ASCII-Format und kann somit relativ einfach generiert werden.

## LT-Spice Syntax  

Generelle Informationen über die Version und der Größe des LT-Spice Files
```
Version 4
SHEET 1 1000 1000
```


Beispiel für die Platzierung eines Bauteils samt Beschriftung:


\<bauteil> ist hierbei die Art des Bauteils ("cap","resistor",...) \
\<R90/R0> ist die Drehung des Bauteils. Entweder R0 oder R90 \
\<name> ist der sichtbare Name des Bauteils
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
## Umsetzung

Grundsätzlich gibt es für ein Bauteil im Graphen mehrere Möglichkeiten wie es in der finalen Schaltung angeschlossen werden kann. Dies kommt daher, da der Graph keine Information über die vertikale und horizontale Spiegelung eines Bauteils gespeichert hat!

![Die zwei Möglichkeiten, einen Widerstand anzuschließen](.\Dateien\2MöglichkeitenAnzuschließen.png){width=60%}

Aus diesem Grund muss im ersten Schritt für jedes Bauteil festgestellt werden, an welchen Anschlüssen, es mit welchen anderen Bauteilen verbunden ist.

Dafür bekommt jeder Anschluss des Bauteils in der finalen Schaltung eine Nummer zugeordnet.

![Nummerierte Anschlüsse an dem Widerstand](.\Dateien\NummerierteAnschlüsse.png){width=40%}

Die Reihenfolge wird bestimmt durch den Abstand der linken oberen Ecke zu dem jeweiligen Anschluss.

![Abstand, kleinster zu größter aufsteigend](.\Dateien\NummerierteAnschlüsse2.png){width=40%}

\newpage

Dasselbe wird mit der gezeichneten Schaltung gemacht.

![Abstand, kleinster zu größter aufsteigend](.\Dateien\NummerierteAnschlüsse3.png){width=40%}

Durch diese Information können dann gleiche Nummern zusammen geordnet, die Anschlüsse richtig verbunden und in die einzelnen Bauteil-Vertices gespeichert werden.

![Graph mit Verbindungen gespeichert.](.\Dateien\ConnectionMap.png){width=40%}

\newpage



Dann muss für jeden Bauteil-Vertex der jeweilige Code (siehe zuvor), welcher ein Bauteil in LT-Spice beschreibt, in ein Output-File eingefügt werden. Die Koordinaten entsprechen dabei den in dem Vertex gespeicherten.

![Widerstand wird als Text in das Output-File gespeichert](.\Dateien\LT-SpicePicture1.png){width=40%}

Für jeden Verbindungs-Vertex, wird ein WIRE LT-Spice Code in das Output-File hinzugefügt.

![Verbindungen zwischen den Bauteilen werden in das Output-File geschrieben](.\Dateien\LT-SpicePicture2.png){width=40%}

\newpage

**Problem:** 

![Beispiel für eine problematische Schaltung](.\Dateien\Problem1.png){width=40%}

Treffen zwei Bauteile direkt aufeinander, würde dies einen solchen Graphen erzeugen.

![Graph für eine Schaltung mit zwei Bauteilen direkt nebeneinander](.\Dateien\Problem2.png){width=40%}

Mit der Beschreibung von oben hätte eine solche Schaltung jedoch keine Verbindung zwischen den beiden Widerständen, da ja dort kein Verbindungs-Vertex ist.

**Lösung:**

Sollte einer der Vertices, mit denen ein Bauteil verbunden ist, ein weiterer Bauteil-Vertex sein, wird ein WIRE vom Anschluss des Bauteils bis zur Mitte, zwischen den beiden Bauteilen eingefügt!

![Einfügen eines WIREs vom Anschluss des Bauteils bis zur Mitte](.\Dateien\Lösung1.png){width=40%}

Das selbe wird auch für den zweiten Widerstand gemacht.

![Einfügen eines WIREs vom Anschluss des Bauteils zur Mitte, für das zweite Bauteil](.\Dateien\Lösung2.png){width=40%}

Diese Lösung wurde gewählt, da ein Bauteil somit nicht wissen muss, welches Bauteil sein Nachbar ist.