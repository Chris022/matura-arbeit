## Output File erstellen

### Problem
Der fertig bearbeitete Graph muss nun in ein vom Simulator "LT-Spice" verständliches Format umgewandelt werden.

### Idee
Das Format, indem LT-Spice Schaltungen gespeichert werden, ist ein einfaches ASCII-Format. Kann also relativ einfach erstellt werden. Für mehr Information über die Syntax des Files, siehe LT-Spice Syntax

### LT-Spice Syntax  

Generelle Informationen über die Version und der Größe des LT-Spice Files
```
Version 4
SHEET 1 1000 1000
```


Beispiel für die Platzierung eines Bauteils samt Beschriftung
<bauteil> -> Art des Bauteils ("cap","resistor",...)
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

Für jedes Bauteil muss festgestellt werden, an welchen Koordinaten es mit dem Bauteil verbunden ist.

![Die zwei Möglichkeiten, ein Bauteil anzuschließen](.\Dateien\2MöglichkeitenAnzuschließen.png){width=60%}

Als Erstes bekommt dabei jeder Anschluss eine Nummer zugeordnet.

![Nummerierte Anschlüsse an dem Widerstand](.\Dateien\NummerierteAnschlüsse.png){width=40%}

Die Reihenfolge wird dabei bestimmt durch den Abstand der linken oberen Ecke zu dem jeweiligen Anschluss.

![Abstand, kleinster zu größter aufsteigend](.\Dateien\NummerierteAnschlüsse2.png){width=40%}

Das Selbe wird mit der gezeichneten Schaltung gemacht.

![Abstand, kleinster zu größter aufsteigend](.\Dateien\NummerierteAnschlüsse3.png){width=40%}

Durch diese Information können dann selbe Nummern zusammen geordnet werden und richtig verbunden werden.
Speichere diese Information in den einzelnen Bauteil-Vertices.

![Graph mit Verbindungen gespeichert. In diesem Fall durch die gepunkteten Linien dargestellt](.\Dateien\ConnectionMap.png){width=40%}

---

Für jeden Bauteil-Vertex füge den passenden LT-Spice Code in ein Output-File hinzu. Die Koordinaten entsprechen dabei den in dem Vertex Gespeicherten.

![Widerstand wird als Text in das Output-File gespeichert](.\Dateien\LT-SpicePicture1.png){width=40%}

Für jeden Verbindungs-Vertex, füge den WIRE LT-Spice Code in das Output-File hinzu.

![Verbindungen zwischen den Bauteilen werden in das Output-File geschrieben](.\Dateien\LT-SpicePicture2.png){width=40%}

\newpage

**Problem:** Treffen 2 Bauteile direkt aufeinander  

![Beispiel für eine problematische Schaltung](.\Dateien\Problem1.png){width=40%}

Eine solche Schaltung würde einen solchen Graphen erzeugen.

![Gepunktete Linien stellen zuvor genannte Verbindungen dar](.\Dateien\Problem2.png){width=40%}

Mit der Beschreibung von oben hätte eine solche Schaltung jedoch keine Verbindung zwischen den beiden Widerständen, da ja dort kein Verbindungs-Vertex ist.

**Lösung:**

Sollte einer der Vertices mit denen ein Bauteil verbunden wird, ein weiterer Bauteil-Vertex sein, füge ein WIRE vom Anschluss des Bauteils bis zur Mitte, zwischen den beiden Bauteilen ein!

![Schritt 1](.\Dateien\Lösung1.png){width=40%}

Das selbe wird auch für den zweiten Widerstand gemacht.

![Schritt 2](.\Dateien\Lösung2.png){width=40%}

Die Lösung mit einer Linie nur bis zu Mitte der beiden Bauteile, wurde gewählt, da ein Bauteil somit nicht wissen muss, welches Bauteil sein Nachbar ist.